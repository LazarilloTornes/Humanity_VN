#Minijuegos 
#Sopa de Letras
default inicio = None
default seleccion = []
default tablero_deldia = []
default palabras_deldia = []
#para más adelante, crear los archivos de tablero.rpy más adelante
default palabras_noencontradas = ["AVENIDA","ENTRADA","HIELO","MOMENTO","PIERNA","PINGO","PROTESTA","RECUERDO","CAYO"]
default palabras_encontradas = []
default arrastrando = False

init python:
    TABLERO=[
        ["X","Q","Y","P","P","G","X","A","Z","H","P","H"],
        ["R","C","H","L","B","I","D","R","I","T","R","O"],
        ["T","G","M","N","R","I","E","E","X","R","O","G"],
        ["G","N","C","M","N","M","L","R","X","Z","T","N"],
        ["J","J","Q","E","T","O","J","V","N","N","E","I"],
        ["Z","P","V","E","N","T","R","A","D","A","S","P"],
        ["C","A","Y","O","T","N","E","M","O","M","T","T"],
        ["M","Y","Q","W","T","Z","D","G","N","R","A","D"],
        ["T","K","C","O","R","E","C","U","E","R","D","O"],
    ]
    PALABRAS = ["AVENIDA", "ENTRADA", "HIELO", "MOMENTO", "PIERNA", "PINGO", "PROTESTA", "RECUERDO", "CAYO"]
    
    def empezar_arrastre(fila, col):
        # store.arrastrando = True
        # store.inicio = (fila, col)
        # store.seleccion = [(fila, col)]
        coord = (fila, col)
        # si NO estás seleccionando → empiezas
        if not store.arrastrando:
            store.arrastrando = True
            store.inicio = coord
            store.seleccion = [coord]
            return

        # si ya estabas seleccionando → CONFIRMAR
        else:
            terminar_arrastre()

    def pasar_por_celda(fila, col):
        if not store.arrastrando:
            return
        store.seleccion = calcular_linea(
        store.inicio,
        (fila, col)
        )
    def calcular_linea(inicio, fin):

        f1, c1 = inicio
        f2, c2 = fin

        df = f2 - f1
        dc = c2 - c1

        # Solo horizontal, vertical o diagonal
        if not (
            df == 0 or
            dc == 0 or
            abs(df) == abs(dc)
        ):
            return []

        paso_f = 0 if df == 0 else (1 if df > 0 else -1)
        paso_c = 0 if dc == 0 else (1 if dc > 0 else -1)

        longitud = max(abs(df), abs(dc))

        return [
            (f1 + i * paso_f, c1 + i * paso_c)
            for i in range(longitud + 1)
        ]
                
    def terminar_arrastre():
        store.arrastrando = False
        palabra = "".join(TABLERO[fila][col] for fila, col in store.seleccion)
        palabra_inv = palabra[::-1]
        if palabra in PALABRAS or palabra_inv in PALABRAS:        
            renpy.notify("Encontrada: " + (palabra if palabra in PALABRAS else palabra_inv))
            store.palabras_encontradas.append(palabra)
            if palabra in palabras_encontradas and palabra in palabras_noencontradas:
                palabras_noencontradas.remove(palabra)
            store.seleccion = []
        else:
            renpy.notify("Palabra no encontrada")
            store.seleccion = []

                      
    def restart_seleccion():        
        store.seleccion = []
screen sopa_letras():
    add "bg soup.png" xsize config.screen_width ysize config.screen_height
    zorder 100 
    timer 0.1 repeat True action If(
        len(palabras_noencontradas) == 0,
        Jump("winSopaLetras"),
        NullAction()
    )
    #añadir foto de mesa con el libro abierto y un rotu al lado add "bg soup.png"
    frame:
        
        xpos 110
        ypos 100
        xsize 1040
        ysize 560
        vbox:
            xpos 800
            ypos 5
            for j in palabras_noencontradas:
                textbutton "[j]":
                    text_style "txtSoup"
    
        fixed:
            

            for fila in range(len(TABLERO)):
                for col in range(len(TABLERO[0])):
                        textbutton TABLERO[fila][col]:
                            style ("txtSelected" if (fila, col) in store.seleccion else "txtSoup")
                            text_style "txtSoup"
                            xpos col * 60
                            ypos fila * 60
                            xsize 60
                            ysize 60
                            action Function(empezar_arrastre,fila,col)
                            hovered Function(pasar_por_celda, fila, col)
            imagebutton:
                idle "closebutton.png"
                hover "closebutton.png"
                xpos 500
                ypos 800
                action Hide("sopa_letras")
default soup_of_the_day = False
label winSopaLetras:
    hide screen sopa_letras
    $ hour += 1
    "Has completado la Sopa de Letras de hoy"
    "Sientes que has invertido más tiempo de lo que deberías en este juego"
    "Mañana podrás hacer otra diferente"
    $ soup_of_the_day = True
    hide screen sopa_letras
    hide mainroom
    jump main_loop
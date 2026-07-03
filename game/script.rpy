# Coloca el código de tu juego en este archivo.
# Declara los personajes usados en el juego como en el ejemplo:
define p = Character(("[player_name]"), color="#cdcdcd")
define plNews = Character(("Presentador de noticias"), color="#9ba5d8")
define plAdd = Character (("Anunciador Entusiastico"), color="#f1f1d3")
define plAdd2 = Character (("Anunciador Tranquilo"), color="#d4f1d3")
define c = Character(("Carnicera"), color="#d99d9d")
define t = Character(("Trabajadora Telefónica"), color="#d3ebea")
#variable que determina que hora va a ser
#image bg_bathroom = "bathroom.png"
#screen funciona como una funcion para crear un "escenario", esto puede servir más adelante para la crear la dinámica de libertad de exploración
image eat = im.Scale("bg eater.jpeg", 1800, 1080)
image bg_superkmarket = im.Scale("bg supermarket.png", config.screen_width, config.screen_height)
image bg_verduras = im.Scale("bg verdura.png", config.screen_width, config.screen_height)
image bg_pasta = im.Scale("bg pasta.png", config.screen_width, config.screen_height)
image bg_carniceria = im.Scale("bg carniceria.png", config.screen_width, config.screen_height)
image bg_capricho = im.Scale("bg capricho.png", config.screen_width, config.screen_height)
image bg_sopa_instantanea = im.Scale("bg sopa.png", config.screen_width, config.screen_height)
image bg_ventana = im.Scale("bg ventana.png", config.screen_width, config.screen_height)
image bg_pagar = im.Scale("bg pagar.jpg", config.screen_width, config.screen_height)
image mainroom = "mainroom.png"
image livingroom = "livingroom.png"
image ticket = "ticket.png"




default player_name = "Bolonga"




#Dinero y comida
default dinero = 50
default food = 0

#la comida suele durar 3 días, teniendo un máximo de 3
#En la intro empieza en 0, sin embargo se obligará a la persona a hacer la compra
#En la aplicación donde se mira eso aparecerá:
#Tienes comida para: ["food"] días.
#
#






#variable que controla el paso de los días, el día 0 es básicamente la intro
default day = 0
default room = "mainroom"





#Todos los estilos de letras
style txtRoom:
    color "#f0dfdc"
style btnSoup:
    background "#f5f0e3"
    padding (10, 10)
style text_notify:
    color "#270303ff"
style txtActions:
    color "#3a0c0c"
style txtContacts:
    size 25
    color "#273529"
    line_spacing 2
    font "Pixel Digivolve.otf"
style txtMinesweeper:
    size 22
    color "#273529"
    padding (12, 12)
    background "#cddbc8"
    font "Pixel Digivolve.otf"
style txtSoup:
    size 35
    color "#273529"
    padding (12, 12)
style txtSelected:
    size 35
    color "#273529"
    padding(12,12)
    background "#ffd54a"
style txtPhone:
    size 30
    color "#1e2c20"
    font "Pixel Digivolve.otf"
style txtClock:
    size 32
    color "#3a0c0c" 
    font "Pixel Digivolve.otf"




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



#Minigames upcoming






#Minesweeper game
#celd_status = 0 nothing
#celd_status = -1 mine

#what coordenates I have to search
# x-1,y-1   x,y-1   x+1,y-1
# x-1,y     x,y     x+1,y
# x-1,y+1   x,y+1   x+1,y+1
init python:
    import random
    
    mine = []
    WIDTH = 8 #puede ser el número que sea
    HEIGHT = 8
    MINES = 8


    all_posible_positions = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            all_posible_positions.append((x, y))
    #Working with the visual grid thingy 
    HIDDEN = 0
    REVEALED = 1
    FLAGGED = 2
    #Establish all the celds in 0 not mine
    #Board stores "mine" or "number"
    board = [
        [0 for x in range(WIDTH)]
        for y in range(HEIGHT)
    ]
    #State stores the "revealed", "hiden" and "Flag"
    state = [
        [HIDDEN for x in range(WIDTH)]
        for y in range(HEIGHT)
    ]

    
    mines = random.sample(all_posible_positions,8) 
    for x,y in mines:
        board[y][x] = -1 #Establish all the coordenates with mines


    def count_mines(x, y):

        count = 0

        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):

                if dx == 0 and dy == 0:
                    continue

                nx = x + dx
                ny = y + dy

                if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:

                    if board[ny][nx] == -1:
                        count += 1
        return count
    def generate_numbers():

        for y in range(HEIGHT):
            for x in range(WIDTH):

                if board[y][x] == -1:
                    continue

                board[y][x] = count_mines(x, y)

    def flood_fill(x, y):

        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):

                nx = x + dx
                ny = y + dy

                if not (0 <= nx < WIDTH and 0 <= ny < HEIGHT):
                    continue

                if state[ny][nx] == REVEALED:
                    continue

                if board[ny][nx] == -1:
                    continue

                state[ny][nx] = REVEALED

                # if empty, keep expanding
                if board[ny][nx] == 0:
                    flood_fill(nx, ny)


    generate_numbers()

    def reset_game():
        global board, state, mines
        board = [
            [0 for x in range(WIDTH)]
            for y in range(HEIGHT)
        ]
        #State stores the "revealed", "hiden" and "Flag"
        state = [
            [HIDDEN for x in range(WIDTH)]
            for y in range(HEIGHT)
        ]
        mines = random.sample(all_posible_positions,12) 
        for x,y in mines:
            board[y][x] = -1 #Establish all the coordenates with mines
            count_mines(x,y)
            generate_numbers()



    #I mean, this is pretty simple
    def reveal_cell(x, y):
        if state[y][x] == REVEALED:
            return
        state[y][x] = REVEALED
        if board[y][x] == -1:
            renpy.notify( "Boom!")
            return
        # if empty → flood fill
        if board[y][x] == 0:
            flood_fill(x, y)
        if check_win():
            renpy.notify("¡Has ganado!")
            renpy.restart_interaction()
    def toggle_flag(x, y):

        if state[y][x] == REVEALED:
            return
        if state[y][x] == FLAGGED:
            state[y][x] = HIDDEN
        else:
            state[y][x] = FLAGGED
    def check_win():

        for y in range(HEIGHT):
            for x in range(WIDTH):

                # Si una casilla NO es mina y sigue oculta,
                # aún no ha ganado.
                if board[y][x] != -1 and state[y][x] != REVEALED:
                    return False

        return True
    
    
default tool_mode = "REVELAR"  # or "flag"    
default win = True    


#que en vez de dividirse en partes el avance del día, cada actividad te consuma tiempo
#Ver la tele
#Escribir
#Leer




#En efecto, el juego del buscaminas esta incorporado en el telefono
default phone_tab = "home"
default contacts = ["AAMamá","AAPapá"]
default phone_open = False
default open_contacts = False
default selected_contact = None
screen phone():
    if open_contacts == False:
        modal True
    else:
        modal False
    $ phone_open = True
    add "phone.png":
        xalign 0.95
        yalign 0.45
        xsize 500
        ysize 1070
        

    if phone_tab == "home":
        imagebutton:
            idle "closebutton.png"
            hover "closebutton.png"
            xpos 1700
            ypos 370
            action SetVariable("phone_open", False), Hide("phone"), Jump("main_loop")
        imagebutton:
            idle "contactsbutton.png"
            hover "contactsbutton.png"
            xsize 100
            ysize 100
            xpos 1470
            ypos 250
            action SetVariable("phone_tab", "contacts"),SetVariable("open_contacts", True), Show("phone")
        imagebutton:
            idle "minesweeperbutton.png"
            hover "minesweeperbutton.png"
            xsize 100
            ysize 100
            xpos 1530
            ypos 250
            action SetVariable("phone_tab", "minesweeper"), Show("phone")
        imagebutton:
            idle "bank_button.png"
            hover "bank_button.png"
            xsize 100
            ysize 100
            xpos 1590
            ypos 250
            action SetVariable("phone_tab", "bank"), Show("phone")
        if alquilar:
            $ phone_open = True
            imagebutton:
                idle "rent_button.png"
                hover "rent_button.png"
                xsize 100
                ysize 100
                xpos 1470
                ypos 310
                action SetVariable("phone_tab", "rent"), Show("phone")
    elif phone_tab == "contacts":
        
        imagebutton:
            idle "back_button.png"
            hover "back_button.png"
            xpos 1470
            ypos 370
            action SetVariable("phone_tab", "home"), Show("phone")
        viewport:
            xsize 210
            ysize 170
            xpos 1490
            ypos 250
            scrollbars "vertical"
            mousewheel True
            draggable True
            vbox:
                spacing 10
                
                for i in contacts:
                    textbutton "[i]":
                        text_style "txtContacts"
                        action If(
                            i == "661",
                            [Jump("dlg_661"), Hide("phone"), SetVariable("phone_open", False)],
                            If(
                                i == "627",
                                Jump("dlg_627"),
                                If(
                                    i == "AAMamá",
                                    Jump("dlg_mama"),
                                    If(
                                        i == "AAPapá",
                                        Jump("dlg_papa"),
                                        NullAction()
                                    )
                                )
                            )
                        )
    elif phone_tab == "minesweeper":
        
        frame:
            xpos 1405
            ypos 95
            xsize 410
            ysize 860
            xpadding 20
            ypadding 20
            background "#6e766bff"

            grid WIDTH HEIGHT:
                
                spacing 2
                xalign 0.5
                yalign 0.5
                for y in range(HEIGHT):
                    for x in range(WIDTH):
                        if state[y][x] == HIDDEN:
                            frame:
                                xsize 45
                                ysize 45
                                background "#585d57"

                                textbutton "":
                                    action If(tool_mode == "BANDERIN",
                                    Function(toggle_flag, x, y),
                                    Function(reveal_cell, x, y))
                                    xfill True
                                    yfill True
                        elif state[y][x] == FLAGGED:
                            frame:
                                xsize 45
                                ysize 45
                                background "#585d57"
                                text "🚩"
                        else:
                            frame:
                                xsize 45
                                ysize 45
                                background "#ccc"   # light color

                                if board[y][x] == -1:
                                    text "💣" style "txtMinesweeper"
                                    $ win = False
                                elif board[y][x] > 0:
                                    text str(board[y][x]) style "txtMinesweeper"
                                else:
                                    text "" style "txtMinesweeper"
        textbutton "[tool_mode]":    
            xpos 1500
            ypos 150
            padding (15, 10)
            background "#bbc5b9"
            action If(tool_mode == "REVELAR",
                    SetVariable("tool_mode", "BANDERIN"),
                    SetVariable("tool_mode", "REVELAR"))
        imagebutton:
            idle "back_button.png"
            hover "back_button.png"
            xpos 1530
            ypos 900
            action SetVariable("phone_tab","home"), Show("phone")
        imagebutton:
            idle "reset_button.png"
            hover "reset_button.png"
            xpos 1460
            ypos 900
            action Function(reset_game)
    elif phone_tab == "bank":
        imagebutton:
            idle "back_button.png"
            hover "back_button.png"
            xpos 1470
            ypos 370
            action SetVariable("phone_tab", "home"), Show("phone")
        textbutton "Saldo: [dinero]$":
            text_style "txtContacts"
            xpos 1450  
            ypos 250
            padding (15, 10)
            #background "#e6f4e1"
            action NullAction()
        textbutton "Dinero gastado: [dinero_gastado]$":
            text_style "txtContacts"
            xpos 1450  
            ypos 280
            padding (15, 10)
            #background "#e6f4e1"
            action NullAction()
        textbutton "Dinero ganado: 0$": #cambiar esto más adelante, pero por ahora lo dejaremos así
            text_style "txtContacts"
            xpos 1450  
            ypos 310
            padding (15, 10)
            #background "#e6f4e1"
            action NullAction()
    elif phone_tab == "rent_room":
        if day == 0:
            textbutton "No hay solicitudes :(":
                xpos 1450  
                ypos 310
                padding (15, 10)
                text_style "txtContacts"
        else:
            textbutton "Wilson":
                xpos 1450  
                ypos 310
                padding (15, 10)
                text_style "txtContacts"
        imagebutton:
            idle "back_button.png"
            hover "back_button.png"
            xpos 1530
            ypos 900
            action SetVariable("phone_tab","home"), Show("phone")
#Aquí todas las llamadas
default qt_661 = ["Preguntar para alquilar la habitación","Preguntar detalles sobre la compañía","Mejor nada..."]
default alquilar = False
label dlg_mama:  
    show black
    stop music fadeout 1.0
    play sound "audio/call.mp3" fadein 0.5
    pause 
    stop sound fadeout 0.5
    play music "audio/ambientedia.mp3" loop volume 0.2 fadein 0.5
    "{cps=15}No parece que vaya a responder...{/cps}"
    hide black
    jump main_loop
label dlg_papa: 
    show black
    stop music fadeout 1.0
    play sound "audio/call.mp3" fadein 0.5
    pause 10
    stop sound fadeout 0.5
    play music "audio/ambientedia.mp3" loop volume 0.2 fadein 0.5
    "{cps=15}No parece que vaya a responder...{/cps}"
    hide black
    jump main_loop
label dlg_661: 
    stop music fadeout 1.0
    play sound "audio/call.mp3" fadein 0.5
    pause 2.5
    stop sound fadeout 0.5
    play music "audio/ambientedia.mp3" loop volume 0.2 fadein 0.5
    if alquilar == False:
        t "{cps=15}Hola, buenos días, podría decirme su nombre para dirigirme a usted?{/cps}"
        p "{cps=15}[player_name]{/cps}"
        t "{cps=15}Y cuénteme [player_name], en que le puedo ayudar?{/cps}"
    else:
        t "{cps=15}Hola de nuevo [player_name], dime, en que te puedo ayudar?{/cps}"
    menu:
        "Preguntar para alquilar la habitación" if "Preguntar para alquilar la habitación" in qt_661:
            $ qt_661.remove("Preguntar para alquilar la habitación")
            p "{cps=15}Pues, me gustaría alquilar una habitación que tengo vacia en mi apartamento{/cps}"
            t "{cps=18}Perfecto, pues dígame su dirección{/cps}"
            p "XXXXXX, XXXX XXXXX, XXXXX 1, XXXX"
            pause 2.0
            t "{cps=18}Vale, ya te tengo{/cps}"
            t "{cps=18}Me podrías dar algunos detalles de la casa y de la habitación?{/cps}"
            menu:
                "Decir que es normal sin nada especial": 
                    p "{cps=14}Es una casa normal con 2 habitaciones, un salón, una cocina... lo que todas las casas tienen.{/cps}"
                    pause 1
                    t "{cps=18}Bueno, lo tendremos en cuenta{/cps}"
                "Decir que es lujosa y mentir":
                    p "{cps=14}Será la mejor casa del mercado, con incontables lujos, la mejor televisión, piso completamente nuevo y decorado.{/cps}"
                    t "{cps=18}En serio?{/cps}"
                    t "{cps=14}...{/cps}"
                    t "{cps=18}Lo cierto es que usted vive en un barrio bastante antiguo...{/cps}"
                    t "{cps=18}Pero bueno, lo que usted diga{/cps}"
                "Decir que es decente pero acogedora":
                    p "{cps=14}Es una casa modesta y cómoda, ordenada, con todo lo necesario para vivir pero sin ningún lujo caro.{/cps}"
                    t "{cps=18}Perfecto, es justo lo que buscabamos{/cps}"
            pause 2
            t "{cps=18}Pues mire [player_name], viendo el barrio en el que vives y con lo que me has dicho de la habitación, podríamos darle una estimación de 71$ la semana{/cps}"
            menu:
                "Me parece poco dinero":
                    t "{cps=18}Le entiendo, pero hoy en día el mercado trabaja con esos precios, si lo subimos más seguramente tardaría una eternidad en venderse{/cps}"
                "Perfecto":
                    t "{cps=18}Me alegra escuchar eso{/cps}"
                "Me parece demasiado dinero":
                    t "{cps=14}Podríamos bajarlo más si lo desea...{/cps}"
                    menu:
                        "Sí por favor":
                            t "{cps=14}Lo mázimo que lo puedo bajar es a 70${/cps}"
                            t "{cps=18}Pero bueno{/cps}"
                        "Mejor no":
                            t "{cps=18}Entendible{/cps}"
            t "{cps=18}Pues le cuento, nosotros nos encargaremos de buscar los inquilinos, le mandaremos atraves de una aplicación todos los interesados, tu podrás organizar las entrevistas como quieras{/cps}"
            t "{cps=18}En cuanto al pago del alquiler nosotros nos encargaremos de ingresarte el dinero que nos den los inquilinos{/cps}"
            t "{cps=18}Y si necesita cualquier otra cosa no dude en volver a llamar{/cps}"
            t "{cps=18}Nosotros le ayudaremos con lo que sea{/cps}"
            play sound "audio/hang_up.mp3"
            pause 0.5
            "{cps=14}Pues te ha colgado...{/cps}"
            $ alquilar = True
            jump main_loop
        "Preguntar detalles sobre la compañía":
            t "{cps=18}Muy bien, y que le gustaría saber?{/cps}"
            menu:
                "Como funciona el alquiler de la habitación":
                    t "{cps=18}Te cuento{/cps}"
                    t "{cps=18}En el momento que aceptas a un inquilino este tiene que pagar por adelantado un porcentaje del alquiler{/cps}"
                    t "{cps=18}Ese dinero se transferirá directamente a nosotros{/cps}"
                    t "{cps=18}Para posteriormente depositarlo en tu cuenta bancaria{/cps}"
                    t "{cps=18}Así evitamos tramites inoportunos y controlamos las cuentas globales de la empresa{/cps}"
                "Como se buscan inquilinos":
                    t "{cps=18}Pues verás [player_name]{/cps}"
                    t "{cps=18}Nosotros subimos a nuestra web el piso, la dirección y el precio, colgamos carteles o incluso los ponemos de exposición en nuestro local{/cps}"
                    t "{cps=18}Y así cualquier persona que esté interesada puede preguntar o mandar una solicitud{/cps}"
                    return                
                "Nada":
                    return
            jump main_loop
        "Mejor nada...":
            jump main_loop
        

label dlg_627: 
#label dlg_:                         


















#Actualizar todo lo relacionado con el tiempo
default hour = 9
default eathour = "Desayunar"
default day_moment = "Intro"
default phone_disponible = False



screen digital_clock:

    zorder 100
    textbutton "[hour:02d]:00":
        text_style "txtClock"
        xalign 0.95  
        yalign 0.05
        padding (15, 10)
        background "#cddbc8"
        action NullAction()
    textbutton "Telefono":
        text_style "txtPhone"
        xalign 0.85  
        yalign 0.05
        padding (15, 10)
        background "#a9b4a5"
        action SetVariable("phone_open", True), Show("phone")



label dlg_bed:
    if 9 <= hour <= 13:
        show mainroom
        "Aquí yace tu cómoda cama, de la cual te acabas de levantar."
        "{cps=4}. . . {/cps}"
        "No creo que quieras seguir durmiendo"
        hide mainroom
        call screen Mr_Game_and_Watch

    elif 14 <= hour <= 19:
        "Vas a echarte una siesta de verdad? Y no prefieres disfrutar del tiempo libre que tienes?"
    return
    

label dlg_wordsearch:
    show mainroom
    "Es la antigua revista de Sopa de Letras de tu abuelo. Parece estar solo en Español"
    if hour == 9:
        "Despues de desayunar podrías hacer una"
        hide mainroom
        return
    elif hour == 13:
        "Es hora de comer, mejor dejar la sopa de letras para otro momento"
        hide mainroom
        return
    elif hour == 20:
        "Ya es hora de cenar, dejemos los pasatiempos para otro momento"
        hide mainroom
    elif soup_of_the_day:
        "Ya has completado la sopa de letras diaria, mañana podrás hacer otra"
        hide mainroom
    elif  hour < 21 and soup_of_the_day == False:
        "Quieres resolver una sopa de letras?"
        menu:
            "Sí":
                show screen sopa_letras
                return
            "No":
                "Mejor para más tarde"
                hide mainroom
                return
    return
    hide mainroom

label dlg_eat:
    show kitchen
    if hour == 9:
        play sound "audio/kitchen.mp3"
        pause 2.5
        stop sound
        "{cps=16}Será mejor desayunar en el salón{/cps}"
        pause 2.0
        "{cps=16}Mirándolo bien, no queda casi nada de comida, tendrás que hacer la compra esta tarde{/cps}"
        window hide
        show hall2
        pause 1
        hide hall2
        show livingroom
        pause 0.5
        "Bon Apetite"
        hide livingroom
        show eat
        play sound "audio/comer.mp3"
        pause 0.5
        "{cps=16}Buscando entre los cojines encuentras el mando de la televisión y la enciendes{/cps}"
        play sound "audio/button.mp3"
        stop sound
        call news
    elif 9 < hour < 13:
        "{cps=16}Ya has desayunado...{/cps}"
        "{cps=16}Para que quieres desayunar otra vez{/cps}"
    elif hour == 13:
        "Hola"
    elif 13 < hour < 20:
        "{cps=16}Ya has comido...{/cps}"
        "{cps=16}Para que quieres comer otra vez{/cps}"
    elif hour == 20:
        "Hola"
    elif 20 < hour < 23:
        "{cps=16}Ya has cenado...{/cps}"
        "{cps=16}Para que quieres cenar otra vez{/cps}"
    hide kitchen
    return


default pelicula = False
label dlg_sofa:
    show livingroom
    "{cps=15}El antiguo sofá de tu abuelo...{/cps}"
    if pelicula:
        "Que película quieres ver?"
    else:
        "{cps=15}Podríamos ver una peli{/cps}"
        "Otro día"
    #más adelante incorporar la opción de ver series o peliculas
    if hour == 13:
        "Quieres comer aquí?"
    elif hour == 20:
        "Quieres cenar aquí?"
    hide livingroom
    return
label dlg_window:
    show bg_ventana with dissolve
    if hour == 9:
        "Será mejor desayunar primero"
        hide bg_ventana
        return
    elif hour == 13:
        "Ya es la hora de comer, mejor pensar en otro momento"
    elif hour == 20:
        "Es hora de cenar... ve a la cocina y pilla algo"
    else:
        #Aquí dentro compruebas que día es, según el día que sea, se mostrará un menú u otro
        pause
        "{cps=15}Sientes que podrías perderte en tus pensamientos por un momento{/cps}"
        "{cps=15}Descansar"
        "{cps=15}Cavilar en las ocurrencias del hoy y el mañana{/cps}"
        #Para controlar que ocurrencias pensar basta con controlarlo en if day == x then el menu que corresponda
        menu:
            "{cps=15}Deseas seguir mirando por la ventana?{/cps}"
            "Sí":
                "{cps=15}Ahora que estas sol[articulo], puede ser la oportunidad de pensar con más tranquilidad{/cps}"
                "{cps=15}Alejad[articulo] de los gritos, las broncas y discusiones sin sentido que suelen tener tus padres{/cps}"
                "{cps=3}. . .{/cps}"
                "{cps=15}Sinceramente, resulta preocupante{/cps}"
                "{cps=15}Has estado intentando contactar con tus padres días atrás, pero estos ni cogen las llamadas ni las devuelven{/cps}"
                "{cps=12}Incluso te llegan a colgar antes de contestarte{/cps}"
                pause 2
                "{cps=18}Cambiando de tema{/cps}"
                "{cps=14}Teniendo todo el tiempo libre del mundo podrías retomar antiguos hábitos{/cps}"
                "{cps=14}Como leer, escribir, ver alguna serie, jugar a alguno de los jueguitos antiguos que tenia tu abuelo...{/cps}"
                "{cps=18}O buscar trabajo{/cps}"
                "{cps=15}Seria una buena manera de pasar el tiempo{/cps}"
                pause 2
                "{cps=15}Hablando de trabajo{/cps}"
                "{cps=15}Lo cierto es que no te queda mucho dinero, y la verdad es que necesitas al menos una fuente de ingresos{/cps}"
                "{cps=15}Después de todo, la comida no es gratis{/cps}"
                pause 1
                "{cps=14}Puede ser un buen momento para alquilar la otra habitación que tienes en el piso{/cps}"
                "{cps=14}Ni siquiera la usas para nada{/cps}"
                "{cps=14}Solo está ahí{/cps}"
                "{cps=14}Acumulando polvo{/cps}"
                "{cps=15}Pero bueno, será mejor proseguir con el día.{/cps}"
                hide bg_ventana
                return
                
            "No":
                "{cps=3}. . .{/cps}"
                "{cps=15}Mejor en otro momento{/cps}"
                hide bg_ventana
                return
  







label news:
    show eat
    #all the news will be condicionate by the day
    stop music fadeout 1.0
    play music "audio/news.mp3" volume 0.17
    plNews "{cps=16}Buenas tardes, y bienvenidos a las noticias de la ciudad, hoy es un día soleado y caluroso, con temperaturas que alcanzarán los 33 grados, así que no olviden hidratarse y usar protector solar.{/cps}"
    plNews "{cps=16}En otras noticias, se han reportado varios casos de una nueva cepa estacional.{/cps}"
    plNews "{cps=16}Los contagiados presentan síntomas similares a una gripe o resfriado común, con la ligera diferencia de provocar insomnio en un pequeño número de pacientes.{/cps}"
    plNews "{cps=16}Se han reportado 21 enfermos hasta el momento, y ningún caso grabe ni fallecimiento.{/cps}"
    plNews "{cps=16}Y esas han sido las noticias de hoy, gracias por su atención y que tengan un buen día.{/cps}"
    plNews "{cps=16}Volvemos en 1 minuto{/cps}"
    stop music fadeout 0.5
    pause 1.0
    play music "audio/addmusic.mp3" volume 0.17 
    plAdd "{cps=20}¿Te sientes solo? ¿Estas buscando compañía y necesitas dinero?{/cps}"
    plAdd "{cps=20}¡Pues ahora puedes alquilar tu habitación semanalmente con la mejor compañía del mercado!{/cps}"
    p "{cps=5}Mmmmmm...{/cps}{cps=16}No suena mal del todo{/cps}"
    plAdd "{cps=18}Hacemos el presupuesto y te ayudamos a venderla rápido y seguro. ¡En menos de una semana!{/cps}"
    plAdd "{cps=16}Llama hoy al 661 y nosotros nos encargamos del resto!{/cps}"
    $ renpy.notify("Nuevo número registrado: 661")
    $ contacts.append("661")
    pause 0.5
    stop music fadeout 0.5
    play music "audio/addmusic2.mp3" volume 0.17 fadein 0.5
    plAdd2 "{cps=16}Esta semana la comida viene a tu casa con descuento{/cps}"
    #para añadir el signo de porcentaje en un string se debe poner doble porcentaje, ya que el primero es para escapar el segundo
    plAdd2 "{cps=15}Consigue hasta un 50%% en tu próximo pedido a domicilio. {/cps}"
    plAdd2 "{cps=18}Llama ya al 627 y pide lo que quieras.{/cps}"
    $ renpy.notify("Nuevo número registrado: 627")
    $ contacts.append("627")
    play sound "audio/comer.mp3" loop
    pause 
    stop sound fadeout 0.5
    narrator "{cps=16}Bueno, suficientes noticias por hoy, creo que es hora de ir a comprar todo lo que te falta{/cps}"
    "De paso sales y aprovechas la mañana"
    play music "audio/ambientedia.mp3" loop fadein 0.5
    $ room = "livingroom"
    $ hour += 1
    $ doorEvent = 1
    hide eat
    return




default doorEvent = 0
label lookoutside():
    if doorEvent == 0 or doorEvent == 2:
        show bg outside
        "No parece haber mucho movimiento ahí fuera"
        hide bg outside
        return
    elif doorEvent == 1:
        menu:
            "Quieres salir a hacer la compra?"
            "Sí":
                pause 1.0
                "{cps=15} Antes de salir...{/cps}"
                "{cps=15} Cuanto dinero te queda...{/cps}"
                show screen compra
                "{cps=15}Tienes [dinero]$ en tu bolsillo{/cps}"
                "{cps=16}Te da de sobra para hacer la compra{/cps}"
                $ doorEvent = 2
                jump hacer_compra
            "Aún no...":
                "Esta bien, comprueba que no te dejas nada"
                jump main_loop





default lista_compra = ["Carne","Verduras","Pasta", "Comida Instantánea", "Capricho"]
default dinero_gastado = 0
screen compra:
    zorder 200
    textbutton "Dinero: [dinero]$":
        text_style "txtClock"
        xalign 0.85  
        yalign 0.05
        padding (15, 10)
        background "#e6f4e1"
        action NullAction()
label hacer_compra:
    show black
    play sound "audio/door_slam.mp3"
    stop music
    pause 4
    show bg_superkmarket with dissolve
    "{cps=15}Acabas llegando al supermercado más cercano de tu casa, y al que has estado yendo básicamente para cualquier tontería.{/cps}"
    "{cps=15} Así que hoy para comprar hay...{/cps}"
    "{cps=15}Algo de carne{/cps}"
    "{cps=15}Verduras{/cps}"
    "{cps=15}Alguna sopa de estas que se hacen en 5min{/cps}"
    "{cps=15}Pasta{/cps}"
    "{cps=15}Y quizás algun capricho{/cps}"
    "{cps=15}Lo suficiente para sobrevivir{/cps}"
    hide bg_superkmarket with fade
    play music "audio/supermarket.mp3" loop volume 0.5 
    show bg_pasta with dissolve 
    "{cps=15}Parece estar más abarrotado de lo que creías{/cps}"
    "{cps=15}La gente parece nerviosa{/cps}"
    "{cps=15}Agetreada{/cps}"
    #p "Pero no le di importancia..."
    p "{cps=15}Pero... que comprar primero{/cps}"
    stop music
    hide bg_pasta with fade




label menu_compra:
    show black
    play music "audio/supermarket.mp3" loop volume 0.5 fadein 0.5
    show bg_pasta with dissolve
    if not lista_compra:
        "Ya has comprado todo, ya podemos ir a pagar..."
        hide screen compra
        hide bg_pasta with dissolve
        stop music fadeout 0.0
        $ hour += 1
        $ food = 3
        jump pagar_compra
    else:
        
        menu:
            "..."
            "Carne" if "Carne" in lista_compra:
                hide bg_pasta 
                $ lista_compra.remove("Carne")
                call carniceria 
                jump menu_compra
            "Verduras" if "Verduras" in lista_compra:
                $ lista_compra.remove("Verduras")
                hide bg_pasta 
                call verduras
                jump menu_compra
            "Pasta" if "Pasta" in lista_compra:
                $ lista_compra.remove("Pasta")
                hide bg_pasta 
                call macarrones
                jump menu_compra
            "Comida Instantánea" if "Comida Instantánea" in lista_compra:
                $ lista_compra.remove("Comida Instantánea")
                hide bg_pasta 
                call comida_instantanea
                jump menu_compra
            "Capricho" if "Capricho" in lista_compra:
                $ lista_compra.remove("Capricho")
                hide bg_pasta 
                call capricho
                jump menu_compra
    hide bg_pasta 
    return
                                                  
label carniceria:
    stop music fadeout 1.0
    play music "audio/butcher.mp3" loop volume 0.2
    show bg_carniceria 
    "{cps=16}Coges un tiquet y te sientas hasta que te toque tu turno{/cps}"
    show ticket at Position(xalign=0.5, yalign=0.5) onlayer overlay
    pause 1.0
    hide ticket with dissolve
    "{cps=14}Al menos tienen buena música de ambiente...{/cps}"
    $ renpy.notify("Pulsa espacio para avanzar")
    pause
    c "¡{cps=27}{b}{size=50}557?!{/size}{/b}{/cps}"
    "{cps=14}wow,{w=0.1} eso fue rápido{/cps}"
    stop music fadeout 1.0
    menu:
        c "{cps=16}Que quieres?{/cps}"
        "Solomillo de cerdo: 13$/kg":
            c "{cps=16}Aquí tienes{/cps}"
            $ dinero -= 13
            $ dinero_gastado += 13
            hide bg_carniceria
            show black with dissolve
            play sound "audio/meat.mp3"
            pause 1
            show bg_carniceria 
            c "{cps=16}Todo listo{/cps}"
            hide bg_carniceria with dissolve
            
            return
        "Ternera: 16$/kg":
            c "{cps=16}Aquí tienes{/cps}"
            $ dinero -= 16
            $ dinero_gastado += 16
            hide bg_carniceria
            show black with dissolve
            play sound "audio/meat.mp3"
            pause 1
            show bg_carniceria
            c "{cps=16}Todo listo{/cps}"
            hide bg_carniceria with dissolve
            
            return
        "Alitas de pollo: 6.50$/kg":
            c "{cps=16}Aquí tienes{/cps}"
            $ dinero -= 6.5
            $ dinero_gastado += 6.5
            hide bg_carniceria 
            show black with dissolve
            play sound "audio/meat.mp3"
            pause 1
            show bg_carniceria
            c "{cps=16}Todo listo{/cps}"
            hide bg_carniceria with dissolve
            
            return
        "Filetes de pavo: 11$/kg":
            c "{cps=16}Aquí tienes{/cps}"
            $ dinero -= 11
            $ dinero_gastado += 11
            hide bg_carniceria
            show black with dissolve
            play sound "audio/meat.mp3"
            pause 1
            show bg_carniceria 
            c "{cps=16}Todo listo{/cps}"
            hide bg_carniceria with dissolve
            
            return
    stop music fadeout 0.5
    return



label verduras:
    show bg_verduras with dissolve
    "{cps=16}Esta bien comer verduras.{/cps}"
    "{cps=16}Y cocinar con ellas le da mucho sabor a los platos{/cps}"
    menu:
        "{cps=16}Que vas a comprar?{/cps}"
        "Tomate: 2$/kg":
            "{cps=16}Sobrará con pillar un kilo{/cps}"
            $ dinero -= 2
            $ dinero_gastado += 2
            hide bg_verduras with fade
            return
        "Lechuga: 1.50$/kg":
            "{cps=16}Sobrará con pillar una{/cps}"
            $ dinero -= 1.5
            $ dinero_gastado += 1.5
            hide bg_verduras with fade
            return
        "Zanahoria: 1$/kg":
            "{cps=16}Sobrará con pillar un kilo{/cps}"
            $ dinero -= 1
            $ dinero_gastado += 1
            hide bg_verduras with fade
            return
        "Cebolla: 1.50$/kg":
            "{cps=16}Sobrará con pillar un kilo{/cps}"
            $ dinero -= 1.5
            $ dinero_gastado += 1.5
            hide bg_verduras with fade
            return
        "Patata: 3$/kg":
            "{cps=16}Sobrará con pillar un kilo{/cps}"
            $ dinero -= 3
            $ dinero_gastado += 3
            hide bg_verduras with fade
            return
        
label macarrones:
    show bg_pasta 
    menu:
        "{cps=16}Haber que opciones hay por aquí{/cps}"
        "Macarrones: 0.80$ el paquete":
            "{cps=16}Con un paquete va bien{/cps}"
            $ dinero -= 0.8
            $ dinero_gastado += 0.8
            return
        "Espaguetis: 0.95$ el paquete":
            "{cps=16}Con un paquete va bien{/cps}"
            $ dinero -= 0.95
            $ dinero_gastado += 0.95
            return
        "Ñoquis: 1.20$ el paquete":
            "{cps=16}Con un paquete va bien{/cps}"  
            $ dinero -= 1.2
            $ dinero_gastado += 1.2
            return
        "Raviolis: 1.50$ el paquete":
            "{cps=16}Con un paquete va bien{/cps}"
            $ dinero -= 1.5
            $ dinero_gastado += 1.5
            return


label comida_instantanea:
    show bg_sopa_instantanea with dissolve
    "{cps=16}No creo que tenga mucha complicacion escoger que sopa pillar, todas valen lo mismo{/cps}"
    "{cps=16}Y todas son de la misma marca, así que no hay mucho donde elegir{/cps}"
    menu:
        "Quieres pillar una de cada?"
        "Sí":
            "{cps=16}Perfecto, así no te faltará de nada{/cps}"
            $ dinero -= 3
            $ dinero_gastado += 3
            hide bg_sopa_instantanea with fade
            return
        "No":
            "{cps=16}Vale, entonces que sopa quieres?{/cps}"
            menu:
                "Sopa de Pollo: 0.6$":
                    "{cps=16}Suficiente{/cps}"
                    $ dinero -= 0.6
                    $ dinero_gastado += 0.6
                    hide bg_sopa_instantanea with fade
                    return
                "Sopa de Verduras: 0.6$":
                    "{cps=16}Suficiente{/cps}"
                    $ dinero -= 0.6
                    $ dinero_gastado += 0.6
                    hide bg_sopa_instantanea with fade
                    return
                "Sopa de Marisco: 0.6$":
                    "{cps=16}Suficiente{/cps}"
                    $ dinero -= 0.6
                    $ dinero_gastado += 0.6
                    hide bg_sopa_instantanea with fade
                    return
                "Sopa de Fideos: 0.6$":
                    "{cps=16}Suficiente{/cps}"
                    $ dinero -= 0.6
                    $ dinero_gastado += 0.6
                    hide bg_sopa_instantanea with fade
                    return
                "Sopa de Cebolla: 0.6$":
                    "{cps=16}Suficiente{/cps}"
                    $ dinero -= 0.6
                    $ dinero_gastado += 0.6
                    hide bg_sopa_instantanea with fade
                    return               

label capricho:
    show bg_capricho with dissolve
    "{cps=16}Bueno, un capricho de vez en cuando no hace daño{/cps}"
    "{cps=16}El dilema es...{/cps}"
    menu:
        "{cps=16}Que pillar?{/cps}"
        "Chocolate: 1.50$":
            "{cps=16}Buen postre o acompañamiento{/cps}"
            $ dinero -= 1.5
            $ dinero_gastado += 1.5
            hide bg_capricho with fade
            return
        "Gominolas: 1.20$":
            "{cps=16}Es una pena que despues no duren nada{/cps}"
            $ dinero -= 1.2
            $ dinero_gastado += 1.2
            hide bg_capricho with fade
            return
        "Galletas: 1.00$":
            "{cps=16}Perfecto para acompañar el desayuno{/cps}"
            $ dinero -= 1
            $ dinero_gastado += 1
            hide bg_capricho with fade
            return
    return
transform bump:
    linear 0.04 xoffset -20 yoffset 0
    linear 0.04 xoffset 20 yoffset 0
    linear 0.04 xoffset -10 yoffset 0
    linear 0.04 xoffset 0 yoffset 0
label pagar_compra:
    show bg_pagar with dissolve
    stop music fadeout 1.0
    play music "audio/butcher.mp3" loop volume 0.1 fadein 1.0
    "{cps=16}Las cajas estan llenas de gente comprando cantidades inmensas de comida, pero logras meterte en la fila donde menos gente había{/cps}"
    "{cps=16}Aún así, parece que va a tardar un rato{/cps}"
    pause 1.0
    hide bg_pagar 
    show bg_pagar at bump
    stop music fadeout 0.5
    play sound "audio/coughing.mp3"
    "{cps=12}Vaya...{/cps}{cps=15} parece que alguien esta costipado{/cps}"
    "{cps=15}Y no tiene otro lugar para estornudar que justamente en tu espalda{/cps}"
    "{cps=15}Pero bueno, ya va tocandote, así que coloca toda la compra en la cinta{/cps}"
    pause 0.5
    play sound "audio/receipt.mp3"
    pause 2.0
    "{cps=16}Con todo ya pagado, es momento de irse a casa{/cps}"
    hide bg_pagar 
    show black with dissolve
    stop music fadeout 1.0
    pause 4
    $ renpy.notify("Explora la casa y haz cosas hasta la hora de comer(13:00 - 14:00)")
    play music "audio/ambientedia.mp3" loop volume 0.2 fadein 2.0
    hide black with dissolve
    hide screen compra
    $ room = "hall2"
    jump main_loop
    


    



default door_actions = ["Mirar", "Salir", "Contestar"]
default phone_avaliable = True
screen Mr_Game_and_Watch():
    if room == "mainroom":
        add "mainroom.png"

        imagebutton:
            idle "interactive.png"
            hover "interactive.png"
            xpos 1150
            ypos 500
            action Call("dlg_bed")
        imagebutton:
            idle "interactive.png"
            hover "interactive.png"
            xpos 400
            ypos 710
            action Call("dlg_wordsearch")
        textbutton "Pasillo":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "pasillo")
    elif room == "pasillo":
        add "hall.png"
        textbutton "Salón":
            text_style "txtRoom"
            xpos 1050
            ypos 1000
            action SetVariable("room", "livingroom")
        textbutton "Habitacion":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "mainroom")
        textbutton "Cocina":
            text_style "txtRoom"
            xpos 750
            ypos 510
            action SetVariable("room", "kitchen")
        textbutton "Puerta":
            text_style "txtRoom"
            xpos 960
            ypos 450
            action SetVariable("room", "door")
    elif room == "kitchen":
        add "kitchen.png"
        textbutton "Comer algo":
            text_style "txtActions"
            xpos 960
            ypos 650
            action Call("dlg_eat")
        textbutton "Atrás":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "pasillo")
    elif room == "livingroom":
        add "livingroom.png"
        imagebutton:
            idle "interactive.png"
            hover "interactive.png"
            xpos 300
            ypos 580
            action Call("dlg_window")
        imagebutton:
            idle "interactive.png"
            hover "interactive.png"
            xpos 850
            ypos 500
            action Call("dlg_sofa")
            
        textbutton "Atrás":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "pasillo")
    elif room == "hall2":
        add "hall2.png"
        textbutton "Puerta":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "door")
        textbutton "Cocina":
            text_style "txtRoom"
            xpos 1600
            ypos 250
            action SetVariable("room", "kitchen")
        textbutton "Salón":
            text_style "txtRoom"
            xpos 900
            ypos 100
            action SetVariable("room", "livingroom")
        textbutton "Habitación de Invitados":
            text_style "txtRoom"
            xpos 1000
            ypos 1000
            action SetVariable("room", "guestroom")
    elif room == "door":
        add "door.png"
        textbutton "Atrás":
            text_style "txtRoom"
            xpos 1000
            ypos 1000
            action SetVariable("room", "hall2")
        textbutton "[door_actions[doorEvent]]":
            text_style "txtRoom"
            xpos 1000
            ypos 250
            action Call("lookoutside")
    elif room == "guestroom":
        add "guestroom.jpeg"
        textbutton "Atrás":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "hall2")

#renpy.say hace de dialogo abriendo una nueva interacción, que pasa, screen se cuenta como otra interacción y se interceptan
 



















label start:
    scene black
    "Buenos días, tardes o noche"
    "Antes de introducirte en el juego y contarte tu historia me gustaria avisarte de unas pequeñas cosillas"
    "Este juego presenta contenido maduro, explícito e incluso gráfico, por lo cual debe de jugarse bajo estas condiciones"
    "Sí eres sensible a alguno de estos temas, por favor, te ruego encarecidamente que no juegues, y si aún así te atreves, permíteme darte un consejo"
    "Ningún contenido explícito y gráfico es obligatorio, sino que opcional"
    menu:
        "Desearias recivir un aviso de que opciones pueden conllevar a este tipo de contenido?"
        "Sí":
            narrator "Perfecto"
            pass
        "No":
            narrator "Sin problema"
            pass
    "En cualquier caso, el juego esta lleno de muchas otras cosas de la que podrás disfrutar"
    pause 2
    #antes de el nombre y pronombre los avisos del contenido de este juego
    play music "audio/ambientedia.mp3" loop
    narrator "Antes de comenzar,desearía dirigirme a ti de alguna forma, así que dime"
    $ player_name = renpy.input("¿Cómo te llamas?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Bolonga"
    menu:
        "Una última cosa, para referirme a ti prefieres?"

        "El":
            $ genero = "hombre"
            $ pronombre = "él"
            $ articulo = "o"

        "Ella":
            $ genero = "mujer"
            $ pronombre = "ella"
            $ articulo = "a"


   
    #INTRODUCCIÓN - CONTEXTO
    narrator "{cps=9}La soledad{/cps}"
    narrator "Algo nuevo para ti en esta nueva etapa de tu vida"
    narrator "{cps=5}. . .{/cps}"
    narrator "{cps=16}Han pasado 2 semanas desde que tu abuelo falleció, dejando tras él un arduo y complejo testamento donde toda su herencia se repartiría con la familia.{/cps}"
    narrator "{cps=16}Hubieron guerras, gritos y amenazas, pero una vez las cosas se calmaron a ti te toco uno de los viejos apartamentos de tu abuelo, realmente nunca te metiste en el tema, y aún así, conseguiste un trozo del pastel{/cps}"
    narrator "{cps=16}Cualquiera diría que te ha tocado la lotería, alguien como tú, con estudios pero desempleado, buscando trabajo, consiguiendo una casa de la noche a la mañana, ¿Quién lo imaginaba?{/cps}"
    narrator "{cps=16}Y con tus padres desesperados por echarte de casa esta era la excusa perfecta.{/cps}"
    narrator "{cps=16}Pero que te puedo decir, aunque haya costado un poco has conseguido mudarte a un rincón de la ciudad, un antiguo barrio de trabajadores.{/cps}"
    menu:
        "¿Llevas bien la soledad?"
        "Sí":
            narrator "{cps=16}Supongo que es lo normal con el paso del tiempo{/cps}" 
        "No":
            narrator "{cps=16}No te preocupes, en algún momento te acostumbrarás.{/cps}" 
    pause 0.5
    play sound "audio/alarm-clock.mp3" fadein(0.5)
    narrator "{cps=16}Abres tus ojos lentamente, agotad[articulo],  intentando alcanzar tu móvil que no paraba de vibrar y sonar{/cps}"
    pause 1
    show bg weikiweiki 
    #narrator "{cps=16}{/cps}" 
    narrator "{cps=16}Son las 9:00, y por alguna razón te has puesto una alarma a esa hora, intentando crear un buen habito en tu nueva vida de independiente.{/cps}"
    narrator "{cps=4}Supongo{/cps}"
    pause 1
    play sound "wake_up.mp3"
    narrator "{cps=16}Siendo tan pronto tienes todo el tiempo para hacer lo que quieras… Pero lo mejor será desayunar para empezar el día{/cps}"
    hide bg weikiweiki
    window hide
    pause 1.0
    $ renpy.notify("Acabas de coger el móvil")
    show screen digital_clock
    call screen Mr_Game_and_Watch
    jump main_loop

label asking_game:
    
    menu:
        "Quieres seguir jugando?"
        "Sí":
            return True
        "No":
            return False



#Let the game be
label main_loop:
    
    if phone_open == False:
        call screen Mr_Game_and_Watch
    else:
        call screen phone
    jump main_loop

    

# #labels y python para lógica
# #screens para la interfaz

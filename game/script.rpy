# Coloca el código de tu juego en este archivo.
# Declara los personajes usados en el juego como en el ejemplo:
define p = Character(("[player_name]"), color="#cdcdcd")
define plNews = Character(("Presentador de noticias"), color="#9ba5d8")
define plAdd = Character (("Anunciador Entusiastico"), color="#f1f1d3")
define plAdd2 = Character (("Anunciador Tranquilo"), color="#d4f1d3")
#variable que determina que hora va a ser
#image bg_bathroom = "bathroom.png"
#screen funciona como una funcion para crear un "escenario", esto puede servir más adelante para la crear la dinámica de libertad de exploración
image eat = "bg eater.jpeg"
image mainroom = "mainroom.png"
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
    size 20
    color "#273529"
    line_spacing 2
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
    color "#e0e8e1"
    font "Pixel Digivolve.otf"




#Minijuegos 
#Sopa de Letras
default inicio = None
default seleccion = []
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
label winSopaLetras:
    hide screen sopa_letras
    "Has completado la Sopa de Letras de hoy"
    "Sientes que has invertido más tiempo de lo que deberías en este juego"
    menu:
        "Deseas jugar otra vez?"

        "Sí":
            $ palabras_encontradas = []
            $ palabras_noencontradas = ["AVENIDA","ENTRADA","HIELO","MOMENTO","PIERNA","PINGO","PROTESTA","RECUERDO","CAYO"]
            

        "No":
            hide screen sopa_letras
#Minigames upcoming


#que en vez de dividirse en partes el avance del día, cada actividad te consuma tiempo
#Ver la tele
#Escribir
#Leer









#Prueba de diálogo en init python
#Actualizar todo lo relacionado con el tiempo
default hour = 9
default eathour = "Desayunar"
default day_moment = "Intro"
default phone_disponible = False



screen digital_clock():

    zorder 100
    frame:
        # Cambia el estado del día dependiendo de la hora
        xalign 0.95  
        yalign 0.05
        padding (15, 10)
        # El texto que se mostrará en pantalla
        text "[hour:02d]:00" size 32  color "#3a0c0c"


label dlg_bed:
    if 9 <= hour <= 13:
        show mainroom
        "Aquí yace tu cómoda cama, de la cual te acabas de levantar."
        "{cps=4}. . . {/cps}"
        "No creo que quieras seguir durmiendo"
        call screen Mr_Game_and_Watch

    elif 14 <= hour <= 19:
        "Vas a echarte una siesta de verdad? Y no prefieres disfrutar del tiempo libre que tienes?"
    return
    hide mainroom

label dlg_wordsearch:
    show mainroom
    "Es la antigua revista de Sopa de Letras de tu abuelo. Parece estar solo en Español"
    if hour == 9:
        "Despues de desayunar podrías hacer una o dos"
        return

    elif hour < 21:
        "Quieres resolver una sopa de letras?"
        menu:
            "Sí":
                show screen sopa_letras
                return
            "No":
                "Mejor para más tarde"
                return
    return
    hide mainroom

label dlg_eat:
    show kitchen
    if hour == 9:
        $ hour += 1
        play sound "audio/kitchen.mp3"
        pause 2.5
        stop sound
        "{cps=16}Será mejor desayunar en el salón{/cps}"
        pause 2.0
        "{cps=16}Mirándolo bien, no queda casi nada de comida, tendrás que hacer la compra esta tarde{/cps}"
        hide window
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
        "{cps=16}Espero que este bueno el desayuno, mientras tanto, por que no vemos las noticias?{/cps}"
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
    plNews "{cps=16}Y ahora, un mensaje de nuestros patrocinadores{/cps}"
    stop music fadeout 0.5
    play music "audio/addmusic.mp3" volume 0.17 
    plAdd "{cps=20}¿Te sientes solo? ¿Estas buscando compañía y necesitas dinero?{/cps}"
    plAdd "{cps=20}¡Pues ahora puedes alquilar tu habitación semanalmente con la mejor compañía del mercado!{/cps}"
    p "{cps=5}Mmmmmm...{/cps}{cps=16}No suena mal del todo{/cps}"
    plAdd "{cps=18}Hacemos el presupuesto y te ayudamos a venderla rápido y seguro. ¡En menos de una semana!{/cps}"
    plAdd "{cps=16}Llama hoy al 661 y nosotros nos encargamos del resto!{/cps}"
    $ renpy.notify("Nuevo número registrado: 661")
    #$ contacts.append("661")
    pause 0.5
    stop music fadeout 0.5
    play music "audio/addmusic2.mp3" volume 0.17 fadein 0.5
    plAdd2 "{cps=16}Esta semana la comida viene a tu casa con descuento{/cps}"
    #para añadir el signo de porcentaje en un string se debe poner doble porcentaje, ya que el primero es para escapar el segundo
    plAdd2 "{cps=15}Consigue hasta un 50%% en tu próximo pedido a domicilio. {/cps}"
    plAdd2 "{cps=18}Llama ya al 627 y pide lo que quieras.{/cps}"
    $ renpy.notify("Nuevo número registrado: 627")
    #$ contacts.append("627")
    play sound "audio/comer.mp3" loop
    pause 5.0
    stop sound fadeout 0.5
    narrator "{cps=16}Bueno, suficientes noticias por hoy, creo que es hora de ir a hacer la compra, aprovecha la mañana{/cps}"
    play music "audio/ambientedia.mp3" loop fadein 0.5
    $ room = "livingroom"
    hide eat
    return

label lookoutside():
    show bg outside
    "No parece haber mucho movimiento ahí fuera"
    hide bg outside
    return
    
       






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
        textbutton "Habitacion":
            text_style "txtRoom"
            xpos 1050
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
                xpos 400
                ypos 710
        imagebutton:
            idle "interactive.png"
            hover "interactive.png"
            xpos 850
            ypos 500
        textbutton "Atrás":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "pasillo")
    elif room == "hall2":
        add "hall2.png"
    elif room == "door":
        add "door.png"
        textbutton "Atrás":
            text_style "txtRoom"
            xpos 1000
            ypos 1000
            action SetVariable("room", "pasillo")
        textbutton "Mirar":
            text_style "txtRoom"
            xpos 1000
            ypos 250
            action Call("lookoutside")


#renpy.say hace de dialogo abriendo una nueva interacción, que pasa, screen se cuenta como otra interacción y se interceptan
 




















label start:
    #antes de el nombre y pronombre los avisos del contenido de este juego
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


    play music "audio/ambientedia.mp3" loop
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
    narrator "{cps=16}Abres tus ojos lentamente, agotad[articulo],  intentando alcanzar tu móvil que no paraba de vibrar y emitir esa irritante música.{/cps}"
    pause 1
    show bg weikiweiki
    #narrator "{cps=16}{/cps}" 
    narrator "{cps=16}Son las 9:00, y por alguna razón te has puesto una alarma a esa hora, intentando crear un buen habito en tu nueva vida independiente.{/cps}"
    narrator "{cps=4}Supongo{/cps}"
    pause 1
    play sound "wake_up.mp3"
    narrator "{cps=16}Siendo tan pronto tienes todo el tiempo para hacer lo que quieras… Pero lo mejor será desayunar para empezar el día{/cps}"
    hide bg weikiweiki
    call screen Mr_Game_and_Watch
    jump main_loop



#Let the game be
label main_loop:
    call screen Mr_Game_and_Watch
    jump main_loop

    

# #labels y python para lógica
# #screens para la interfaz

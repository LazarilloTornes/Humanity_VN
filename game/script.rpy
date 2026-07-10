
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

image found_coin = Movie(
    play="text.webm",
    size=(1920,1080)
    )
image closet = im.Scale("bg closet.jpg", config.screen_width, config.screen_height)
default player_name = "Bolonga"
#Dinero y comida
default dinero = 50
default food = 0

#la comida suele durar 3 días, teniendo un máximo de 3
#En la intro empieza en 0, sin embargo se obligará a la persona a hacer la compra
#En la aplicación donde se mira eso aparecerá:
#Tienes comida para: ["food"] días.
#variable que controla el paso de los días, el día 0 es básicamente la intro
default day = 0
default room = "mainroom"

default rndItem = ["Moneda", "Consola", "Juegos", "Cartas antiguas", "Bakugan1","Bakugan2", "Bakugan3", "Gafas", "Libro1", "Libro2", "Libro3", "Libro4"]
#Closet thingy
#AND REMEMBER SON
# IF THE VIDEO DOESN'T WORK USE THE MAGIC WORDS
#ffmpeg -i coin.webm -c:v libvpx-vp9 -pix_fmt yuv420p -c:a libopus coin_fixed.webm 
label search_closet:
    hide screen Mr_Game_and_Watch
    show found_coin zorder 100
    show closet
    pause 4
    hide found_coin
    hide closet
    jump main_loop
    

 
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

#All interactions, don't get lost buddy
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
        hide kitchen
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
                $ hour += 1
                hide bg_ventana
                return
                
            "No":
                "{cps=3}. . .{/cps}"
                "{cps=15}Mejor en otro momento{/cps}"
                hide bg_ventana
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
        imagebutton:
            idle "right.png"
            hover "right_p.png"
            xpos 1650
            ypos 970
            action SetVariable("room", "closet")
    elif room == "closet":
        add im.Scale("bg closet.jpg", config.screen_width, config.screen_height)
        textbutton "Habitacion":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "mainroom")
        imagebutton:
            idle "interactive.png"
            hover "interactive.png"
            xpos 830
            ypos 534
            action Call("search_closet")  
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
        textbutton "...":
            text_style "txtRoom"
            xpos 1210
            ypos 520
            action SetVariable("room","guestroom")
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
            ypos 350
            action SetVariable("room", "kitchen")
        textbutton "Salón":
            text_style "txtRoom"
            xpos 900
            ypos 200
            action SetVariable("room", "livingroom")
        textbutton "Habitación de Invitados":
            text_style "txtRoom"
            xpos 300
            ypos 850
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
        add im.Scale("guestroom.jpeg", config.screen_width, config.screen_height)
        textbutton "Atrás":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "hall2")

#renpy.say hace de dialogo abriendo una nueva interacción, que pasa, screen se cuenta como otra interacción y se interceptan
 



















label start:

    pause 4
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
    if hour == 13:
        $ renpy.notify("Ya es hora de comer")    
    if phone_open == False:
        call screen Mr_Game_and_Watch
    else:
        call screen phone
    jump main_loop

    

# #labels y python para lógica
# #screens para la interfaz

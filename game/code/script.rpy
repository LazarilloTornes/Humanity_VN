
#variable que determina que hora va a ser
#image bg_bathroom = "bathroom.png"
#screen funciona como una funcion para crear un "escenario", esto puede servir más adelante para la crear la dinámica de libertad de exploración
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

default items = ["Moneda", "Consola Antigua", "Juegos", "Cartas antiguas", "Bakugan Rojo","Bakugan Azul", "Bakugan Celeste", "Gafas Negras", "Obras de Espronceda", "Lazarillo de Tormes", "Rimas y Leyendas", "Don Juan Tenorio"]
default item_founded = ""
default inventory = []
init python:
    import random
    def rnd_item_generator():
        global item_founded, items
        if not items:
            item_founded = ""
            return None
        item_founded = random.choice(items)
        items.remove(item_founded)
        inventory.append(item_founded)


#Closet thingy
#AND REMEMBER SON
# IF THE VIDEO DOESN'T WORK USE THE MAGIC WORDS
#ffmpeg -i coin.webm -c:v libvpx-vp9 -pix_fmt yuv420p -c:a libopus coin_fixed.webm 
label search_closet:
   
    if hour == 8 or hour == 13 or hour == 20:
        show closet
        "{cps=15}Creo que es un mejor momento para comer que para buscar entre los trastos.{/cps}"
        hide closet
        return
    else:
        if clst_attempts == 1:
            hide screen Mr_Game_and_Watch
            show closet
            "{cps=15}Estos armarios siguen llenos de todas las cosas dejadas atrás por tu abuelo{/cps}"
            "{cps=15}Nadie se ha dignado a vaciar nada{/cps}"
            "{cps=15}Podrías rebuscar entre las cosas{/cps}"
            "{cps=15}Quizás encuentres algo interesante{/cps}"
            hide closet with fade
            show black with dissolve
            play sound "audio/search_closet.mp3" fadein 0.5
            pause 5
            stop sound
            show closet #Aquí iría el video
            $ rnd_item_generator()
            $ renpy.notify("Has encontrado {}".format(item_founded))
            $ clst_attempts = 0
            $ hour += 1
            "{cps=15}Alfinal buscar entre tantas cosas te ha llevado bastante tiempo{/cps}"
            hide closet
            jump main_loop
        else:
            show closet
            "{cps=15}Ya has rebuscado lo suficiente por hoy, quizás otro día sigues{/cps}"
            hide closet
            jump main_loop
    

 
#Actualizar todo lo relacionado con el tiempo
default hour = 8
default phone_disponible = False
default clst_attempts = 1
screen digital_clock:
    zorder 100
    draggroup:
        drag:
            drag_name "popup"
            draggable True
            xpos 1700
            ypos 50
            xsize 100
            ysize 100
            fixed:
                textbutton "[hour:02d]:00":
                    text_style "txtClock"
                    background "#cddbc8"
                    action NullAction()
    if room == "closet":
        textbutton "Intentos: [clst_attempts]":
            text_style "txtContacts"
            xalign 0.85  
            yalign 0.05
            padding (15, 10)
            background "#e6f4e1"
            action NullAction()
    else:
        imagebutton:
            idle "buttons/btn_phone.png"
            hover "buttons/btn_phone.png"
            xalign 0.85  
            yalign 0.05
            action SetVariable("phone_open", True), Show("phone")

#All interactions, don't get lost buddy
label dlg_bed:
    if 8 == hour:
        show mainroom
        "Aquí yace tu cómoda cama, de la cual te acabas de levantar."
        "{cps=4}. . . {/cps}"
        "No creo que quieras seguir durmiendo"
        hide mainroom
        call screen Mr_Game_and_Watch
    elif hour != 8 and hour < 13:
        show mainroom
        "{cps=14}Ciertamente tienes una cama bastante cómoda.{/cps}"
        if doorEvent == 1:
            "{cps=14}Pero antes de dormir más tienes que hacer la compra.{/cps}"
            "{cps=14}Se que puede dar pereza.{/cps}"
            "{cps=14}Es lo que hay.{/cps}"
            hide mainroom
            return
        else:
            "{cps=10}Quieres dormir hasta la hora de comer?{/cps}"
            menu:
                "Sí, no tengo nada mejor que hacer":
                    hide mainroom
                    show black
                    pause 2.0
                    #Agregar sonido de ronquido
                    $ hour = 13
                    return
                "No, prefiero hacer otra cosa":
                    return
    elif 14 <= hour <= 19:
        "Vas a echarte una siesta de verdad? Y no prefieres disfrutar del tiempo libre que tienes?"
    return
    

label dlg_wordsearch:
    show mainroom
    "Es la antigua revista de Sopa de Letras de tu abuelo. Parece estar solo en Español"
    if hour == 8:
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
    if hour == 8:
        play sound "audio/kitchen.mp3"
        pause 2.5
        stop sound
        "{cps=16}Será mejor desayunar en el salón{/cps}"
        pause 2.0
        "{cps=16}Mirándolo bien, no queda casi nada de comida, tendrás que hacer la compra{/cps}"
        window hide
        hide kitchen
        show hall_bh
        pause 1
        hide hall_bh
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
    elif 8 < hour < 13:
        "{cps=16}Ya has desayunado...{/cps}"
        "{cps=16}Para que quieres desayunar otra vez{/cps}"
    elif hour == 13:
        "{cps=16}Es momento de comer algo...{/cps}"
        play sound "audio/kitcken.mp3"
        show black with dissolve
        pause 3.0
        stop sound
        show kitchen
        menu:
            "Donde prefieres comer?"
            "Salón":
                jump lb_livingroom_eat
            "Aquí mismo":
                jump lb_kitchen_eat
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

label lb_livingroom_eat:
    hide kitchen
    show hall_bh with dissolve
    pause 1.0
    hide hall_bh
    show eat
    narrator "{cps=15}Que aproveche{/cps}"
    play sound "audio/comer.mp3" loop
    call news
label lb_kitchen_eat:
    stop music
    hide kitchen
    "{cps=16}Pues aquí mismo entonces{/cps}"
    show black with dissolve
    show kitchen with dissolve
    play sound "audio/comer.mp3" loop
    "{cps=16}Espero que esté rica la comida{/cps}"
    pause 3
    if alquilar == False:
        "{cps=16}Sabes?{w=0.5} podrías llamar a esa compañía que alquila habitaciones{/cps}"
        "{cps=14}Así podrías darle un buen uso a esa habitación que tienes vacía{/cps}"
        "{cps=14}Y conseguir un poco de dinero{/cps}"
    else:
        "{cps=14}mmmmmmmmmm{/cps}"
        "{cps=14}Qué podrías hacer esta tarde?{/cps}"
    pause
    stop sound
    show black with dissolve
    $ hour += 1
    "Bueno, pues ya estaría"
    pause 0.5
    play music "audio/ambientenoon.mp3" loop
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
    if hour == 8:
        "Será mejor desayunar primero"
        hide bg_ventana
        return
    elif hour == 13:
        "Ya es la hora de comer, mejor pensar en otro momento"
        return
    elif hour == 20:
        "Es hora de cenar... ve a la cocina y pilla algo"
        return
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


label lb_lvb:
    show bath 
    pause 0.5
    hide bath
    show labamanos with dissolve
    "Quieres labarte las manos?"
    menu:
        "Sí":
            show black
            play sound "audio/tap_water.mp3"
            pause 3
            show labamanos
            stop sound
            "{cps=14}Sientes tu manos bastante más...limpias{/cps}"
            "{cps=16}No se que te esperabas{/cps}"
            hide labamanos
            jump main_loop
            return
        "Ahora no hace falta":
            hide labamanos
            jump main_loop
            return
            
label lb_tlt:
    show bath 
    "{cps=15}...{/cps}"
    "{cps=15}Supongo que necesitas hacer tus necesidades{/cps}"
    menu:
        "Sí":
            show black
            pause 5
            play sound "audio/flush.mp3"
            pause
            stop sound
            "{cps=14}Te sientes más... vacío?{/cps}"
            "Mejor"
            hide bath
            jump main_loop
            return
        "No":
            hide bath
            jump main_loop
            return

label lb_dch:
    show bath
    if hour == 8:
        "{cps=14}No hay nada mejor que una ducha para empezar el día{/cps}"
        menu:
            "Ducharse":
                show black
                play sound "audio/shower.mp3" loop
                pause
                stop sound
                hide bath
                jump main_loop
                return
            "No":
                hide bath
                jump main_loop
                return
    else:
    
        menu:
            "Ducharse":
                show black
                play sound "audio/shower.mp3" loop
                pause
                stop sound
                hide bath
                jump main_loop
                return
            "No":
                hide bath
                jump main_loop
                return

#renpy.say hace de dialogo abriendo una nueva interacción, que pasa, screen se cuenta como otra interacción y se interceptan
 



















label start:
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
    # narrator "{cps=5}Yaa...{/cps}{cps=9} seguro...{/cps}..... [player_name]."
    # narrator "{cps=16}Ahora permíteme ponerte un poco en contexto [player_name].{/cps}"
    # narrator "{cps=16}Conseguiste independizarte,¡Enhorabuena! aunque gracias a la herencia de un familiar, quien muy amablemente te cedió uno de sus apartamentos.{/cps}"
    # narrator "{cps=16}Puedes considerarte un suertudo y, sin embargo, estás viviendo por tu cuenta, sin nadie más.{/cps}"
    # narrator "{cps=16}Te diría que es un gran logro, pero aún estás buscando trabajo, tus padres te pasan una pensión para que puedas vivir y... poco más, tus últimos días se han resumido en: comer, buscar trabajos y dormir{/cps}"
    # narrator "{cps=16}¿Cuánto llevas repitiendo esta misera vida? {w=1} Tampoco te lo quiero recordar…{/cps}"
    # narrator "{cps=19}Al final, despues de todo vives en una casa con 2 habitaciones, un salón y una cocina para ti, 2 baños que raramente alternas, y aun así te aíslas.{/cps}"
    # narrator "{cps=15}No sabes nada del exterior que no sean las noticias y ese dichoso cielo rojizo que tanto daño te hace a la vista. Te asomas para ver si hay alguien, pero está completamente vacío.{/cps}"
    # narrator "{cps=16}Es como si fueras el último humano en el planeta…{/cps}"
    # narrator "{cps=16}Colgaste hace poco un cartel por tus calles para alquilar una de las habitaciones, lo dejaste a un precio accesible ya que realmente te vendría bien un dinero extra. Pero nadie viene…{/cps}"
    
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
    show wup
    #narrator "{cps=16}{/cps}" 
    narrator "{cps=16}Son las 9:00, y por alguna razón te has puesto una alarma a esa hora, intentando crear un buen habito en tu nueva vida de independiente.{/cps}"
    narrator "{cps=4}Supongo{/cps}"
    pause 1
    play sound "wake_up.mp3"
    narrator "{cps=16}Siendo tan pronto tienes todo el tiempo para hacer lo que quieras… Pero lo mejor será desayunar para empezar el día{/cps}"
    hide wup
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
    elif hour == 9:  
        $ renpy.notify("Hora de desayunar")  
    elif hour == 20:  
        $ renpy.notify("Hora de cenar")  
    if phone_open == False:
        call screen Mr_Game_and_Watch
    else:
        call screen phone
    jump main_loop
 

# #labels y python para lógica
# #screens para la interfaz

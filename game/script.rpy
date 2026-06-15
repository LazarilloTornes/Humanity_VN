# Coloca el código de tu juego en este archivo.
# Declara los personajes usados en el juego como en el ejemplo:
define p = Character("[player_name]")
#variable que determina que hora va a ser
#screen funciona como una funcion para crear un "escenario", esto puede servir más adelante para la crear la dinámica de libertad de exploración
style txtRoom:
    color "#ffffff"
#Actualizar todo lo relacionado con el tiempo
default hour = 1
default passingHours = "Desayunar"
init python:

    def update_time():

        global passingHours, hour

        if hour == 1:
            passingHours = "Desayunar"
            hour += 1

        elif hour == 2:
            passingHours = "Comer"
            hour += 1

        elif hour == 3:
            passingHours = "Cenar"
            hour = 1


screen habitacion():
        #solo como recordatorio, screen trabaja añadiendo los pngs directamente, el bg solo sirve en labels y demás
        add "bg mainroom.png"
        imagebutton:
            idle "interactive.png"
            hover "interactive.png"
            xpos 1150
            ypos 500
            action Call("Bed")
        imagebutton:
            idle "interactive.png"
            hover "interactive.png"
            xpos 400
            ypos 710
            action Call("SopadeLetras")
        textbutton "Pasillo":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action Show("pasillo")
#renpy.say hace de dialogo abriendo una nueva interacción, que pasa, screen se cuenta como otra interacción y se interceptan


screen pasillo():
    add "bg hall.png"
    textbutton "Habitacion":
        text_style "txtRoom"
        xpos 850
        ypos 1000
        action [Hide("pasillo"), Show("habitacion")]
    textbutton "Cocina":
        text_style "txtRoom"
        xpos 750
        ypos 510
        action [Hide("pasillo"), Show("cocina")]
    textbutton "Puerta":
        text_style "txtRoom"
        xpos 960
        ypos 450
        action [Hide("pasillo"), Show("puerta")]


screen cocina():
    add "bg kitchen.png"
    textbutton "[passingHours]":
        text_style "txtRoom"
        xpos 960
        ypos 450
        action Call("eat")
            
        

screen puerta():
    add "bg door.png"
    

#todas las interacciones
label Bed:
    show bg mainroom
    if hour == 1:
        narrator "Aquí yace tu cómoda cama, de la cual te acabas de levantar."
        narrator "{cps=4}. . . {/cps}"
        narrator "no creo que quieras seguir durmiendo"
    elif hour == 2:
        narrator "Vas a echarte una siesta de verdad"
    call screen habitacion
return
label eat:

    if passingHours == "Desayunar":
        narrator "Ya era hora, pero será mejor desayunar en el salón"
        show bg hall2 #hall2 es la pespectiva de la cocina y la puerta
        pause 0.5
        show bg livingroom
        pause 0.5

    elif passingHours == "Comer":
        p "Por fin"
        p "Me muero de hambre"

    elif passingHours == "Cenar":
        "Es hora de cenar."

    return

label SopadeLetras:
    show bg mainroom
    narrator "Es una revista de Sopa de Letras."
    narrator "Curiosamente abierta por la página 27"
    call screen habitacion
return


   
# El juego comienza aquí.
label start:
    scene black
    narrator "Antes de comenzar,desearía dirigirme a ti de alguna forma, así que dime"
    $ player_name = renpy.input("¿Cómo te llamas?")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Bolonga"
    #INTRODUCCIÓN - CONTEXTO
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
    narrator "{cps=16}Abres tus ojos lentamente, agotad[articulo],  intentando alcanzar a tu móvil que no paraba de vibrar y emitir esa irritante música.{/cps}"
    pause 1
    show bg weikiweiki
    #narrator "{cps=16}{/cps}" 
   
    narrator "{cps=16}Son las 9:00, y por alguna razón te has puesto una alarma a esa hora, intentando crear un buen habito en tu nueva vida independiente.{/cps}"
    narrator "{cps=4}Supongo{/cps}"
    scene black
    pause 1
    play sound "wake_up.mp3"
    narrator "{cps=16}Siendo tan pronto tienes todo el tiempo para hacer lo que quieras… Pero lo mejor será desayunar para empezar el día{/cps}" 
    #call para usar el screen, básico
    call screen habitacion


   

#Have in mind you have to design at least 21 news for the whole game
label news:
    if hour == 9: #and day == x:
        show eat
        #all the news will be condicionate by the day
        stop music fadeout 1.0
        play music "audio/news.mp3" volume 0.17
        plNews "{cps=16}Buenos dias, y bienvenidos a noticias Siete, vuestro canal de confianza{/cps}"
        plNews "{cps=16}El dia de hoy será soleado y caluroso, con temperaturas que alcanzarán los 33 grados, así que no olviden hidratarse y usar protector solar.{/cps}"
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
        $ renpy.notify("Sal a hacer la compra")
        return
    elif hour == 13:
        stop music
        hide screen digital_clock
        show screen tv_shit
        show text '{cps=14}{color=#270303ff}...{/color}{/cps}' at Position(xalign=0.8, yalign=0.1) zorder 100
        pause 3
        show text '{cps=14}{color=#270303ff}Vaya programa más raro{/color}{/cps}' at Position(xalign=0.8, yalign=0.1) zorder 100
        pause 3
        show text '{cps=14}{color=#270303ff}De verdad te gusta esto?{/color}{/cps}' at Position(xalign=0.8, yalign=0.1) zorder 100
        pause
        narrator "{cps=16}Supongo que ya habrás terminado de comer{/cps}" 
        narrator "{cps=14}Ahora es momento de disfrutar la tarde{/cps}" 
        hide screen tv_shit
        show screen digital_clock
        stop sound
        $ hour += 1
        $ room = "livingroom"
        play music "audio/ambientenoon.mp3" loop
        jump main_loop



screen tv_shit():
    add Movie(
        play="images/video/tvshit_fixed.mp4",
        loop=True
    )

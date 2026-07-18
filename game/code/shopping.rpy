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
    $ renpy.notify("Explora la casa")
    play music "audio/ambientedia.mp3" loop volume 0.2 fadein 2.0
    hide screen compra
    $ room = "hall2"
    jump main_loop
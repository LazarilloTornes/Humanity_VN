image eat = im.Scale("bg eater.jpeg", 1800, 1080)
image bg_superkmarket = im.Scale("bg supermarket.png", config.screen_width, config.screen_height)
image bg_verduras = im.Scale("bg verdura.png", config.screen_width, config.screen_height)
image bg_pasta = im.Scale("bg pasta.png", config.screen_width, config.screen_height)
image bg_carniceria = im.Scale("bg carniceria.png", config.screen_width, config.screen_height)
image bg_capricho = im.Scale("bg capricho.png", config.screen_width, config.screen_height)
image bg_sopa_instantanea = im.Scale("bg sopa.png", config.screen_width, config.screen_height)
image bg_ventana = im.Scale("bg ventana.png", config.screen_width, config.screen_height)
image bg_pagar = im.Scale("bg pagar.jpg", config.screen_width, config.screen_height)
image mainroom = "bg/bg_bedroom.png"
image livingroom = "bg/bg_livingroom.png"
image hall_bh = "bg/bg_hall2.png"
image wup = "bg/bg_wup.png"
image ticket = "ticket.png"
image bath = "bg/bg_bathroom.png"
image closet = im.Scale("bg/bg_closet.png", config.screen_width, config.screen_height)

screen Mr_Game_and_Watch():
    if room == "mainroom":
        add "bg/bg_bedroom.png"

        imagebutton:
            idle "interactive/b.png"
            hover "interactive/b_h.png"
            focus_mask True
            action Call("dlg_bed")
        imagebutton:
            idle "interactive/sl.png"
            hover "interactive/sl_h.png"
            focus_mask True
            action Call("dlg_wordsearch")
        imagebutton:
            idle "interactive/m.png"
            hover "interactive/m_h.png"
            focus_mask True
            action SetVariable("room", "escritorio")
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
    elif room == "escritorio":
        add im.Scale("bg/bg_escritorio.png", config.screen_width, config.screen_height)
        textbutton "Habitacion":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "mainroom")
    elif room == "closet":
        add im.Scale("bg/bg_closet.png", config.screen_width, config.screen_height)
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
        add "bg/bg_hall.png"
        textbutton "Salón":
            text_style "txtRoom"
            xpos 1070
            ypos 1000
            action SetVariable("room", "livingroom")
        textbutton "Habitacion":
            text_style "txtRoom"
            xpos 830
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
        textbutton "Baño":
            text_style "txtRoom"
            xpos 350
            ypos 650
            action SetVariable("room","bathroom")
    elif room == "bathroom":
        add "bg/bg_bathroom.png"
        
        textbutton "Atrás":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "pasillo")
        imagebutton:
            idle "interactive/lvb.png"
            hover "interactive/lvb_h.png"
            focus_mask True
            action Jump("first_impresion")
    elif room == "kitchen":
        add "bg/bg_kitchen.png"
        imagebutton:
            idle "interactive/mw.png"
            hover "interactive/mw_h.png"
            focus_mask True
            action Call("dlg_eat")
        imagebutton:
            idle "interactive/food.png"
            hover "interactive/food_h.png"
            focus_mask True
            action Call("dlg_eat")
        imagebutton:
            idle "interactive/cf.png"
            hover "interactive/cf_h.png"
            focus_mask True
            action Call("dlg_eat")        
        textbutton "Atrás":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "pasillo")
    elif room == "livingroom":
        add "bg/bg_livingroom.png"
        imagebutton:
            idle "interactive.png"
            hover "interactive.png"
            xpos 300
            ypos 580
            action Call("dlg_window")
        imagebutton:
            idle "interactive/s.png"
            hover "interactive/s_h.png"
            focus_mask True
            action Call("dlg_sofa")
            
        textbutton "Atrás":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "pasillo")
    elif room == "hall2":
        add "bg/bg_hall2.png"
        textbutton "Puerta":
            text_style "txtRoom"
            xpos 950
            ypos 1000
            action SetVariable("room", "door")
        textbutton "Habitación":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "mainroom")
        textbutton "Cocina":
            text_style "txtRoom"
            xpos 1600
            ypos 350
            action SetVariable("room", "kitchen")
        textbutton "Salón":
            text_style "txtRoom"
            xpos 900
            ypos 300
            action SetVariable("room", "livingroom")
        textbutton "...":
            text_style "txtRoom"
            xpos 300
            ypos 850
            action SetVariable("room", "guestroom")
    elif room == "door":
        add "bg/bg_door.png"
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
        add im.Scale("bg/bg_guestroom.png", config.screen_width, config.screen_height)
        textbutton "Atrás":
            text_style "txtRoom"
            xpos 850
            ypos 1000
            action SetVariable("room", "hall2")

label first_impresion:
    
    show bath at Position(xpos=700, ypos=1050)
    hide screen digital_clock
    show text '{cps=14}{color=#f5f0e3}...{/color}{/cps}' at Position(xalign=0.95, yalign=0.5)
    pause 2.0
    hide text 
    show text '{cps=14}{color=#f5f0e3}Te preguntarás ...{/color}{/cps}' at Position(xalign=0.95, yalign=0.5)
    pause 2.0
    hide text
    show text '{cps=14}{color=#f5f0e3}Que es esta{p} franja negra?{/color}{/cps}' at Position(xalign=0.95, yalign=0.5)
    pause 2.0
    hide text
    show text '{cps=4}{color=#f5f0e3}...{/color}{/cps}' at Position(xalign=0.95, yalign=0.5)
    pause 2.0
    hide text
    show text '{cps=14}{color=#f5f0e3}Pero,{p}aún no es el momento{/color}{/cps}' at Position(xalign=0.95, yalign=0.5)
    pause 2.0
    hide text
    show text '{cps=4}{color=#f5f0e3}Espera un poco{p} y lo averiguarás.{/color}{/cps}' at Position(xalign=0.95, yalign=0.5)
    pause 2.0
    hide text
    hide bath
    show screen digital_clock
    jump main_loop
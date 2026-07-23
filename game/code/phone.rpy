#Minesweeper game
#celd_status = 0 nothing
#celd_status = -1 mine

#what coordenates I have to search
# x-1,y-1   x,y-1   x+1,y-1
# x-1,y     x,y     x+1,y
# x-1,y+1   x,y+1   x+1,y+1
default quick_menu_open = False
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

#En efecto, el juego del buscaminas esta incorporado en el telefono
default phone_tab = "home"
default contacts = ["AAMamá","AAPapá"]
default phone_open = False
default selected_contact = None
screen phone():
    
    modal True

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
            xsize 60
            ysize 60
            xpos 1470
            ypos 250
            action SetVariable("phone_tab", "contacts"),Show("phone")
        imagebutton:
            idle "minesweeperbutton.png"
            hover "minesweeperbutton.png"
            xsize 60
            ysize 60
            xpos 1530
            ypos 250
            action SetVariable("phone_tab", "minesweeper"), Show("phone")
        imagebutton:
            idle "bank_button.png"
            hover "bank_button.png"
            xsize 60
            ysize 60
            xpos 1590
            ypos 250
            action SetVariable("phone_tab", "bank"), Show("phone")
        imagebutton:
            idle "buttons/btn_config.png"
            hover "buttons/btn_config.png"
            xsize 60
            ysize 60
            xpos 1650
            ypos 250
            action SetVariable("phone_tab", "config"),SetVariable("quick_menu_open", True), Show("phone")
        if alquilar:
            $ phone_open = True
            imagebutton:
                idle "rent_button.png"
                hover "rent_button.png"
                xsize 60
                ysize 60
                xpos 1470
                ypos 310
                action SetVariable("phone_tab", "rent_room"), Show("phone")
    elif phone_tab == "config":
        imagebutton:
            idle "back_button.png"
            hover "back_button.png"
            xpos 1450
            ypos 370
            action SetVariable("phone_tab", "home"), SetVariable("quick_menu_open", False), Show("phone")
   
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
            xpos 1520
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
                            [Hide("phone"),SetVariable("phone_open", False), Jump("dlg_661")],
                            If(
                                i == "627",
                                Jump("dlg_627"),
                                If(
                                    i == "AAMamá",
                                    [Hide("phone"), SetVariable("phone_open", False), Jump("dlg_mama")],
                                    If(
                                        i == "AAPapá",
                                        [Hide("phone"), SetVariable("phone_open", False), Jump("dlg_papa")],
                                        NullAction()
                                    )
                                )
                            )
                        )
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
        imagebutton:
            idle "back_button.png"
            hover "back_button.png"
            xpos 1470
            ypos 370
            action SetVariable("phone_tab", "home"), Show("phone")
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
    elif phone_tab == "minesweeper":
        draggroup:

            drag:
                drag_name "popup"
                draggable True
                xpos 300
                ypos 150
                xsize 800
                ysize 600
                drag_handle (0,0,800,50)
                fixed:
                    add "images/buttons/minigame_window.png"
                    grid WIDTH HEIGHT:    
                        spacing 2
                        xalign 0.5
                        yalign 0.6
                        for y in range(HEIGHT):
                            for x in range(WIDTH):
                                if state[y][x] == HIDDEN:
                                    frame:
                                        xsize 50
                                        ysize 50
                                        background "#2c372a"

                                        textbutton "":
                                            action If(tool_mode == "BANDERIN",
                                            Function(toggle_flag, x, y),
                                            Function(reveal_cell, x, y))
                                            xfill True
                                            yfill True
                                elif state[y][x] == FLAGGED:
                                    frame:
                                        xsize 50
                                        ysize 50
                                        background "#2c372a"
                                        text "🚩"
                                else:
                                    frame:
                                        xsize 50
                                        ysize 50
                                        background "#ccc"   # light color

                                        if board[y][x] == -1:
                                            text "💣" style "txtMinesweeper"
                                            $ win = False
                                        elif board[y][x] > 0:
                                            text str(board[y][x]) style "txtMinesweeper"
                                        else:
                                            text "" style "txtMinesweeper"
                    textbutton "[tool_mode]":    
                        xpos 20
                        ypos 120
                        text_style "txtMinesweeper"
                        padding (15, 10)
                        background "#bbc5b9"
                        action If(tool_mode == "REVELAR",
                                SetVariable("tool_mode", "BANDERIN"),
                                SetVariable("tool_mode", "REVELAR"))
                    imagebutton:
                        idle "back_button.png"
                        hover "back_button.png"
                        xpos 60
                        ypos 37
                        action SetVariable("phone_tab","home"), Show("phone")
                    imagebutton:
                        idle "reset_button.png"
                        hover "reset_button.png"
                        xpos 10
                        ypos 37
                        action Function(reset_game)
                    

                

        
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
    $ phone_open = False
    jump main_loop
label dlg_papa: 
    show black
    stop music fadeout 1.0
    play sound "audio/call.mp3" fadein 0.5
    pause 10
    stop sound fadeout 0.5
    play music "audio/ambientedia.mp3" loop volume 0.2 fadein 0.5
    "{cps=15}No parece que vaya a responder...{/cps}"
    $ phone_open = False
    jump main_loop
label dlg_661: 
    stop music fadeout 1.0
    play sound "audio/call.mp3" fadein 0.5
    pause 2
    stop sound fadeout 0.5
    play music "audio/ambientedia.mp3" loop volume 0.2 fadein 0.5
    if alquilar == False:
        t "{cps=15}Hola, buenos días, ha llamado al 661 {b}Vendemos tu Habitación{/b}{/cps}"
        t "{cps=15}Podría decirme su nombre para dirigirme a usted?{/cps}"
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
            $ phone_tab = "home"
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
        


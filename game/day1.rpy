label day1:
    $ resets += 1
    $ day = 1
    call resetVariables from _call_resetVariables
    call introDay1

    if papyrusMourn:
        $ papyrusMourn = False
        menu:
            "Jump to the Building":
                jump papyrusGasterConversation
    elif resets == 1:
        menu: 
            "Ahh??!!" :
                jump titleScreen
    else:        
        menu:
            "Jump to the Building":
                show papyrusImg angry at fade:
                    xalign 0.4
                jump normalPath
            "Ask Gaster the Position" if gasterInformPosition:
                jump gasterInformThePosition         
            
            #"Ask Sans about creating a Shortcut" if doors:
            #    jump shortcut

label normalPath:
    call jumpBuilding
    call reunionRoomDay1

    menu:
        "Toriel, I... I...":
        #   $ day2 = False
            call tryToExplain
        "But First":
        #   $ day2 = False
            call thanks
        "Be Quiet":
        #   $ day2 = False
            call beQuiet
        #"Explain your Idea" if idea:
        #   $ day2 = True
        #   jump idea

    call torielsAdvice
    call endOfDay1


jump day2

return

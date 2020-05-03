label day1:
    $ resets += 1
    $ day = 1
    call resetVariables from _call_resetVariables
    call introDay1 from _call_introDay1

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
                call gasterInformThePosition from _call_gasterInformThePosition
                jump altPath
            
            "Ask Sans about creating a Shortcut" if doors:
                $ altPath = True
                call shortcut
                jump altPath

label altPath:
    call papyrusGasterIncidentAverted from _call_papyrusGasterIncidentAverted
    call endOfDay1 from _call_endOfDay1
    jump altDay2

label normalPath:
    call jumpBuilding from _call_jumpBuilding
    call reunionRoomDay1 from _call_reunionRoomDay1

    menu:
        "Toriel, I... I...":
        #   $ day2 = False
            call tryToExplain from _call_tryToExplain
        "But First":
        #   $ day2 = False
            call thanks from _call_thanks
        "Be Quiet":
        #   $ day2 = False
            call beQuiet from _call_beQuiet
        #"Explain your Idea" if idea:
        #   $ day2 = True
        #   jump idea

    call torielsAdvice from _call_torielsAdvice
    call endOfDay1 from _call_endOfDay1_1
    jump day2

label endOfDay1Trigger:
    call endOfDay1 from _call_endOfDay1_2
    jump day2

return

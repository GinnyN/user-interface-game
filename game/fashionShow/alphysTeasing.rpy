label alphysTeasing: 
    scene day2 suit undyne with dissolve:
        ypos -0.3
        linear 7 ypos 0.0
    undyne "What do you think Alphys?"
    show alphysImg casual realizing flip zorder 3 at fade:
        xpos 0.2
        ypos -0.2
    alphys "..."
    alphys "..."
    alphys "..."
    alphys "..."
    toriel "I'll take Frisk out of here"
    undyne "I just love when Alphys get so passionate about something..."
    stop music
    pause(0.1)
    scene toriel house with vpunch
    play sound "music/fx/thump.wav"
    pause(1)
    show undyneImg mild surprise zorder 1 at fade:
        xpos 0.1
        ypos -0.2
    undyne "ALPHYS"
    show mettaton position zorder 3 at fade:
        xpos 0.35
        ypos 0.205
    call mettatonSurprisedFlip from _call_mettatonSurprisedFlip_1
    metatton "Oh no"
    metatton "Her levels of "
    extend "'passion' were too high!"

    menu:
        "Undyne takes her back home":
            jump undyneLab
        "Papyrus takes her back home":
            jump papyrusLab

label undyneLab:
    show undyneImg happy at fade
    undyne "I'll better take her back home!"
    call mettatonComplicitFlip from _call_mettatonComplicitFlip
    metatton "Take the suit as well"
    show undyneImg mild surprise
    undyne "?!"
    metatton "But don't tell her it was my idea"
    show undyneImg happy at fade
    pause(1.5)
    hide undyneImg
    call mettatonPresenting from _call_mettatonPresenting_4
    metatton "Well, we better jump to the decision then!"
    hide mettaton
    $ undyneThere = False
    jump suitDecisionCall

label papyrusLab:
    $ sansSuit = 2
    show papyrusImg me zorder 0 at fade:
        xpos -0.2
    papyrus "I'LL TAKE HER BACK HOME"
    hide mettaton
    show papyrusImg delight
    show undyneImg bored flip:
        xpos 0.4
    undyne "Papyrus please"
    papyrus "SHE MUST BE OVERWHELMED WITH SO MUCH COOLNESS IN SUITS"
    show papyrusImg proud
    papyrus "AND, EVEN IF I'M THE COOLEST, SHE DOESN'T HAVE A CRUSH ON ME"
    show papyrusImg delight
    show undyneImg frustrated flip
    undyne "Ngaaa..."
    show undyneImg neutral flip
    undyne "Ok"
return


label finishPlan:
    scene toriel house with dissolve
    show mettaton position zorder 3 at fade:
        xpos 0.35
        ypos 0.205
    call mettatonPresentingFlip from _call_mettatonPresentingFlip_3    
    show sansImg position zorder 3 at fade:
        xpos 0
        ypos -0.05
    call sansSuitStiff from _call_sansSuitStiff_3
    metatton "Excelent choice!"
    metatton "You look marvelous!"
    hide mettaton
    play music "music/05 Ruins.mp3" fadein 1 fadeout 1    
    show papyrusImg surprised happy flip zorder 2 at fade:
        xpos 0.3
    papyrus "THIS WAS AMAZING!"
    call sansSuitBored from _call_sansSuitBored_1
    if undyneThere:
        show undyneImg bored flip zorder 3 at fade:
            xpos 0.4
            ypos -0.2
        undyne "And wholefully innecesary"
        show papyrusImg delight flip
        papyrus "BUT SANS LOOK VERY COOL!"
        hide undyneImg
    else:
        sans "and kind of tacky"
        show papyrusImg delight flip
        papyrus "BUT YOU LOOK VERY COOL SANS!"
    show torielImg teacher happy flip zorder 3 at fade:
        xpos 0.5
    toriel "And you have a new suit which we needed"
    call sansSuitSarcastic from _call_sansSuitSarcastic_1
    sans "the things i do for my brother"
    hide torielImg
    papyrus "AHHH..."
    papyrus "YOU ARE ADORABLE"
    sans "don't tell me that"
    hide sansImg
    hide papyrusImg
    show asgoreImg shirt crossed flip zorder 1 at fade:
        xpos 0.3
        ypos -0.15
    show torielImg teacher neutral flip zorder 3 at fade:
        xpos 0
    asgore "Ahhh..."
    asgore "Brotherly love"
    hide torielImg

    
    show asgoreImg shirt serious flip
    show papyrusImg neutral zorder 2 at fade:
        xpos 0
    if undyneThere:
        show undyneImg neutral zorder 3 at fade:
            xpos -0.1
            ypos -0.2
    asgore "Tomorrow we will start searching in the woods"
    asgore "Hopefully we're going to end this problem this week"
    if undyneThere:
        show papyrusImg angry
        show undyneImg motivated
        "* YES SIR!"
    else:
        papyrus "YES SIR"
        show asgoreImg shirt explaining flip
        asgore "Papyrus, please tell Undyne about this tomorrow, ok?"
        papyrus "YES SIR"
    return
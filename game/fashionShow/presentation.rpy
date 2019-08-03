label presentation:
    scene black with dissolve
    metatton "Welcome! Gentlemen and Gentlebeauties"
    metatton "To today's Metatton's Fashion Emergency!"
    scene toriel house
    show lights at sparkles zorder 4
    play music "music/49 It's Showtime!.mp3" fadein 1 fadeout 1
    show sansImg hoddie done zorder 3 at fade:
        xpos 0
        ypos -0.05
    show mettaton position zorder 3 at fade:
        xpos 0.35
        ypos 0.205
    call mettatonPresenting from _call_mettatonPresenting
    pause(1)
    sans "just do this thing quickly"
    call mettatonSurprisedFlip from _call_mettatonSurprisedFlip
    metatton "My oh My, our subject today has a temper"
    undyne "BUT HE DOESN'T HAVE AN OPTION"
    hide lights
    call mettatonDelightFlip from _call_mettatonDelightFlip
    metatton "Those are my favorite subjects!"
    call mettatonPresenting from _call_mettatonPresenting_1
    metatton "Let's see for what you have to dress for!"
    hide mettaton
    hide sansImg
    show torielImg teacher neutral flip zorder 3 at fade:
        xpos 0.3
    toriel "..."
    show torielImg teacher surprised
    toriel "Ah... ap..."
    show torielImg teacher surprised flip
    toriel "Ahh.."
    show torielImg teacher surprised 
    toriel "Ap.."
    show torielImg unsure flip
    toriel "..."
    show torielImg teacher neutral flip
    toriel "We just need a formal suit for an official meeting"
    metatton "But with GLAMOUR and PIZZAZ"
    show torielImg teacher angry flip
    toriel "ehh.. No"
    toriel "Just formal"
    metatton "..."
    metatton "I still can do something with that"
    hide torielImg
    show mettaton position zorder 3 at fade:
        xpos 0.35
        ypos 0.205
    call mettatonPresenting from _call_mettatonPresenting_2
    metatton "Well Darlings, let's present the first of all options!"
    $ alphysHot = 0
    $ undyneThere = True
    return


label bonestrousleSuit:
    scene day2 suit red with dissolve:
        ypos -0.3
        linear 7 ypos 0.0
    metatton "This is a great design by our greatest designer"
    metatton "Combines a stylish white suit with a wonderful red tie"
    metatton "Great for big and special days"
    metatton "In which you are going to be the star"
    show mettaton position zorder 3 at fade:
        xpos 0.35
        ypos 0.205
    call mettatonPresentingFlip from _call_mettatonPresentingFlip
    show sansImg position zorder 3 at fade:
        xpos 0
        ypos -0.05
    call sansSuitStiff from _call_sansSuitStiff
    sans ".."
    sans "i cannot move my shoulders"
    sans "even if i don't have any"
    metatton "Let's see what the public is thinking!"
    return

label megalovaniaSuit:
    scene day2 suit blue with dissolve:
        ypos -0.3
        linear 7 ypos 0.0
    metatton "This is a wonderful design by our greatest designer"
    metatton "It an elegant blue blazer with a minimalistic tie"
    metatton "Excelent all types of events"
    metatton "I which you will dazzle with style!"
    show mettaton position zorder 3 at fade:
        xpos 0.35
        ypos 0.205
    call mettatonPresentingFlip from _call_mettatonPresentingFlip_1
    show sansImg position zorder 3 at fade:
        xpos 0
        ypos -0.05
    call sansSuitStiff from _call_sansSuitStiff_1
    sans ".."
    sans "i don't have a body and anyway i can barely move"
    metatton "Let's see what the public is atching to say!"
    return

label spearsSuit:
    scene day2 suit green with dissolve:
        ypos -0.3
        linear 7 ypos 0.0
    metatton "This is a incredible design by our greatest designer"
    metatton "It has a wonderful green combination of suit and shirt, with a purple tie"
    metatton "Wonderful for those big days"
    metatton "You need to be deckered with style!"
    show mettaton position zorder 3 at fade:
        xpos 0.35
        ypos 0.205
    call mettatonPresentingFlip from _call_mettatonPresentingFlip_2
    show sansImg position zorder 3 at fade:
        xpos 0
        ypos -0.05
    call sansSuitStiff from _call_sansSuitStiff_2
    sans "i cannot breathe"
    sans "and i don't need to breathe"
    call mettatonPresenting from _call_mettatonPresenting_3
    metatton "Let's see what the public want to tell us!"
    return

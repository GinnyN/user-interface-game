label mettatonsfashion:
    call presentation

    label loopSuit:
        menu:
            "The Red One":
                $ suit = 1
                call bonestrousleSuit
            "The Blue One":
                $ suit = 2
                call megalovaniaSuit
            "The Green One":
                $ suit = 3
                call spearsSuit
        
    call publicAsk

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
    jump publicAsk

label publicAsk:
    $ askUndyne = False
    menu:
        "Ask Asgore":
            hide mettaton
            hide sansImg
            show asgoreImg shirt crossed flip zorder 3 at fade:
                xpos 0.1
            if suit == 1:
                asgore "It look very well on him"
                asgore "That shirt has a nice color"
                asgore "Goes very well with his bones' color"
            elif suit == 2:
                asgore "The blue color suits him"
                asgore "And that shirt..."
                asgore "Goes very well with his eyes"
            elif suit == 3:
                asgore "The green purple combination is very pleasant"
                asgore "That shirt combines very well"
                asgore "It has a good fit"
            $ alphysHot = 0
            hide asgoreImg
        "Ask Papyrus":
            hide mettaton
            hide sansImg
            show papyrusImg surprised happy flip zorder 2 at fade:
                xpos 0.3
            if suit == 1:
                papyrus "METATTON IS SOOOO BISHONEN AND SEXY I'LL DIE!!"
                show papyrusImg uhh flip
                papyrus "I MEAN"
                show papyrusImg screamingCall flip
                papyrus "YOU LOOK GREAT SANS!"
                show papyrusImg delight flip
                toriel "Yes Papyrus"
                toriel "Keep Supporting him"
                sans "somebody forgot i'm here against my will"
                papyrus "BUT I'M STILL SUPPORTING YOU!"
            elif suit == 2:
                papyrus "OHHH I CAN'T BELIEVE I'M SO CLOSE TO MY SEXY RECTANGLE IN HIS OWN SHOW!!!"
                show papyrusImg scared flip
                papyrus "OH!"
                show papyrusImg screamingCall flip
                papyrus "IT REALLY SUITS YOU SANS!"
                sans "papyrus don't"
                show papyrusImg angry flip
                papyrus "WHAT?!"
                papyrus "I REALLY MEAN IT!"
            elif suit == 3:
                papyrus "I'M SO CLOSE I CAN SEE HIS BISHONEN EYES..."
                show papyrusImg delight flip
                papyrus "OH ME!"
                show papyrusImg screamingCall flip
                papyrus "IT HAS A GOOD FIT ON YOU SANS!"
                toriel "I must agree"
                show papyrusImg delight flip
                papyrus "KEEP SUPPORTING SANS!"
                sans "why?"
                sans "whhhhyyyy?!"
            hide papyrusImg
            $ alphysHot = 0
        "Ask Toriel":
            hide mettaton
            hide sansImg
            show torielImg teacher neutral flip zorder 2 at fade:
                xpos 0.2
            if suit == 1:
                toriel "I think he looks very s..."
                show torielImg teacher unsure flip
                toriel "mmm"
                show torielImg teacher neutral flip
                toriel "Confident in it"
                papyrus "TORIEL APROVES SANS!"
            elif suit == 2:
                toriel "I think he looks very s..."
                show torielImg teacher unsure flip
                toriel "mmm"
                show torielImg teacher neutral flip
                toriel "Dreamy in it"
                show torielImg teacher surprised flip
                toriel "!?"
                frisk "XD"
                asgore ":("
                papyrus "TORIEL *DEFINITELY* APROVES SANS!"
            elif suit == 3:
                toriel "I think he looks very p..."
                show torielImg teacher unsure flip
                toriel "mmm"
                show torielImg teacher neutral flip
                toriel "comfortable in it"
                papyrus "I DON'T KNOW WHAT SHE REALLY WAS GOING TO SAY BUT SHE APPROVES!"
            hide torielImg
            $ alphysHot = 0
        "Ask Undyne":
            hide mettaton
            hide sansImg
            $ askUndyne = True
            show undyneImg mild surprise flip zorder 1 at fade:
                xpos 0.3
                ypos -0.2
            if suit == 1:
                undyne "Uh?"
                undyne "Me?"
                undyne "Why me?"
                undyne "Do you really want me??"
            elif suit == 2:
                undyne "Ahhh..."
                undyne "What..."
                show undyneImg thinking flip
                undyne "Wait.."
                undyne "what can I sa..."
            elif suit == 3:
                undyne "Wait..."
                show undyneImg thinking flip
                undyne "No, no..."
                show undyneImg mild surprise flip
                undyne "Ah.."
                show undyneImg thinking flip
                undyne "I know"
                undyne "I KNOW!!"
            hide undyneImg
            $ alphysHot = 0
        "Ask Alphys":
            hide mettaton
            hide sansImg
            if alphysHot == 0:
                show alphysImg casual confused mild flip zorder 3 at fade:
                    xpos 0.2
                    ypos -0.2
                alphys "(Why am I feeling so turn on right now?)"
                $ alphysHot = alphysHot + 1
            elif alphysHot == 1:
                show alphysImg casual confused flip zorder 3 at fade:
                    xpos 0.2
                    ypos -0.2
                alphys "(He's just a gross fat skeleton)"
                alphys "(Who's also very smart)"
                $ alphysHot = alphysHot + 1
            else:
                show alphysImg casual realizing flip zorder 3 at fade:
                    xpos 0.2
                    ypos -0.2
                alphys "(OH NO, I forgot I always get turn on by people on suits)"
                alphys "(Everybody look always so great on suits)"
                show mettaton position zorder 3 at fade:
                    xpos -0.1
                    ypos 0.205
                call mettatonThinking from _call_mettatonThinking
                metatton "Mmm..."
                metatton "Darlings, I am noticing a disturbance in the force..."
                show undyneImg mild surprise flip zorder 1 at fade:
                    xpos 0.4
                    ypos -0.2
                undyne "Oh wait"
                undyne "I know!"
                show undyneImg laugh flip
                undyne "Hey! Metatton! Can we?!"
                call mettatonDelight from _call_mettatonDelight
                metatton "Oh, Please! Be my guest!"
                jump alphysTeasing
            hide alphysImg
        "Ask Frisk":
            hide mettaton
            hide sansImg
            if suit == 1:
                show friskImg unsure flip zorder 3 at fade:
                    xpos 0.5
                    ypos 0.13
                frisk "..."
                toriel "Do you think?"
                toriel "mmm...."
            elif suit == 2:
                show friskImg affirmation flip zorder 3 at fade:
                    xpos 0.5
                    ypos 0.13
                frisk "..."
                papyrus "ONE VOTE FOR THE BLUE ONE!"
            elif suit == 3:
                show friskImg angry mild flip zorder 3 at fade:
                    xpos 0.5
                    ypos 0.13
                frisk "Desaproving expression"
                undyne "Come on Frisk!"
                undyne "Help me out on this!"
            hide friskImg
            $ alphysHot = 0

    metatton "Are we ready to make a decision?"
    if askUndyne:
        undyne "Hey! Wait! Let me f..."

    menu:
        "Yes":
            metatton "Let's see which one is the winner!"
            jump suitDecision
        "No":
            metatton "Let's see other suits then!"
            jump loopSuit

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

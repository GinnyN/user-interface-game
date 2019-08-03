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
            jump suitDecisionCall
        "No":
            metatton "Let's see other suits then!"
            jump loopSuit
label day2:
    #$ if day2:
    #    jump alternative

label schoolPapyrusRun:
    scene black with dissolve
    pause(1.0)
    scene skelebroHouse outside with dissolve
    pause 0.5
    show studentImg dog gossiping flip zorder 3 at fade:
        xalign 0.7 yalign 1.0
    show kidImg listening zorder 0 at fade:
        xalign 0.3 yalign 1.0
    "Student" "* Did you heard that?"
    "Student" "* The teacher said we'll not meet with Papyrus today!"
    show studentImg dog sorry flip zorder 4 at fade
    show kidImg angry at fade
    monsterKid "No sense!"
    monsterKid "Papyrus never miss his morning run!"
    monsterKid "He's as cool as that!"
    show studentImg dog happy at fade
    show kidImg happy at fade
    show papyrusImg coolDude cocky flip zorder 2 at fade:
        xalign 0.9 yalign 1.0
    play music "music/16 Nyeh Heh Heh!.mp3" fadein(1)
    papyrus "HI KIDS!"
    papyrus "THE GREAT PAPYRUS HAS ARRIVED!"
    monsterKid "Papyrus!"
    papyrus "DON'T STOP MOVING!"
    papyrus "YOU DON'T WANNA ANGER YOUR TEACHER!"
    show undyneImg gym sarcastic at fade:
        xalign 0.2 yalign 1.0
    undyne "And what's Toriel told you!?"
    show papyrusImg coolDude surprised flip at fade
    show studentImg dog surprised flip at fade:
        xalign 0.8 yalign 1.0
    show kidImg scared flip at fade:
        xalign 0.6 yalign 1.0
    "* UNDYNE!"
    show studentImg dog scared flip
    show kidImg hiding flip
    show papyrusImg coolDude annoyed flip at fade
    show undyneImg gym bored at fade
    undyne "Move along kids, I need to talk with 'The Great Papyrus'"
    hide studentImg
    hide kidImg
    papyrus "I'M DOING WHAT TORIEL TOLD ME"
    undyne "You are keeping your rutine Papyrus"
    undyne "You need to rest!"
    show papyrusImg coolDude explaining flip at fade
    papyrus "BUT KEEPING WITH MY RUTINE IS RELAXING TO ME!"
    show undyneImg gym yelling at fade
    undyne "That's the opposite of a vacation Papyrus"
    show papyrusImg coolDude screaming flip at fade
    papyrus "BUT I DON'T TAKE VACATIONS!"
    show undyneImg gym frustrated at fade
    undyne "BUT NOW YOU SHOULD! AND IT'S TORIEL'S ADVICE!"
    show papyrusImg coolDude explaining flip at fade
    papyrus "BUT.."
    papyrus "I LIKE TO BE WITH THE KIDS"
    undyne "And I..."
    show undyneImg gym shy at fade
    undyne "..."
    show papyrusImg coolDude annoyed flip at fade
    papyrus "WHAT?!"
    stop music
    undyne "I don't want you to be with them"
    undyne "Not during this week at least"
    show papyrusImg coolDude speakless flip at fade
    papyrus "UNDYNE..."
    show undyneImg gym frustrated at fade
    undyne "Now, go to marathon Metaton's... "
    show undyneImg gym shy at fade
    extend "whatever is called now"
    show undyneImg gym frustrated at fade

    undyne "NOW GO!"
    hide undyneImg
    papyrus "..."
    hide papyrusImg

# Grillsby

    scene black with dissolve
    play sound "music/fx/steps.wav"
    pause(1.0)
    play music "music/15 sans.mp3" fadein 1
    pause(1.0)
    scene grillsbys inside with dissolve
    show grillsby neutral zorder 1 at fade:
        xalign 0.1 ypos 0.0 
    grillsby "..."
    show papyrusImg coolDude sorry flip zorder 0 at fade:
        xalign 1.0 yalign 1.2
    papyrus "YES, IT'S ME"
    grillsby "..."
    papyrus "NO IT'S NOT A MISTAKE"
    show papyrusImg coolDude sorry flip zorder 0 at fade:
        xpos 0.9 ypos 1.5
    papyrus "I FEEL AWFUL NOW"
    papyrus "UNDYNE THINKS I'M DANGEROUS"
    show papyrusImg coolDude grandiose flip at fade
    papyrus "AND SHOULDN'T BE! BECAUSE I'M THE GREAT PAPYRUS"
    show papyrusImg coolDude sorry flip at fade
    papyrus "Not anymore it seems..."
    grillsby "..."
    papyrus "GIVE ME THE KETCHUP BOTTLE"
    grillsby "?!"
    papyrus "JUST GIVE ME THE KETCHUP BOTTLE"
    grillsby "..."
    hide grillsby
    hide papyrusImg
    show grillsby neutral flip zorder 3 at fade:
        xpos 0.1
    show dogamy neutral flip zorder 2 at fade:
        xpos 0.3 ypos 0.25
    show dogaressa neutral flip zorder 1 at fade:
        xpos 0.5 ypos 0.25
    dogamy "What's happening?"
    grillsby "..."
    show dogamy surprised flip at fade
    show dogaressa surprised flip at fade
    dogamy "You say it's Papyrus?!"
    show dogamy worried at fade
    show dogaressa worried flip at fade
    dogaressa "He doesn't smell like him... weird..."
    grillsby "..."
    show dogamy surprised flip at fade
    show dogaressa surprised flip at fade
    dogamy "He's drinking the ketchup bottle?!"
    dogaressa "He can also do that?!"
    hide dogamy
    hide dogaressa
    hide grillsby
    stop music
    pause(0.1)
    scene grillsbys inside with vpunch
    play sound "music/fx/thump.wav"
    pause(1)
    show sansImg hoddie content flip at fade:
        xpos 0.6 ypos 0.05
    sans "time to..."
    show sansImg hoddie surprised flip at fade
    sans "papyrus?!"
    hide sansImg
    show grillsby neutral flip zorder 3 at fade:
        xpos 0.1
    show dogamy surprised  flip zorder 2 at fade:
        xpos 0.3 ypos 0.25
    show dogaressa worried flip zorder 1 at fade:
        xpos 0.5 ypos 0.25
    dogamy "The world is backwards today!"
    dogaressa "I think I'll need some ketchup myself"

label school:
    play music "music/12 Home.mp3" fadein 1
    scene school outside with dissolve:
        ypos -0.2
        linear 5 ypos -0.5
    pause(1.5)
    scene school gym with dissolve:
        xpos 0
        ypos 0.0
        linear 5 xpos -0.1
    pause(0.8)
    show undyneImg gym happy at fade:
        ypos -0.2
        xpos 0
    undyne "Today was a long one, those kids!"
    show undyneImg gym mildSurprise
    show sansImg hoddie angry flip at fade:
        xpos 0.6
        ypos 0.05
    sans "i should say the same"
    show undyneImg gym yelling
    undyne "SANS?!"
    undyne "shouldn't you be at the elevator to High Snowdin?"
    sans "no... i was taking my break"
    show undyneImg gym bored
    undyne "Break... heh"
    sans "and i found my brother at grillsby"
    show undyneImg gym mildSurprise
    sans "drunk"
    undyne "that isn't a Papyrus thing"
    sans "exactly"
    show undyneImg gym frustrated
    undyne "Ok, ok, he feels bad for what happened yesterday, I get it, tough cookie"
    undyne "But what I have to do with anything now"
    show undyneImg gym mildSurprise
    sans "he was in the floor, sobbing, asking you for forgiveness"
    show undyneImg gym shy
    undyne "Oh"
    sans ".."
    undyne "I told him I didn't want him near to the kids today"
    show sansImg hoddie annoyed flip
    sans ".."
    undyne "He's just unstable after what happened yesterday and..."
    undyne "And even I have problems keeping cool with those kids"
    sans "that's explain it"
    show sansImg hoddie angry flip
    sans "but papyrus loves kids, you know that"
    undyne "I know, but..."
    sans "you don't feel ok with it"
    undyne "Despite I think those humans have it coming"
    show sansImg hoddie unsure flip
    sans "we need to find a way to solve this..."
    show undyneImg gym frustrated
    undyne "Before Papyrus does something REALLY crazy"
    undyne "like he's prone to do"
    play music "music/24 Bonetrousle.mp3" fadeout 1
    show undyneImg gym mildSurprise
    show sansImg hoddie surprised flip
    toriel "WHAT ARE YOU DOING!?"
    show sansImg hoddie surprised
    sans "toriel!"
    scene black with dissolve

#Outside School 
label outsideSchool:
    scene day2 papyrusJump frame1 with dissolve
    pause(0.5)
    scene day2 papyrusJump frame2 with dissolve
    pause(0.5)
    scene day2 papyrusJump frame3 with dissolve
    pause(0.5)
    scene day2 papyrusJump frame4 with dissolve
    pause(0.5)
    scene day2 papyrusJump frame1 with dissolve
    pause(0.5)
    show torielImg teacher angry zorder 2 at fade:
        xpos -0.1
    show sansImg hoddie surprised zorder 3 at fade:
        xpos 0.3
        ypos 0.05
    show undyneImg gym yelling zorder 4 at fade:
        xpos 0.5
        ypos -0.2
    toriel "Papyrus! Come down inmediatly!"
    undyne "I'll catch him up..."
    show sansImg hoddie angry
    sans "let's me try that"
    show undyneImg gym mildSurprise flip
    undyne "?!"
    toriel "Good luck Sans"
    hide sansImg
    hide torielImg
    hide undyneImg
    scene day2 papyrusLanding frame1 with dissolve
    pause(0.5)
    scene day2 papyrusLanding frame2 with dissolve
    pause(0.5)
    scene day2 papyrusLanding frame3 with dissolve
    pause(0.5)
    show papyrusImg angry flip at fade:
        xpos 0.5
    show sansImg hoddie angry at fade:
        xpos 0
        ypos -0.05
    papyrus "SANS?"
    papyrus "IT'S THERE A SHORTCUT TO HERE?!"
    sans "what are you doing papyrus?"

label loop1:
    show papyrusImg angry flip at fade:
        xpos 0.5
    show sansImg hoddie angry at fade:
        xpos 0
        ypos -0.05
    menu:
        "This is for keep my greatness!":
            jump honor
        "Stay away Sans! This is my problem!":
            jump stuborn
        "Sans! I have a Plan!":
            jump plan

label honor:
    papyrus "THIS IS FOR MY OWN GREATNESS SANS!"
    sans "you don't have anything to prove to undyne, really"
    show papyrusImg confused flip
    papyrus "WHO SAID ANYTHING ABOUT HER?!"
    show papyrusImg angry flip
    papyrus "THIS IS FOR ME!"
    papyrus "I NEED TO GO BACK TO BE AS GREAT AS I CAN BE!"
    sans "papyrus, please.."
    jump loop1

label stuborn:
    papyrus "DON'T GET IN THE WAY SANS!"
    papyrus "THIS IS *MY* PROBLEM!"
    sans "i understand the feeling"
    sans "but toriel told you, it's not anymore"
    papyrus "BUT IT'S STILL MY FAULT"
    papyrus "*I* HAVE TO SOLVE IT!"
    sans ".."
    jump loop1

label plan:
    papyrus "I HAVE A PLAN SANS!"
    sans "what kind of plan now..."
    papyrus "I'LL CAPTURE THE REST OF THOSE TERRIBLE HUMANS"
    papyrus "AND I'LL DELIVER THEM TO THE HUMANS' AUTHORITIES!"
    show papyrusImg proud flip
    papyrus "I'LL BE A HERO"
    papyrus "AND THE GOOD HUMANS WILL CONSIDER US ALLIES INSTEAD OF ENEMIES!"
    stop music fadeout 6
    show sansImg hoddie surprised
    sans "......"
    show papyrusImg uhh flip
    papyrus "SANS?"
    show sansImg hoddie neutral
    sans "that's actually a good idea"
    show papyrusImg proud flip
    papyrus "OF COURSE IT IS"
    show sansImg hoddie sideglance
    sans "but.."
    sans "but maybe it needs a bit more of.."
    sans "diplomacy"
    show papyrusImg uhh flip
    papyrus "???"
    show sansImg hoddie neutral
    sans "let's talk with toriel"

label planning:
    scene black with dissolve
    play music "music/05 Ruins.mp3" fadein 1 fadeout 1
    pause(1)
    scene toriel house with dissolve
    show torielImg teacher unsure zorder 2 at fade:
        xpos -0.1
    show papyrusImg neutral flip zorder 2 at fade:
        xpos 0.6
    show sansImg hoddie neutral flip zorder 3 at fade:
        xpos 0.55
        ypos -0.05
    toriel "It doesn't sound half bad"
    show papyrusImg proud flip at fade
    papyrus "OF COURSE IT'S NOT BAD, IT'S MY IDEA"
    show torielImg teacher neutral at fade
    toriel "But Sans it's right, we need to have some diplomacy added to the idea"
    show papyrusImg angry flip at fade
    papyrus "I DON'T DO WORDS. I DO ACTION"
    show torielImg teacher happy at fade
    toriel "We know that my friend, I was thinking on doing it myself"
    show papyrusImg surprised happy flip at fade
    papyrus "REALLY?"
    show sansImg hoddie content flip at fade
    show torielImg teacher neutral at fade
    toriel "Of course"
    show torielImg teacher unsure at fade
    toriel "But I will need help"
    show asgoreImg shirt explaining zorder 1 at fade:
        xpos 0
        ypos -0.15
    asgore "I'm sorry saying this but"
    show sansImg hoddie neutral flip
    show papyrusImg scared flip at fade
    papyrus "YOUR MAJESTY!"
    show papyrusImg uhh flip at fade
    asgore "I would prefer help with capturing those people"
    show asgoreImg shirt embarrased at fade
    asgore "Also, I have never been good with diplomacy"
    show torielImg teacher angry at fade
    toriel "I sadly agree"
    hide asgoreImg at fade
    show undyneImg laugh zorder 1 at fade:
        xpos 0.0
        ypos -0.2
    undyne "Hey, and why don't you go with Sans"
    show sansImg hoddie surprised flip at fade
    show torielImg teacher unsure at fade
    sans "hey"
    show alphysImg casual laugh zorder 3 at fade:
        xpos 0
        ypos -0.2
    alphys "I think is appropiate"
    show sansImg hoddie annoyed flip at fade
    sans "don't"
    show papyrusImg explaining flip at fade:
        xpos 0.5
    papyrus "THAT'S A GOOD IDEA"
    show sansImg hoddie angry at fade
    hide undyneImg at fade
    hide alphysImg at fade
    sans "do i not have a say on this?"
    papyrus "NO"
    show torielImg teacher happy at fade
    toriel "Come on Papyrus, don't be like that with your brother"
    show friskImg explaining zorder 3 at fade:
        xpos 0.1
        ypos 0.1
    frisk "But..."
    frisk "Sans did stand up at Metatton's Hotel"
    papyrus "EXACTLY"
    show torielImg teacher neutral at fade
    toriel "Then is settled"
    hide papyrusImg at fade
    hide friskImg at fade
    show sansImg hoddie angry flip at fade
    sans "i really didn't have any say on this"
    show torielImg teacher happy at fade
    toriel "I cannot go alone and you are the only one who can help me Sans"
    show sansImg hoddie unsure flip at fade
    sans ".."
    show sansImg hoddie angry flip at fade
    sans "ok"
    toriel "Well then"
    show torielImg teacher neutral at fade
    show papyrusImg neutral flip zorder 2 at fade:
        xpos 0.6
    show asgoreImg shirt explaining zorder 1 at fade:
        xpos 0
        ypos -0.15
    toriel "Sans and I will go to talk with the humans authorities"
    asgore "We will ask for an audience in my behalf"
    show torielImg teacher angry at fade
    toriel "We're going to ask for cooperation in the investigation of this human trafficking thing"
    toriel "They are doing it near to our lands for some reason and they kidnapped Frisk"
    toriel "So is our problem too"
    show papyrusImg angry flip at fade
    papyrus "AND WHAT'S GOING TO HAPPEN IF WE FIND THEM FIRST"
    hide papyrusImg at fade
    show undyneImg angry flip zorder 2 at fade:
        xpos 0.5
        ypos -0.2
    undyne "That's a good question"
    undyne "I'll not sat here waiting for you to tell me to crush those bastards"
    show sansImg hoddie angry at fade
    sans "we will improvise"
    show torielImg teacher happy at fade
    toriel "Well yes"
    toriel "We did improv once"
    show asgoreImg shirt embarrased at fade
    hide torielImg at fade
    hide undyneImg at fade
    asgore "I'm sorry Sans but..."
    show sansImg hoddie surprised flip at fade
    show asgoreImg shirt explaining at fade
    asgore "Do you have something else to wear apart of that hoddie?"
    asgore "Something a bit more..."
    asgore "formal?"
    show papyrusImg explaining flip zorder 2 at fade:
        xpos 0.5
    papyrus "NO, HE DOESN'T"
    show sansImg hoddie angry at fade
    sans "papyrus"
    show alphysImg casual explaining zorder 3 at fade:
        xpos -0.2
        ypos -0.2
    alphys "Well... Metatton can help with that"
    show sansImg hoddie done flip at fade
    sans "today is not my day"
    stop music fadeout(1)

label mettatonsfashion:
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
    call mettatonPresenting
    pause(1)
    sans "just do this thing quickly"
    call mettatonSurprisedFlip
    metatton "My oh My, our subject today has a temper"
    undyne "BUT HE DOESN'T HAVE AN OPTION"
    hide lights
    call mettatonDelightFlip
    metatton "Those are my favorite subjects!"
    call mettatonPresenting
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
    call mettatonPresenting
    metatton "Well Darlings, let's present the first of all options!"
    $ alphysHot = 0
    $ undyneThere = True

label loopSuit:
    menu:
        "The Red One":
            jump bonestrousleSuit
        "The Blue One":
            jump megalovaniaSuit
        "The Green One":
            jump spearsSuit

label bonestrousleSuit:
    $ suit = 1
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
    call mettatonPresentingFlip
    show sansImg position zorder 3 at fade:
        xpos 0
        ypos -0.05
    call sansSuitStiff
    sans ".."
    sans "i cannot move my shoulders"
    sans "even if i don't have any"
    metatton "Let's see what the public is thinking!"
    jump publicAsk

label megalovaniaSuit:
    $ suit = 2
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
    call mettatonPresentingFlip
    show sansImg position zorder 3 at fade:
        xpos 0
        ypos -0.05
    call sansSuitStiff
    sans ".."
    sans "i don't have a body and anyway i can barely move"
    metatton "Let's see what the public is atching to say!"
    jump publicAsk

label spearsSuit:
    $ suit = 3
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
    call mettatonPresentingFlip
    show sansImg position zorder 3 at fade:
        xpos 0
        ypos -0.05
    call sansSuitStiff
    sans "i cannot breathe"
    sans "and i don't need to breathe"
    call mettatonPresenting
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
                call mettatonThinking
                metatton "Mmm..."
                metatton "Darlings, I am noticing a disturbance in the force..."
                show undyneImg mild surprise flip zorder 1 at fade:
                    xpos 0.4
                    ypos -0.2
                undyne "Oh wait"
                undyne "I know!"
                show undyneImg laugh flip
                undyne "Hey! Metatton! Can we?!"
                call mettatonDelight
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
    call mettatonSurprisedFlip
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
    call mettatonComplicitFlip
    metatton "Take the suit as well"
    show undyneImg mild surprise
    undyne "?!"
    metatton "But don't tell her it was my idea"
    show undyneImg happy at fade
    pause(1.5)
    hide undyneImg
    call mettatonPresenting
    metatton "Well, we better jump to the decision then!"
    hide mettaton
    $ undyneThere = False

label suitDecision:
    stop music
    scene black with dissolve
    metatton "And the winner is..."
    menu:
        "The Red One":
            $ suit = 1
        "The Blue One":
            $ suit = 2
        "The Green One":
            $ suit = 3
    scene toriel house with dissolve
    show mettaton position zorder 3 at fade:
        xpos 0.35
        ypos 0.205
    call mettatonPresentingFlip    
    show sansImg position zorder 3 at fade:
        xpos 0
        ypos -0.05
    call sansSuitStiff
    metatton "Excelent choice!"
    metatton "You look marvelous!"
    hide mettaton
    play music "music/05 Ruins.mp3" fadein 1 fadeout 1    
    show papyrusImg surprised happy flip zorder 2 at fade:
        xpos 0.3
    papyrus "THIS WAS AMAZING!"
    call sansSuitBored
    if undyneThere:
        show undyneImg bored flip zorder 3 at fade:
            xpos 0.5
            ypos 0.1
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
    call sansSuitSarcastic
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
            xpos 0
            ypos 0.1
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

    jump endOfDay2

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

label alphysHome:
    scene undyneAlphysHouse inside with dissolve
    play music "music/33 Quiet Water.mp3" fadein 1 fadeout 1 
    show papyrusImg neutral zorder 0 at fade:
        xpos -0.2
    show alphysImg casual tired zorder 3 at fade:
        xpos 0.2
        ypos -0.2
    alphys "Thanks Papyrus"
    papyrus "IT'S OK, MY PLEASURE"
    alphys "I'm such a mess..."
    alphys "Undyne must be so embarrased..."
    show papyrusImg delight
    papyrus "SHE ACTUALLY LOVES WHEN YOU DO THIS"
    show papyrusImg neutral
    papyrus "BUT I THOUGHT YOU ALREADY KNEW THAT"
    show alphysImg casual tired flip
    alphys "Yes..."
    alphys "I just cannot believe it myself"
    papyrus "WE CAN ADD THAT 'UNDYNE LOVES ME FOR HOW I'M' TO OUR TRAINING EVERY WEDNESDAY AND FRIDAY"
    alphys "No, we'll not going to do that"
    papyrus "EVERYBODY BELIEVE YOU ARE AMAZING DR. ALPHYS"
    papyrus "IF YOU NEED SOMEONE TO REMIND YOU, APART OF UNDYNE, JUST GIVE A CALL"
    show alphysImg casual nostalgic flip
    alphys "Aw... Papyrus..."
    show alphysImg casual tired flip
    alphys "..."
    show alphysImg casual nostalgic flip
    alphys "Undyne is right, you are way too nice..."
    show papyrusImg uhh
    papyrus "?"
    papyrus "I JUST DO WHAT I THINK IS THE CORRECT THING TO DO"
    papyrus "THAT'S NOT BEEN NICE"
    show papyrusImg neutral
    papyrus "IT'S BEEN CONSEQUENT"
    alphys "Well..."
    show alphysImg casual tired flip
    alphys "..."
    alphys "..."
    show alphysImg casual nostalgic flip
    alphys "If you say so"
    if pen and not program:
        $ penAtAlphys = True
        papyrus "DR. ALPHYS, I KNOW YOU ARE BUSY"
        papyrus "BUT I HAVE A PROBLEM ONLY YOU CAN SOLVE"
        alphys "What do you mean?"
        papyrus "I HAVE HERE THE BLUEPRINTS OF A DETERMINATION ABSORBING MACHINE"
        alphys "How you..."
        papyrus "I CANNOT TELL YOU THAT"
        papyrus "JUST..."
        papyrus "TRUST ME"
        alphys "Ok..."
        papyrus "SOMEONE IS TRAPPED THERE"
        papyrus "IT BECAME ONE WITH EVERYTHING ONCE"
        papyrus "BUT WITH THIS MACHINE IS GETTING THEIR ORIGINAL FORM BACK"
        papyrus "BUT THE PROCESS IS NOT COMPLETE"
        papyrus "CAN YOU SEE IF THERE'S A WAY TO COMPLETE THE PROCESS?"
        alphys "With just the bluprints?"
        papyrus "I DON'T HAVE MORE WITH ME, I'M..."
        alphys "It's going to be a piece of cake"
        papyrus "THANKS!"
        papyrus "JUST KEEP THE THING A SECRET, PLEASE"
        alphys "Will do."

    show papyrusImg me
    papyrus "GOOD NIGHT DR ALPHYS"
    hide papyrusImg
    papyrus "DREAM OF TINY UNDYNES BEEN AWESOME"
    show alphysImg casual laugh
    alphys "PAPYRUS!"

    if pen and not program:
        pause(1)
        alphys "I'm sorry Papyrus"

label endOfDay2:
    if resets > 0:
        call questionsEnd
    
    jump day3

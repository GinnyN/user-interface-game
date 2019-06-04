label day3:
    $ day = 3
    call freeMorning from _call_freeMorning

label forest:
    scene skelebroHouse outside with dissolve
    show papyrusImg neutral zorder 0 at fade:
        xpos 0
    papyrus "EVERYTHING HAS BEEN ACCOUNTED FOR"
    show papyrusImg serious
    papyrus "AND NOW, DIRECTLY TO THE CASTLE!"
    hide papyrusImg
    papyrus "THE KING AND UNDYNE ARE WAITING FOR ME"
    papyrus "TODAY IS THE DAY WE TRAP THOSE AWFUL PEOPLE!"
    if resets < 1:
        pause (0.5)
        "???" "{font=fonts/NewAster.ttf} ... {/font}"
        "???" "{font=fonts/NewAster.ttf} DE... {/font}"
        "???" "{font=fonts/NewAster.ttf} PA... {/font}"
        "???" "{font=fonts/NewAster.ttf} US... {/font}"
        "???" "{font=fonts/NewAster.ttf} ... {/font}"

# label newHome:
    scene day3 intro background with dissolve:
        ypos 0.0
        linear 13 ypos -1.0
    show day3F intro foreground at fade:
        ypos 0.0
        linear 9 ypos -1.1
    play music "music/33 Quiet Water.mp3" fadein(1) fadeout(1) 
    pause (1.0)
    asgore "Remember that we need to just trap them"
    asgore "We don't need them neither maimed or dead"
    undyne "But also we need to remember to be as scary as we can"
    undyne "If those humans suddenly discover they can produce more determination than us"
    papyrus "WE'RE DOOMED!"
    undyne "Exactly"
    show asgoreImg armor joking zorder 1 at fade:
        xpos 0.1
        ypos -0.15
    asgore "I don't think you will have that problem"
    asgore "You are plenty scary yourself"
    show papyrusImg neutral flip  zorder 1 at fade:
        xpos 0.5
    show undyneImg armor cocky zorder 1 at fade:
        xpos -0.1
        ypos -0.2
    undyne "Pfff"
    undyne "Yeah, says the guy with the horns and the trident!"
    show undyneImg armor smile
    asgore "Maybe you have a point there"
    show papyrusImg angry
    show undyneImg armor surprised
    show asgoreImg armor surprised
    papyrus "WE'RE READY!"
    papyrus "LET'S DO THIS!!!"
    hide papyrusImg
    play sound "music/fx/steps.wav"
    show undyneImg armor worried
    show asgoreImg armor joking
    asgore "Between you and me"
    asgore "I think he's the scariest"
    undyne "MMmmm"

#Outside Forest
    scene forest with dissolve
    show papyrusImg confused  zorder 0 at fade:
        xpos 0.0
    papyrus "I'M PRETTY SURE MY DOG LIKE NOSE CAN GUIDE US"
    show papyrusImg dissapointed
    papyrus "BUT THEY DECIDED TO SEPARATE TO COVER MORE AREA"
    papyrus "AS USUAL"
    show papyrusImg proud
    papyrus "WELL, THEY WILL BE SURPRISED WHEN I FIND THE PLACE WHERE THE REST OF THOSE EVIL BEINGS ARE FIRST!"
    hide papyrusImg
    papyrus "*SNIFF SNIFF*"
    show papyrusImg curious zorder 0 at fade:
        xpos 0.0
    papyrus "OH?!"
    hide papyrusImg
    show cuero zorder 0 at fade:
        xpos 0.2
    show coo flip zorder 0 at fade:
        xpos 0.5
    "Monster 1" "* Did you said the place was around here"
    "Monster 2" "* Yes! After what happened two days ago the..."
    stop music fadeout 1.0
    play music "music/16 Nyeh Heh Heh!.mp3" fadein(1)
    show papyrusImg me zorder 0 at fade:
        xpos -0.2
    show cuero flip zorder 0 at fade:
        xpos 0.3
    show coo flip zorder 0 at fade:
        xpos 0.6
    papyrus "HEY!"
    show cuero flip zorder 0 at fade:
        xpos 0.2
    show coo flip zorder 0 at fade:
        xpos 0.5
    "Monster 1" "* Ohh... Hey!"
    show papyrusImg delight
    papyrus "I DIDN'T KNEW THE KING AND UNDYNE RECLUTED MORE MONSTERS TO HELP OUT!"
    show cuero
    "Monster 1" "* Uhhh..."
    show coo flip at fade:
        xpos 0.4
    "Monster 2" "* Yes... we..."
    "Monster 2" "* are helping out"
    show cuero flip at fade:
        xpos 0.5
    papyrus "GREAT!"
    show papyrusImg explainingPointing flip
    show coo
    papyrus "I ALREADY CHECKED OUT THAT AREA AND I'M GOING TO CHECK OUT THERE"
    show papyrusImg explainingPointing
    show coo flip
    papyrus "YOU CAN GO THAT WAY AND CHECK THERE"
    show papyrusImg proud
    papyrus "I'LL GIVE YOU A HEAD START!"
    "Monster 1" "* Yes.. yes..."
    "Monster 2" "* We're going to check out there"
    "Monster 1" "* Thanks..."
    hide papyrusImg
    stop music fadeout 0.1
    show coo at fade:
        xpos 0.1
    "Monster 1" "* He's talking about the king of all monsters?"
    "Monster 2" "* He likes humans" 
    "Monster 2" "* He basically adopted one too!"
    "Monster 1" "* We need to move quickly, before he realize anything"
    menu:
        "Help them out":
            jump helpthemout
        "Let's them go alone":
            jump leaveThemAlone

label leaveThemAlone:
    play music "music/33 Quiet Water.mp3" fadein(1) fadeout(1) 
    $ whoRescueMauricio = True
    "Monster 1" "* Let´s move"
    hide coo
    hide cuero
    pause(0.5)
    show papyrusImg neutral zorder 0 at fade:
        xpos 0.1
    papyrus "HOPEFULLY THOSE TWO ARE GOING TO BE OK"
    hide papyrusImg
    papyrus "SNIFF, SNIFF.."
    show papyrusImg curious flip zorder 0 at fade:
        xpos 0.1
    papyrus "LET'S FOLLOW THE SCENT!"
    scene day3 fortress background with dissolve:
        xpos 0.0
        linear 10 xpos -0.1
    show day3F fortress foreground at fade
    papyrus "ANOTHER OF THIS HUMAN BUILDINGS"
    papyrus "I'D BETTER TELL UNDYNE AND THE KING"
    scene black with dissolve
    play music "music/83 Here We Are.mp3" fadein 1
    pause(1)
    scene fortress inside with dissolve
    show asgoreImg armor awe at fade:
        ypos -0.15
    show undyneImg armor surprised at fade:
        ypos -0.2
        xpos -0.1
    show papyrusImg curious zorder 0 at fade:
        xpos 0.4
    asgore "This must be one of the buildings of the monsters during the war"
    asgore "The humans must have found it and restore it"
    papyrus "WOWIE"
    papyrus "A PIECE OF MONSTERS' HISTORY!"
    show undyneImg armor cocky
    undyne "Let's better check before any human appears"
    undyne "For their own sake"
    hide papyrusImg
    show undyneImg armor surprised
    show asgoreImg armor surprised
    papyrus "HEEEEYYYY!!!! KIDNAPPEEEEERRRRRRSSSSSS!!!"
    hide undyneImg
    undyne "Stop doing that Papyrus!"
    show undyneImg armor angry flip at fade:
        ypos -0.2
        xpos 0.4
    show papyrusImg sorry zorder 0 at fade:
        xpos -0.1
    papyrus "I'M SORRY"
    show asgoreImg armor joking
    asgore "Calm down everyone"
    asgore "Let's keep moving"
    hide undyneImg
    hide asgoreImg
    hide papyrusImg
    pause(0.8)
    show papyrusImg curious flip zorder 0 at fade:
        xpos 0.4
    papyrus "UH?"
    papyrus "WHAT'S THAT?"
    stop music fadeout 1
    hide papyrusImg
    scene day3 fortress findMauricio frame1 with dissolve
    pause(0.5)
    scene day3 fortress findMauricio frame2 with dissolve
    pause(0.5)
    show papyrusImg worried flip at fade:
        xpos 0.5
    papyrus "HEY... YOU..."
    "Human Kid" "* AAAHHGGG"
    "Human Kid" "* A MONSTER!"
    show papyrusImg proud flip zorder 0 at fade:
        xpos 0.4
    papyrus "YES, A MONSTER!"
    papyrus "WHO CAME TO SAVE YOU FROM THE EVIL..."
    "Human Kid" "* Monsters?"
    show papyrusImg uhh flip
    papyrus "COME AGAIN?"
    "Human Kid" "* A Purple one, like a snake..."
    show papyrusImg uhh
    papyrus "..."
    show papyrusImg proud flip
    papyrus "COME ON HUMAN, I'LL TAKE YOU OUT OF HERE"
    "Human Kid" "* But... my brother..."
    show papyrusImg uhh flip
    papyrus "IS HE HERE?"
    "Human Kid" "* I don't know"
    show papyrusImg proud flip
    papyrus "I'LL LEAVE YOU WITH A GOOD FRIEND OF MINE"
    papyrus "SHE LOVES KIDS"
    hide papyrusImg
    papyrus "I'LL SEARCH FOR YOUR BROTHER AFTER THAT"
    scene black with dissolve
    play music "music/05 Ruins.mp3" fadein 1 fadeout 1
    pause(1)
    scene toriel house with dissolve
    show alphysImg casual noWords zorder 3 at fade:
        xpos -0.15
        ypos -0.2
    alphys "Toriel is not here! She's with Sans at the humans'"
    show papyrusImg surprised flip at fade:
        xpos 0.4 
    show alphysImg casual nostalgic
    papyrus "YOU RIGHT!"
    show papyrusImg surprised happy flip
    papyrus "THEN WE'LL HAVE TO TAKE CARE OF THE HUMAN"
    alphys "Sorry I'm asking, but did you tell Undyne and the King about this?"
    show papyrusImg surprised flip
    papyrus "OOOPPPSSS"
    hide papyrusImg
    show alphysImg casual nostalgic zorder 3 at fade:
        xpos 0.4
        ypos -0.2
    papyrus "I'D BETTER BE GOING!"
    frisk "Don't worry, you'll be fine"
    frisk "They are my friends"
    scene black with dissolve
    stop music fadeout 1
    pause(1)
    scene fortress inside with dissolve
    show papyrusImg screamingCall at fade:
        xpos 0.4
    papyrus "UNDYNE!"
    papyrus "YOUR MAJESTY!"
    show papyrusImg confused flip
    papyrus "WHERE'S EVERYBODY?"
    show coo at fade:
        xpos -0.3
    show cuero at fade:
        xpos -0.1
    "Monster 1" "ARGH!"
    show coo at fade:
        xpos -0.2
    show cuero at fade:
        xpos -0.3
    "Monster 2" "The Skeleton!"
    show papyrusImg angry flip
    papyrus "HEY YOU!"
    papyrus "ARE YOU KIDNAPPING HUMAN KIDS????"
    "Monster 1" "..."
    hide cuero
    hide coo
    show papyrusImg surprised flip
    "Monster 2" "run"
    hide papyrusImg
    play music "music/24 Bonetrousle.mp3" fadeout 1
    papyrus "HEY YOU! WAIT!"
    show day3 fortress persue frame1 with dissolve
    papyrus "EXPLAIN TO ME WHAT ARE YOU DOING?!"
    papyrus "THERE WAS A HUMAN CHILD HERE AND THEY WASN'T HAPPY"
    "Monster 1" "NO, I WILL NOT TELL YOU!"
    show day3 fortress persue frame2 with dissolve
    "Monster 1" "YOU WILL NEVER UNDERSTAND!"
    papyrus "WHAT I HAVE TO UNDERSTAND I'M SO TIRED OF THAT"
    show day3 fortress persue frame3 with dissolve
    pause(2)
    show papyrusImg surprised zorder 2 at fade:
        xpos 0.4
    papyrus "WAIT, WHERE DID THEY GO?!"
    stop music
    show asgoreImg armor menacing zorder 1 at fade:
        xpos 0.0
    asgore "That's also my question"
    show papyrusImg scared
    papyrus "!?"
    jump backNewerHome

label helpthemout:
    play music "music/16 Nyeh Heh Heh!.mp3" fadein(1)
    $ whoRescueMauricio = False
    show papyrusImg explaining zorder 0 at fade:
        xpos -0.2
    papyrus "NOW I THINK ABOUT IT"
    show cuero flip zorder 0 at fade:
        xpos 0.2
    show coo flip zorder 0 at fade:
        xpos 0.5
    "Monster 1 and 2" "* AAAHHHH!!!"
    papyrus "I'LL BETTER GO WITH YOU GUYS'"
    hide papyrusImg
    papyrus "NOBODY KNOWS WHAT COULD HAPPEN IF I LEAVE YOU ALONE IN A PLACE THIS DANGEROUS!"
    show cuero zorder 0 at fade:
        xpos 0.1
    show coo flip zorder 0 at fade:
        xpos 0.4
    "Monster 1" "* (We need to get rid of him)"
    "Monster 2" "* (Yes, but how?)"
    "* MMMMMmmmmm"
    hide cuero
    hide coo
    stop music
    scene black with dissolve
    pause(1)
    play music "music/33 Quiet Water.mp3" fadein(1) fadeout(1) 
    scene day3 forest hanging with dissolve:
        ypos 0.0
        linear 10 ypos -0.7
    pause(1.0)
    papyrus "HOW I LET THIS HAPPEN?"
    papyrus "WELL, AT LEAST THEY PROMISE ME THEY WILL FIND SOME HELP"
    papyrus "BUT IT'S GETTING LATE ALREADY"
    papyrus "MMM..."
    scene day3 forest pickup frame1 with dissolve
    pause(1)
    scene day3 forest pickup frame2 with dissolve
    pause(1)
    scene day3 forest pickup frame3 with hpunch
    pause(1)
    scene day3 forest pickup frame4 with dissolve
    pause(1)
    scene day3 forest pickup frame5 with dissolve
    pause(1)
    scene day3 forest pickup frame6 with dissolve
    pause(1)
    papyrus "THE GREAT PAPYRUS HAS DONE IT AGAIN!"
    papyrus "NOW I NEED TO FIND THOSE MONSTERS"
    papyrus "THEY MUST BE WORRIED SICK I FELL INTO THIS PLACE"
    scene forest with dissolve
    show papyrusImg screamingCall at fade:
        xpos 0.1
    papyrus "HELLOOOOO???"
    papyrus "WHERE ARE YOU GUYS???"
    show papyrusImg worried
    papyrus "MMM...."
    papyrus "HOPEFULLY THEY ARE ALRIGHT"
    scene day3 forest action frame1 with dissolve
    pause(1)
    play music "music/24 Bonetrousle.mp3" fadeout 1 fadein 1
    papyrus "!?"
    scene day3 forest action frame2 with dissolve
    pause(1)
    scene day3 forest action frame3 with dissolve
    pause(1)
    papyrus "A HUMAN?!"
    papyrus "ARE THEY KIDNAPPING A HUMAN CHILD!?"
    papyrus "NOT ON THE WITNESS OF THE GREAT PAPYRUS!"
    scene day3 forest stop frame1 with dissolve
    pause(0.2)
    play sound "music/fx/thump.wav"
    scene day3 forest stop frame2 with hpunch
    pause(0.5)
    papyrus "WRONG MONSTER!"
    papyrus "BUT I CAN STILL FIX THIS!"
    scene day3 forest stop frame1 with dissolve
    play sound "music/fx/spears.wav"
    pause(0.2)
    play sound "music/fx/explosion.wav"
    pause(0.2)
    scene day3 forest spear frame1 with vpunch
    pause(0.5)
    papyrus "UNDYNE?!"
    papyrus "WHAT ARE YOU DOING?!"
    show papyrusImg surprised at fade:
        xpos -0.1
    papyrus "THEY ARE ESCAPING!!!"
    show undyneImg armor angry flip at fade:
        ypos -0.2
        xpos 0.4
    undyne "WHAT ARE YOU DOING YOU IDIOT?!"
    undyne "These monsters has nothing to do with anything!!!!"
    show papyrusImg worried
    papyrus "UNDYNE PLEASE!"
    papyrus "THEY ARE CARRYING A SCARED HUMAN CHILD"
    papyrus "AND THEY ARE RUNNING AWAY FROM US"
    undyne "Because they are smart and trying to get away from the evil humans!"
    papyrus "BUT UNDYNE!"
    papyrus "I'M SURE THE CHILD IS NOT AGREEING WITH THIS!"
    show papyrusImg surprised flip
    papyrus "OH GOD!"
    hide papyrusImg
    papyrus "THE CHILD!"
    show undyneImg armor angry flip at fade:
        ypos -0.2
        xpos 0.0
    undyne "Papyrus wait!"
    show undyneImg armor surprised flip
    undyne "This stupid bonehead is getting away somehow!"
    show asgoreImg armor menacing flip zorder 1 at fade:
        xpos 0.2
    asgore "Leave this to me"
    hide asgoreImg
    undyne "But..."
    play sound "music/fx/spears.wav"
    pause(1)
    scene  day3 forest trident frame1 with hpunch
    play sound "music/fx/explosion.wav"
    pause(0.2)
    scene  day3 forest trident frame2 with vpunch
    stop music    
    play sound "music/fx/thump.wav"
    pause(0.2)
    papyrus "YOUR MAJESTY! PLEASE!"
    papyrus "I NEED TO SAVE THAT CHILD!!"
    asgore "And you need to calm down Papyrus"
    asgore "False accusations go nowhere here"
    asgore "Let's go home"
    scene black with dissolve
    pause(1.0)
    papyrus "THOSE AREN'T..."
    extend " FALSE..."           
    jump backNewerHome

label backNewerHome:
    scene black with dissolve
    play music "music/05 Ruins.mp3" fadein 1 fadeout 1
    pause(1)
    scene toriel house with dissolve
    show torielImg position zorder 2 at fade:
        xpos -0.1
    show sansImg position zorder 4 at fade:
        xpos 0.15
        ypos -0.05
    call sansSuitAnnoyed from _call_sansSuitAnnoyed
    call torielSuitWorried from _call_torielSuitWorried
    sans "what just happened?"
    sans "we were at the middle of a meeting"
    toriel "Hopefully they are already captured the humans"
    show undyneImg armor serious flip zorder 3 at fade:
        ypos -0.2
        xpos 0.3
    undyne "Not really"
    show undyneImg armor serious zorder 3 at fade:
        ypos -0.2
        xpos 0.1
    show asgoreImg armor menacing flip zorder 1 at fade:
        xpos 0.2
    show papyrusImg sorry upsidedown zorder 2 at fade:
        xpos 0.5
    call sansSuitSurprised from _call_sansSuitSurprised
    call torielSuitSuprised from _call_torielSuitSuprised
    papyrus "..."
    hide papyrusImg
    hide asgoreImg
    play sound "music/fx/thump.wav"
    sans "papyrus?"
    sans "what just happened?"
    hide torielImg
    show undyneImg armor serious flip zorder 3 at fade:
        ypos -0.2
        xpos 0.3
    undyne "We found by cheer luck some monsters in the forest"
    undyne "And Papyrus started to attack them with no reason at all"
    show papyrusImg worried flip zorder 2 at fade:
        xpos 0.5
    papyrus "UNDYNE!"
    show undyneImg armor serious
    papyrus "I TOLD YOU THE REASON!"
    show undyneImg armor angry
    show papyrusImg scared flip
    call sansSuitBored from _call_sansSuitBored
    undyne "PAPYRUS SHUT UP"
    show undyneImg armor serious
    show papyrusImg worried
    undyne "THIS IS GETTING WAY OUT OF HAND"
    show undyneImg armor surprised flip
    show torielImg position zorder 2 at fade:
        xpos -0.1
    call torielSuitAngry from _call_torielSuitAngry
    toriel "UNDYNE"
    show undyneImg armor serious flip
    toriel "What do you think you are doing?"
    undyne "It's just..."
    show undyneImg armor serious
    undyne "grrrr...."
    show undyneImg armor serious flip
    undyne "argh"
    call sansSuitSarcastic from _call_sansSuitSarcastic
    sans "what the matter, uh?"
    undyne "Those monsters did nothing"
    asgore "..."
    show undyneImg armor angry flip
    undyne "And he is attacking them"
    show undyneImg armor serious flip
    undyne "This is exactly what I..."
    show undyneImg armor serious
    undyne "grrr...."
    show undyneImg armor serious flip
    sans "exactly you what?"
    show undyneImg armor serious
    call sansSuitAnnoyed from _call_sansSuitAnnoyed_1
    sans "come on, say it!"
    show undyneImg armor serious flip
    undyne "You don't get it"
    dtSans "I'll tell you what I`m getting then"
    dtSans "So maybe you"
    stop music fadeout(1)
    hide papyrusImg
    play sound "music/fx/steps.wav"
    call sansSuitSurprised from _call_sansSuitSurprised_1
    call torielSuitSuprised from _call_torielSuitSuprised_1
    show undyneImg armor surprised
    papyrus "EVERYBODY JUST STOP!"
    papyrus "I CAN`T TAKE THIS ANYMORE!"
    play sound "music/fx/thump.wav"
    call torielSuitWorried from _call_torielSuitWorried_1
    call sansSuitWorried from _call_sansSuitWorried
    show undyneImg armor serious
    show asgoreImg armor awe zorder 1 at fade:
        xpos 0.3
    asgore "Oh no"
    sans "bro..."
    asgore "I'm scared about the same thing, though"
    call sansSuitAnnoyed from _call_sansSuitAnnoyed_2
    sans "what?"
    show asgoreImg armor awe flip
    asgore "Not in the way of he will go out of control again"
    call sansSuitWorried from _call_sansSuitWorried_1
    asgore "But in a way he will start to look too hard trying to fix that mistake"
    undyne "He always tries too hard..."
    undyne "..."
    show undyneImg armor worried
    undyne "And I always thought he will die at the hands to a powerful enemy if I teach him to fight"
    sans "..."
    toriel "Everybody is stressed out, specially him"
    toriel "I think the best we can do is just rest and tomorrow study his accusations"
    toriel "Let`s give him the benefit of the doubt this time"
    scene toriel house with dissolve
    show friskImg worried zorder 3 at fade:
        xpos 0.1
        ypos 0.2
    pause(1)
    hide friskImg
    pause(0.5)
    scene black with dissolve
    play music "music/33 Quiet Water.mp3" fadein(1) fadeout(1) 
    scene day3 nightview background with dissolve:
        ypos 0.0
        linear 20 ypos -0.5
    show day3F nightview foreground at fade
    papyrus "BEEN GREAT IS GETTING MORE DIFFICULT AT THE TIME GOES ON"
    papyrus "I HAVE TO STILL WORK ON IT"
    papyrus "but..."
    papyrus "..."
    papyrus "NO BUTS PAPYRUS, NOT THIS TIME"
    papyrus "THE GREAT PAPYRUS HAS..."
    papyrus "NO."
    papyrus "WILL SOLVE THIS MESS SOMEHOW"
    papyrus "BUT NOW I HAVE TO WORK IN THE HOW"
    papyrus "HOW?"
    papyrus "MMMMMMMMMMMM"
    show friskImg worried zorder 3 at fade:
        xpos 0.1
        ypos 0.2
    papyrus "UH? FRISK?"
    frisk "Hi"
    papyrus "WHAT'S THE MATTER?"
    if whoRescueMauricio:
        frisk "Do you remember the kid you saved?"
        papyrus "OH RIGHT"
        show friskImg affirmation
        frisk "They`re name is Mauricio"
        frisk "They told me they remembered where their sibling is hidden"  
    else:
        frisk "Did you know Dogamy and Dogaressa found a kid in the woods?"
        papyrus "MAYBE IS..."
        papyrus "OK, GO ON"
        frisk "They said they were kidnapped by some humans and then given to some..."
        papyrus "MONSTERS??"
        show friskImg unsure
        frisk "Yes, how to..."
        papyrus "I FOUND THEM IN THE WOODS"
        show friskImg affirmation
        frisk "Well, they said their sibling were also kidnapped"
        frisk "And that maybe they remember where their sibling is"
    show papyrusImg delight flip zorder 2 at fade:
        xpos 0.3
    papyrus "REALLY??"
    papyrus "WOWIE!"
    papyrus "WE SHOULD GO AT ONCE!"
    show friskImg unsure
    frisk "Are you sure?"
    papyrus "YES!"
    hide friskImg
    frisk "Let's me send a text to my mom first"
    show papyrusImg explainingPointing flip
    papyrus "YES YES, YOU SHOULD TELL TORIEL"
    show papyrusImg neutral flip
    papyrus "DONE?"
    show friskImg happy zorder 3 at fade:
        xpos 0.1
        ypos 0.2
    frisk "Done"
    show papyrusImg delight flip
    papyrus "OK!"
    play sound "music/fx/steps.wav"
    hide papyrusImg
    papyrus "TO"
    papyrus "..."
    play sound "music/fx/steps.wav"
    show papyrusImg uhh flip zorder 2 at fade:
        xpos 0.3
    papyrus "TO WHERE?"
    show friskImg affirmation
    frisk "To"
    stop music    
    scene toriel house with dissolve
    show sansImg unsure flip zorder 3 at fade:
        xpos 0.3
        ypos -0.05
    show torielImg pajamas worried zorder 1 at fade
    show asgoreImg cape neutral flip zorder 2 at fade:
        xpos 0.3
        ypos -0.15
    sans "mount anemi"
    sans "that name is kind of weird"
    play music "music/05 Ruins.mp3" fadein 1 fadeout 1
    asgore "It's near from here"
    asgore "I`ll call U..."
    show asgoreImg cape worried flip
    asgore "I`ll go myself to see what`s going on"
    show sansImg angry
    sans "what are you implying?"
    show sansImg unsure
    show asgoreImg cape neutral flip
    asgore "Just that I don`t want for them to get any trouble"
    toriel "That mount is barely on the humans` maps"
    toriel "I texted Alphys about it"
    show sansImg unsure flip
    sans "then is a perfect place for humans doing illegal things"
    show sansImg serious
    sans "ok, let`s go..."
    show sansImg surprised flip
    sans "wait did you texted alphys?"
    toriel "Yes, I just..."
    show torielImg pajamas surprised
    show asgoreImg cape surprised flip
    toriel "Oh uh"
    play music "music/46 Spear of Justice.mp3" fadein 1
    scene toriel house with hpunch
    undyne "AAAAHHHHHHHHHRRRRGGGGGGGGGGG!!!!!"
    undyne "PAPYRUS!!"
    undyne "AT LEAST WAIT UNTIL TOMORROW DAMMIT!!!!"
    show sansImg surprised  zorder 3 at fade:
        xpos 0.3
        ypos -0.05
    show asgoreImg cape surprised zorder 2 at fade:
        xpos 0.3
        ypos -0.15
    asgore "We should go at once"
    hide asgoreImg
    hide sansImg
    sans "Yes, yes"
    stop music fadeout(1)
    scene black with dissolve
    pause(1)
    play music "music/17 Snowy.mp3" fadein(1) fadeout(1)
    scene mountAnemi with dissolve:
        ypos 0.0
        linear 25 ypos -0.4
    pause(1)
    show papyrusImg annoyed zorder 2 at fade:
        xpos -0.1
    show friskImg unsure zorder 3 at fade:
        xpos 0.1
        ypos 0.2
    papyrus "WHERE DID THEY SAID THEIR SIBLING WERE?"
    frisk "In a cave near to where the snow started"
    papyrus "THIS IS CHILLIER THAN HIGH SNOWDIN"
    papyrus "ARE YOU OK FRISK?"
    show friskImg scared
    frisk "..."
    show papyrusImg explaining
    papyrus "HA! I KNEW IT!"
    show papyrusImg neutral
    papyrus "COME ON FRISK, I DON'T HAVE SKIN, I'LL BE OK!"
    papyrus "TAKE MY SCARF"
    show papyrusImg scarfless happy
    show friskImg scarf flip
    frisk "But"
    extend " it's part of your battle body..."
    show friskImg scarf
    papyrus "WHAT`S A BATTLE BODY GOOD FOR IF IT CAN`T HELP MY FRIENDS?"
    show friskImg scarf flip zorder 3 at fade:
        xpos 0.4
        ypos 0.2
    pause(2) 
    hide friskImg
    frisk "Let`s keep moving"
    hide papyrusImg
    papyrus "YES!"
    pause(1)
    show sansImg surprised  zorder 3 at fade:
        xpos 0.3
        ypos -0.05
    sans "they seem to be fine"
    show sansImg unsure
    sans "mmmm"
    sans "i think we`ll be better follow them and see where this goes"
    show sansImg unsure flip
    sans "but this just leave me with"
    sans "mmm"
    hide sansImg
    pause(0.8)
    show sansImg happy flip zorder 3 at fade:
        xpos 0.6
        ypos -0.05
    sans "done"
    hide sansImg
    pause(0.5)
    play music "music/46 Spear of Justice.mp3" fadein 1
    pause(1)
    show undyneImg armor angry zorder 3 at fade:
        ypos -0.2
        xpos 0.0
    undyne "ARGH!"
    undyne "Not Frisk too!!!"
    show undyneImg armor angry zorder 3 at fade:
        ypos -0.2
        xpos 0.3
    undyne "PA..."
    stop music fadeout(1)
    show undyneImg armor surprised
    undyne "!?"
    hide undyneImg
    play sound "music/fx/thump.wav"

    pause(1)
    
    play music "music/15 sans.mp3" fadein 1
    undyne "SANS!"
    undyne "I KNOW THIS IS YOU!"
    show sansImg happy flip zorder 3 at fade:
        xpos 0.6
        ypos -0.05
    sans "i totally forgot about practical jokes"
    sans "i should do this more often"
    show sansImg laughing flip
    sans "ppfff"
    undyne "You..."
    show asgoreImg cape neutral zorder 2 at fade:
        xpos -0.3
        ypos -0.15
    asgore "What`s going..."
    show asgoreImg cape laughing
    asgore "ppfff"
    undyne "Asgore..."
    undyne "Not you too.."
    show asgoreImg cape worried
    asgore "I`m sorry Undyne..."
    asgore "It`s just..."
    show asgoreImg cape laughing
    asgore "Pffff"
    undyne "GET ME OUT GET ME OUT GET ME OUT!"
    stop music fadeout(1)
    hide asgoreImg
    hide sansImg
    scene black with dissolve
    pause(1)
    play music "music/17 Snowy.mp3" fadein(1) fadeout(1)
    scene mountAnemi with dissolve:
        ypos -0.4
    show papyrusImg scarfless unsure zorder 2 at fade:
        xpos -0.1
    show friskImg scarf zorder 3 at fade:
        xpos 0.1
        ypos 0.2
    frisk "LOOK!"
    frisk "A giant hole on the floor!"
    hide papyrusImg
    hide friskImg
    scene day3 kids cave with dissolve:
        xpos -0.2
        ypos 0.0
        linear 24 xpos 0.0 ypos -0.2
    papyrus "LET`S SEE THERE"
    papyrus "HEEEYYYY!!!"
    "Kid 1" "* It`s another monster!"
    "Kid 2" "* Hide! Hide!"
    frisk "It`s ok! Papyrus is my friend!"
    "Kid 3" "* A human?"
    "Kid 1" "* It`s a kid like us!"
    "Kid 2" "* They came to rescue us?"
    papyrus "YES"
    frisk "We came in the name of Mauricio!"
    "Kid 3" "* That`s my brother"
    "Kid 3" "* Is he alright?"
    papyrus "HE`S FINE!"
    papyrus "NOW WE NEED TO GET YOU GUYS OUT OF THERE!"
    scene black with dissolve
    pause(1)
    play music "music/15 sans.mp3" fadein(1) fadeout(1)
    scene mountAnemi with dissolve:
        ypos -0.4
    show sansImg happy zorder 3 at fade:
        xpos 0.2
        ypos -0.05
    show asgoreImg cape neutral zorder 1 at fade:
        xpos -0.3
        ypos -0.15
    asgore "This is a very good trap Sans"
    sans "i actually surprised myself"
    play sound "music/fx/riseup.wav"
    show undyneImg armor angry zorder 2 at fade:
        ypos 0.1
        xpos 0.3
    undyne "ARGH! I got out!"
    show undyneImg armor angry flip:
        ypos -0.2
    undyne "I`ll talk with you later punk!"
    show sansImg happy
    show asgoreImg cape neutral
    sans "look at me i`m so scared"
    show undyneImg armor angry
    undyne "Now I will"
    show papyrusImg topless angry flip zorder 1 at fade:
        xpos 0.5
    papyrus "WHAT ARE YOU DOING HERE PLAYING IN THE DIRT?"
    show undyneImg armor surprised
    show sansImg surprised
    show asgoreImg cape surprised
    undyne "ARGH! PAPYRUS!"
    undyne "How you..."
    papyrus "CAN WE LEAVE THIS FOR LATER?"
    show papyrusImg topless angry
    papyrus "FRISK AND I FOUND 5 KIDNAPPED KIDS IN A CAVE"
    show papyrusImg topless angry flip
    papyrus "THEY ARE FREEZING AND I`M RUNNING OUT OF CLOTHES"
    asgore "Five?!"
    hide asgoreImg
    show sansImg happy
    sans "well, i got my jacket"
    hide sansImg
    show undyneImg armor sorry
    undyne "Papyrus... I..."
    papyrus "I TOLD YOU, WE BETTER LEAVE THIS FOR LATER"
    papyrus "I`M FINE"
    hide papyrusImg
    papyrus "THOSE KIDS ARE MORE IMPORTANT"
    show undyneImg armor smile
    undyne "Heh..."
    hide undyneImg
    undyne "You right..."
    stop music fadeout(1)
    label endOfDay3:
        if resets > 0:
            call questionsEnd from _call_questionsEnd_1
        jump day4
return



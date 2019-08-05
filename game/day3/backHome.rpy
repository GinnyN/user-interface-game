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
    return
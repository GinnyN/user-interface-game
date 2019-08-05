
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
    return
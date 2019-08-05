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
    return
label prisonPapyrusEnding:
    play music "music/05 Ruins.mp3" fadein 1 fadeout 1
    pause(1)
    scene toriel house with dissolve
    show friskImg future happy flip zorder 3 at fade:
        xpos 0.0
        ypos 0.13
    frisk "PAPYRUS COMES BACK TODAY!"
    hide friskImg
    show torielImg teacher neutral flip zorder 2 at fade:
        xpos 0.3
    toriel "I haven't saw them this happy since..."
    toriel "Since about 5 years ago..."
    show sansImg future neutral flip zorder 9 at fade with dissolve:
        xpos 0.3
    sans "i'm also quite happy"
    toriel "Well, yes"
    toriel "Who isn't?"
    toriel "Everything has become so quiet since he was gone"
    show sansImg future neutral
    sans "we need his singing during his morning run to wake up"
    show torielImg teacher happy flip
    toriel "I had to put my alarm after he surrended to the humans"
    sans "i always found that kind of annoying but it was so sad the first time i expected it and it never came..."
    frisk "PAPYRUS IS GOING TO BE SO DISSAPOINTED ON YOU TWO!"
    show torielImg teacher angry flip
    toriel "From where that came from?"
    show sansImg future neutral flip
    sans "i'm pretty sure he's expecting to be dissapointed"
    show torielImg teacher worried flip
    toriel "Sans.."
    undyne "WE HERE!!"
    hide torielImg
    hide sansImg
    frisk "THEY ARE HERE!!!"
    show papyrusImg future neutral zorder 3 at fade with dissolve
    papyrus "WHOA... IT'S LIKE THIS HAS NEVER..."
    play sound "music/fx/spears.wav"
    scene papyrusPrison frame1 with hpunch
    pause(0.5)
    play sound "music/fx/thump.wav"
    scene toriel house with vpunch
    play music "music/16 Nyeh Heh Heh!.mp3" fadein(1) fadeout(1)
    show friskImg future happy flip zorder 3 at fade:
        xpos 0.3
        ypos 0.13
    show papyrusImg future surprised zorder 2 at fade with dissolve:
        xpos -0.1
    papyrus "YOU ARE SO BIG!"
    papyrus "OH GOD, YOU ARE SO BIG!"
    papyrus "HUMANS GROW UP TOO FAST!"
    papyrus "WHEN THIS STOPS CHANGING!"
    show sansImg future neutral flip zorder 9 at fade with dissolve:
        xpos 0.6
    sans "i heard they peak around 25 and stay mostly the same until around 40"
    papyrus "WHY DO YOU CHANGE SO MUCH?!"
    show friskImg future angry flip
    frisk "You don't go away for so long!"
    show papyrusImg future sad
    papyrus "WELL..."
    papyrus "YOU HAVE A POINT..."
    papyrus "BUT, I HAD TO"
    show papyrusImg future decisive
    papyrus "THOSE ARE THE MISTAKES WHICH SHOULD NOT AVOID PUNISHMENT!"
    frisk "I know"
    frisk "But I don't like it"
    show papyrusImg future neutral
    papyrus "WELL, I CANNOT MOVE OUT OF THE MONSTER KINGDOM FOR AROUND 10 YEARS ANYWAYS"
    papyrus "I GUESS WE'LL HAVE TIME"
    show friskImg future happy flip
    frisk "Yes!"
    frisk "And we're going to start..."
    show friskImg future dissapointed flip
    extend " tomorrow"
    frisk "Because they told me you need to rest today"
    show papyrusImg future well
    papyrus "YEEEAAAAAHHHHHHH...."
    papyrus "I TOTALLY NEED TO REST"
    toriel "Frisk!"
    show friskImg future angry
    frisk "What?"
    scene black with dissolve
    pause(4)
    stop music fadeout(3)
    scene skelebrosHouse papyrus room with dissolve
    show undyneImg future neutral zorder 2 at fade with dissolve:
        ypos -0.2
        xpos 0.0
    show papyrusImg future neutral zorder 2 at fade with dissolve:
        xpos 0.3
    undyne "Alphys and I clean up this place 2 days ago"
    undyne "We didn't throw away anything, so, all your junk is still there"
    show papyrusImg future well
    papyrus "AH..."
    show papyrusImg future neutral flip
    papyrus "THANKS YOU"
    hide undyneImg
    undyne "Remember! We have a party tomorrow!"
    undyne "Do not run away with Frisk today for too long!"
    hide papyrusImg
    papyrus "LET'S SEE EVERYTHING IS IN ORDER..."
    if giveRingToUndyne:
        show papyrusImg future well zorder 2 at fade with dissolve:
            xpos 0.3
        papyrus "OH... THIS CLOTHES ARE SO OLD..."
        papyrus "MY SCARF IS JUST RUINED"
    else:
        papyrus "LET'S CHECK SOMETHING"
        papyrus "OH, STILL HERE..."
        papyrus "..."
        show papyrusImg future frustrated zorder 2 at fade with dissolve:
            xpos 0.3
        papyrus "WHAT I'M GOING TO DO WITH THIS?"
    
    show sansImg future neutral zorder 9 at fade with dissolve:
        xpos 0.1
    sans "how's everything bro?"
    show papyrusImg future surprised
    papyrus "ARGH!"
    show papyrusImg future neutral flip
    papyrus "FINE FINE"
    hide papyrusImg
    papyrus "ALL MY CLOTHES FEEL SO OLD! THIS NEEDS LAUNDRY"
    papyrus "..."
    show papyrusImg future neutral flip zorder 2 at fade with dissolve:
        xpos 0.3
    papyrus "IS THERE SOMETHING YOU NEED TO TELL ME?"
    sans "yeah, well"
    show sansImg future careful
    sans "i could have got you out 2 months after you surrended to the humans"
    show papyrusImg future well flip
    papyrus "I WOULD NOT HAVE LIKE THAT"
    sans "i know"
    show papyrusImg future sad flip
    play music "music/05 Ruins.mp3" fadein 1 fadeout 1
    papyrus "UH?"
    sans "i explained that to asgore and toriel, but they made the point humans live, well, very little"
    show papyrusImg future sad
    papyrus "..."
    show papyrusImg future well flip
    papyrus "I DIDN'T KNEW THAT"
    sans "i assumed you didn't"
    show papyrusImg future well
    papyrus "..."
    papyrus "I HAVE ALSO SOMETHING TO TELL YOU..."
    show papyrusImg future well flip
    papyrus "AND TO SHOW YOU..."
    hide papyrusImg
    papyrus "DO YOU REMEMBER AN OLD SKELETON CALLED W.D. GASTER?"
    hide sansImg
    sans "how... how do you know about him?"
    papyrus "WELL..."
    scene black with dissolve
    "..."
    "I'M SORRY"
    "IT'S SEEMS THE TIME JUMP WAS VERY COSTLY"
    "OR MAYBE NOT"
    "BUT IT'S ALL I CAN SHOW YOU"
    "THANKS FOR BELIEVING IN HIM"
    "I REALLY DON'T KNOW IF WE'LL SEE EACH OTHER AGAIN"
    "BUT I HOPE YOU CAN MOVE FORWARD AS WELL"
    "GOOD BYE"
    nvl clear
    ""
    stop music fadeout(1)
    pause(1.5)
    # $ renpy.set_return_stack([])
    $ renpy.quit()
return
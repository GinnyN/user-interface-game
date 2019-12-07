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
    scene papyrusPrison frame1 with hpunch
    pause(0.5)
    scene toriel house with vpunch
    show friskImg future happy flip zorder 3 at fade:
        xpos 0.3
        ypos 0.13
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
    papyrus "WELL..."
    papyrus "YOU HAVE A POINT..."
    papyrus "BUT, I HAD TO"
    papyrus "THOSE ARE THE MISTAKES WHICH SHOULD NOT AVOID PUNISHMENT!"
    frisk "I know"
    frisk "But I don't like it"
    papyrus "WELL, I CANNOT MOVE OUT OF THE MONSTER KINGDOM FOR AROUND 10 YEARS ANYWAYS"
    papyrus "I GUESS WE'LL HAVE TIME"
    show friskImg future happy flip
    frisk "Yes!"
    frisk "And we're going to start..."
    extend " tomorrow"
    frisk "Because they told me you need to rest today"
    papyrus "YEEEAAAAAHHHHHHH...."
    papyrus "I TOTALLY NEED TO REST"
    toriel "Frisk!"
    frisk "What?"
    "* Scene changes to Undyne and Papyrus at Papyrus' room *"
    undyne "Alphys and I clean up this place 2 days ago"
    undyne "We didn't throw away anything, so, all your junk is still there"
    papyrus "AH..."
    papyrus "THANKS YOU"
    undyne "Remember! We have a party tomorrow!"
    undyne "Do not run away with Frisk today for too long!"
    papyrus "LET'S SEE EVERYTHING IS IN ORDER..."
    if giveRingToUndyne:
        papyrus "OH... THIS CLOTHES ARE SO OLD..."
        papyrus "MY SCARF IS JUST RUINED"
    else:
        papyrus "LET'S CHECK SOMETHING"
        papyrus "OH, STILL HERE..."
        papyrus "..."
        papyrus "WHAT I'M GOING TO DO WITH THIS?"
    sans "how's everything bro?"
    papyrus "ARGH!"
    papyrus "FINE FINE"
    papyrus "ALL MY CLOTHES FEEL SO OLD! THIS NEEDS LAUNDRY"
    papyrus "..."
    papyrus "IS THERE SOMETHING YOU NEED TO TELL ME?"
    sans "yeah, well" 
    sans "i could have got you out 2 months after you surrended to the humans"
    papyrus "I WOULD NOT HAVE LIKE THAT"
    sans "i know"
    papyrus "UH?"
    sans "i explained that to asgore and toriel, but they made the point humans live, well, very little"
    papyrus "..."
    papyrus "I DIDN'T KNEW THAT"
    sans "i assumed you didn't"
    papyrus "..."
    papyrus "I HAVE ALSO SOMETHING TO TELL YOU..."
    papyrus "AND TO SHOW YOU..."
    papyrus "DO YOU REMEMBER AN OLD SKELETON CALLED W.D. GASTER?"
    sans "how... how do you know about him?"
    papyrus "WELL..."
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
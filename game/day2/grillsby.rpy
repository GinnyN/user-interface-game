label day2grillsby:
    scene black with dissolve
    play sound "music/fx/steps.wav"
    pause(1.0)
    play music "music/15 sans.mp3" fadein 1 fadeout 1
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
    return
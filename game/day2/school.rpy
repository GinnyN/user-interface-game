label sansMeetUndyne:
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
    return

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
    return

label honor:
    papyrus "THIS IS FOR MY OWN GREATNESS SANS!"
    sans "you don't have anything to prove to undyne, really"
    show papyrusImg confused flip
    papyrus "WHO SAID ANYTHING ABOUT HER?!"
    show papyrusImg angry flip
    papyrus "THIS IS FOR ME!"
    papyrus "I NEED TO GO BACK TO BE AS GREAT AS I CAN BE!"
    sans "papyrus, please.."
    return

label stuborn:
    papyrus "DON'T GET IN THE WAY SANS!"
    papyrus "THIS IS *MY* PROBLEM!"
    sans "i understand the feeling"
    sans "but toriel told you, it's not anymore"
    papyrus "BUT IT'S STILL MY FAULT"
    papyrus "*I* HAVE TO SOLVE IT!"
    sans ".."
    return
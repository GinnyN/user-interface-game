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
    return

label jumpBuilding:
    undyne "We're going in!"
    hide undyneImg
    papyrus "WAIT FOR US FRISK!"
    hide papyrusImg
    sans "you go that way"
    sans "i'll use a shortcut"
    hide sansImg
    stop music fadeout 1
    pause(0.4)

label insideBuilding:
    scene black with dissolve
    scene day1 scene2 with dissolve:
        xalign 0.0
        linear 5 xalign 0.7
    play music "music/47 Ooo.mp3" fadein 1
    pause (0.4)
    show papyrusImg screamingCall zorder 0 at fade:
        xpos -0.2
    papyrus "FRISK!?"
    show undyneImg explaining zorder 1 at fade:
        xpos 0.2
        ypos -0.2
    show papyrusImg scared
    undyne "shhh..."
    show papyrusImg nervious
    show undyneImg explaining flip
    undyne "shut up Papyrus"
    undyne "They can hear us"
    undyne "And this are humans what we're talking about"
    papyrus "YOU RIGHT..."
    papyrus "I'M SORRY"
    show goon1 flip zorder 0 at fade:
        xpos 0.5
    show papyrusImg scared
    papyrus "A HUMAN!"
    hide goon1
    show undyneImg angry
    undyne "AFTER THEM!"
    scene day1 scene3 with dissolve
    pause(0.5)
    show goon1 zorder 0 at fade:
        yalign 1.0 xalign 0
    "Random Goon" "* BOSS! BOSS!"
    show goon2 flip zorder 3 at fade:
        yalign 1.0 xalign 0.9
    "Boss" "* What is happening?"
    "Random Goon" "* Monsters! They are attacking us!"
    "Boss" "* What?!"
    show goon3 flip zorder 2 at fade:
        xpos 0.5
    "Random Goon 2" "* I heard they use magic to attack directly to our souls!"
    "Random Goon" "* What are we going to do?"
    show sansImg cocky zorder 5 at fade:
        yalign 1.0 xalign 0.0
    sans "return the kid of course."
    show goon1 flip zorder 0 at fade:
        yalign 1.0 xalign 1.3
    "Boss" "* Who are you?"
    sans "a monster."
    sans "and that kid you just kidnapped is my friend."
    sans "and also those other guys friend."
    sans "you better return them or else..."
    show sansImg cockyEyes
    sans "{font=fonts/DTM-Sans.otf}You are going to have a bad time{/font}"
    show sansImg cocky
    "Boss" "* And what you can do that can hurt us?!"
    stop music fadeout 0.5
    pause(0.5)
    play sound "music/fx/spears.wav"
    pause(0.5)
    play sound "music/fx/explosion.wav"
    pause(0.5)
    play music "music/46 Spear of Justice.mp3" fadein 1
    show undyneImg angry zorder 3 at fade:
        xpos 0.1 
        ypos -0.2
    show papyrusImg angry zorder 4 at fade:
        xpos -0.2
    undyne "I'll throw a flurry of spears which will cut your soul in 1000 pieces!"
    undyne "And then I'll make sphagetti sauce with it!"
    papyrus "YOU BETTER TELL US WHERE'S FRISK!"
    papyrus "BECAUSE UNDYNE IS ONE OF THE STRONGEST MONSTERS FROM OUR KINGDOM!"
    undyne "And I'll make sure"
    undyne "TO MAKE A DELICIOUS SPHAGETTI SAUCE WITH YOUR REMAINS!"
    show papyrusImg uhh
    papyrus "..."
    show papyrusImg angry
    papyrus "AND I'LL HELP!"
    hide goon3
    hide goon1
    show goon2 flip zorder 3 at fade:
        xpos 1.3
    "* AAhhhh!!"
    play sound "music/fx/carstarting.wav"
    pause(0.5)
    show goon2 flip zorder 3 at fade:
        xpos 1.1
    show sansImg surprised at fade
    show papyrusImg surprised at fade
    show undyneImg surprised at fade
    "Boss" "* Too late monsters"
    "Boss" "* The kid has already been shipped to our clients"
    show papyrusImg angry at fade
    papyrus "SHIPPED?"
    show sansImg serious
    sans "they's in a car leaving the building."
    sans "it's not too late if we move fast."
    show undyneImg angry at fade
    undyne "Leave it to me!"
    hide undyneImg
    pause(0.5)
    papyrus "DO YOU SELL YOUR OWN SPECIES!?!"
    show sansImg surprised
    sans "papyrus?"
    sans "bro?"
    papyrus "YOU WERE SELLING MY BEST FRIEND?!"
    sans "you shouldn't be..."
    sans "are you..."
    papyrus "..."
    sans "bro?"
    stop music
    papyrus "run."
    sans "!"
    scene day1 scene4 with dissolve
    show undyneImg happy zorder 2 at fade:
        xalign 0.9 ypos -0.2
    show friskImg happy flip zorder 3 at fade:
        xpos 0.6 ypos 0.1
    undyne "There you are Frisk!"
    undyne "We will make sure this humans will learn their lesson!"
    undyne "We were so worried about you!"
    show sansImg surprised flip zorder 3 at fade:
        xalign 0.6 yalign 1.0
    show undyneImg mild surprise flip
    show friskImg surprised flip
    undyne "Sans?"
    undyne "Where's"
    sans "he told me to..."
    play sound "music/fx/quake.wav"
    pause(0.5)
    play music "music/97 But the Earth Refused to Die.mp3" fadein 1 fadeout 1
    scene day1 scene5 with dissolve
    pause(2)
    show sansImg surprised flip zorder 3 at fade:
        xalign 0.6 yalign 1.0
    show undyneImg surprised flip zorder 2 at fade:
        xalign 0.9 ypos -0.2
    show friskImg worried flip zorder 3 at fade:
        xpos 0.6 ypos 0.1
    sans "he told me to run"
    undyne "What are you doing Papyrus?"
    frisk "!!!"
    dtSans "{cps=*0.2}I don't think he knows..{/cps}"
    hide sansImg
    hide undyneImg
    scene day1 scene6 with dissolve
    pause(1)
    stop music fadeout 1
    pause(1.5)
    play sound "music/fx/soulShatter.wav"
    scene mistColor with dissolve
    pause(1)
    show papyrusImg uhh flip at fade:
        yalign 1.0 xalign 0.7
    papyrus "WHAT..."
    papyrus "DID I JUST DID?"
    stop music fadeout 1
    hide papyrusImg

    return

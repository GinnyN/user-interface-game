label day1:
    $ helpedToriel = False
    scene day1 scene1 with dissolve:
        yalign 0.1
        linear 5 yalign 0.7

    play music "music/83 Here We Are.mp3" fadein 1
    pause(1.0)
    show papyrusImg serious zorder 0 at fade:
        xalign 0.1 yalign 1.1
    papyrus "ARE YOU SURE THIS IS THE PLACE SANS?"
    show sansImg serious zorder 2 at fade:
        xalign 0.3 yalign 1.1 # moveinleft:
    sans "yes, this must be."
    show undyneImg angry zorder 1 at fade:
        xalign 0.5 yalign 1.1 #, hideRight(0.5,1.1) # moveinleft:
    undyne "humans! How they dare!"
    undyne "We offered our hospitality and this is how they paid us?!"
    show papyrusImg explaining
    papyrus "REMEMBER UNDYNE THAT NOT ALL THE HUMANS..."
    show undyneImg angry flip at fade:
        xalign 0.8 yalign 1.1
    show papyrusImg scared
    undyne "SAY THAT TO TORIEL!"
    show papyrusImg nervious
    undyne "This is basically her fault!"
    sans "this is nobody's fault. we should instead focusing in our mission."
    show sansImg flustered
    show undyneImg troll flip
    undyne "And since when you speak your mind this way?"
    show papyrusImg explaining
    papyrus "YOU WERE BAD MOUTHING HIS GIRLFRIEND"
    show papyrusImg scared
    show sansImg flustered screaming
    sans "SHE'S NOT MY GIRLFRIEND"
    show sansImg serious
    show papyrusImg nervious
    sans "besides, this is no time for that"
    show papyrusImg serious
    show undyneImg serious flip
    undyne "You're right... this is a rescue mission"
    show undyneImg angry
    undyne "We have to rescue Frisk!"

    menu:
        "Jump to the Building":
            jump jumpBuilding
        "Ahh??!!" if resets > 0:
            jump titleScreen
        #"Ask Sans about creating a Shortcut" if doors:
        #    jump shortcut

label jumpBuilding:
    show papyrusImg decisive at fade:
        xalign 0.4
    undyne "We're going in!"
    papyrus "WAIT FOR US FRISK!"
    hide papyrusImg
    hide undyneImg
    sans "you go that way"
    sans "i'll use a shortcut"
    hide sansImg
    stop music fadeout 1
    pause(0.4)

label insideBuilding:
    scene day1 scene2 with dissolve:
        xalign 0.0
        linear 5 xalign 0.7
    play music "music/47 Ooo.mp3" fadein 1
    pause (0.4)
    show papyrusImg screamingCall zorder 0 at fade:
        xalign 0.05 yalign 1.1
    papyrus "FRISK!?"
    show undyneImg explaining zorder 1 at fade:
        xalign 0.3 yalign 1.1
    show papyrusImg scared
    undyne "shhh..."
    show papyrusImg nervious
    show undyneImg explaining flip zorder 1 at fade:
        xalign 0.3 yalign 1.1
    undyne "shut up Papyrus"
    undyne "They can hear us"
    undyne "And this are humans what we're talking about"
    papyrus "YOU RIGHT..."
    papyrus "I'M SORRY"
    show goon1 flip zorder 0 at fade:
        yalign 1.0 xalign 1.0
    show papyrusImg surprised pointing
    papyrus "A HUMAN!"
    hide goon1
    show undyneImg angry
    undyne "AFTER THEM!"

label bossOffice:
    scene day1 scene3 with dissolve
    pause(0.5)
    show goon1 zorder 0 at fade:
        yalign 1.0 xalign 0
    "Random Goon" "* BOSS! BOSS!"
    show goon2 flip zorder 3 at fade:
        yalign 1.0 xalign 0.8
    "Boss" "* What is happening?"
    "Random Goon" "* Monsters! They are attacking us!"
    "Boss" "* What?!"
    show goon3 flip zorder 2 at fade:
        yalign 1.0 xalign 1.0
    "Random Goon 2" "* I heard they use magic to attack directly to our souls!"
    "Random Goon" "* What are we going to do?"
    show sansImg cocky zorder 3 at fade:
        yalign 1.0 xalign 0.2
    sans "return the kid of course."
    show goon1 flip zorder 0 at fade:
        yalign 1.0 xalign 0.7
    "Boss" "* Who are you?"
    sans "a monster."
    sans "and that kid you just kidnapped is my friend."
    sans "and also those other guys friend."
    sans "you better return them or else..."
    show sansImg cocky eyes zorder 3 at fade
    sans "{font=fonts/DTM-Sans.otf}You are going to have a bad time{/font}"
    show sansImg cocky zorder 3 at fade
    "Boss" "And what you can do that can hurt us?!"
    stop music fadeout 0.5
    pause(0.5)
    play sound "music/fx/spears.wav"
    pause(0.5)
    play sound "music/fx/explosion.wav"
    pause(0.5)
    play music "music/46 Spear of Justice.mp3" fadein 1
    show undyneImg angry zorder 1 at fade:
        xalign 0.3 yalign 1.0
    show papyrusImg decisive zorder 0 at fade:
        yalign 1.0 xalign 0.0
    undyne "I'll throw a flurry of spears which will cut your soul in 1000 pieces!"
    undyne "And then I'll make sphagetti sauce with it!"
    papyrus "YOU BETTER TELL US WHERE'S FRISK!"
    papyrus "BECAUSE UNDYNE IS ONE OF THE STRONGEST MONSTERS FROM OUR KINGDOM!"
    undyne "And I'll make sure"
    undyne "TO MAKE A DELICIOUS SPHAGETTI SAUCE WITH YOUR REMAINS!"
    show papyrusImg uhh
    papyrus "..."
    show papyrusImg decisive
    papyrus "AND I'LL HELP!"
    show goon3 flip zorder 2 at fade:
        yalign 1.0 xalign 1.1
    show goon1 flip zorder 0 at fade:
        yalign 1.0 xalign 0.9
    show goon2 flip zorder 3 at fade:
        yalign 1.0 xalign 1.0
    "AAhhhh!!"
    play sound "music/fx/carstarting.wav"
    pause(0.5)
    show goon2 flip zorder 3 at fade:
        yalign 1.0 xalign 0.8
    show sansImg serious looking up at fade
    show papyrusImg surprised up at fade
    show undyneImg looking up at fade
    "Boss" "* Too late monsters"
    "Boss" "* The kid has already been shipped to our clients"
    show papyrusImg angry at fade
    papyrus "SHIPPED?"
    show sansImg serious zorder 3 at fade
    sans "they's in a car leaving the building."
    sans "it's not too late if we move fast."
    show undyneImg angry at fade
    undyne "Leave it to me!"
    hide undyneImg

    $ time = resets + papyrusTraining
    $ timer_range = resets + papyrusTraining
    $ timer_jump = 'papyrusAngry'

    if time > 1:
        show screen countdown

        menu:
            "Calm Down":
                hide screen countdown
                jump papyrusCalmedDown

    else:
        jump papyrusAngry

label papyrusAngry:
    papyrus "DO YOU SELL YOUR OWN SPECIES!?!"
    show sansImg surprised zorder 3 at fade
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
    hide sansImg
    hide papyrusImg
    hide goon1
    hide goon2
    hide goon3

#label outside:
    scene day1 scene4 with dissolve
    show undyneImg frisk happy zorder 2 at fade:
        xalign 0.9 yalign 1.0
    undyne "There you are Frisk!"
    show undyneImg frisk hug zorder 2 at fade
    undyne "We will make sure this humans will learn their lesson!"
    undyne "We were so worried about you!"
    show sansImg surprised flip zorder 3 at fade:
        xalign 0.6 yalign 1.0
    show undyneImg frisk surprised flip at fade
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
    show undyneImg frisk confused flip zorder 2 at fade:
        xalign 0.9 yalign 1.0
    sans "run."
    undyne "What are you doing Papyrus?"
    frisk "!!!"
    sans "{font=fonts/DTM-Sans.otf}I don't think he knows...{/font}"
    hide sansImg
    hide undyneImg
    scene day1 scene6 with dissolve
    pause(1)
    stop music fadeout 1
    pause(1.5)
    play sound "music/fx/soulShatter.wav"
    scene black with dissolve
    pause(1)
    show papyrusImg uhh flip at fade:
        yalign 1.0 xalign 0.7
    papyrus "WHAT..."
    papyrus "DID I JUST DID?"
    stop music fadeout 1
    hide papyrusImg

#label reunionRoomDay1:
    scene newerHome night with dissolve:
        xalign 0.3
        linear 5 xalign 0.8
    play music "music/05 Ruins.mp3" fadein 1 fadeout 1
    pause(1)
    scene toriel house with dissolve
    pause(0.5)
    show torielImg pajamas worried surprised zorder 1 at fade:
        xalign 0.1 yalign 1.0
    toriel "Human Traffickers??"
    show torielImg pajamas worried at fade
    show alphysImg pajamas reading flip zorder 4 at fade:
        xalign 0.6 yalign 1.0
    alphys "Exactly."
    show alphysImg pajamas sad flip at fade
    alphys "It's a kind of slavery the humans use to do"
    alphys "It's illegal right now, but that doesn't stop some humans to try out"
    alphys "It's pretty sad indeed"
    show friskImg worried zorder 5 at fade:
        xalign 0.2 yalign 1.0
    toriel "My poor child, I'm sorry you had to go thru this mess"
    show undyneImg bored flip zorder 1 at fade:
        xalign 0.8 yalign 1.0
    undyne "At least those were evil humans"
    show torielImg pajamas angry at fade
    toriel "Undyne! Please!"
    show undyneImg bored explaining flip at fade
    undyne "I'm saying that what Papyrus did they have it coming!"
    show undyneImg bored flip at fade
    undyne "Nobody goes and sell my friend to anyone!"
    toriel "That's still too much Undyne"
    toriel "It's not even allowed on our rules"
    show alphysImg pajamas explaining flip at fade
    alphys "Well... we don't have a rule about commercialisation of slaves"
    show alphysImg pajamas sad flip at fade
    undyne "And if it's were me"
    show undyneImg laugh flip at fade
    undyne "THEY WOULD BE DEAD ANYWAY"
    show torielImg pajamas worried at fade
    show undyneImg bored flip at fade
    toriel "But at least they would have a trial"
    toriel "They are humans, like Frisk"
    toriel "Sadly"
    frisk "But where`s Papyrus?"
    show torielImg pajamas worried surprised zorder 1 at fade
    toriel "Yes, that's right!"
    show torielImg pajamas worried at fade
    toriel "Where's he?"
    show sansImg hoddie worried flip zorder 3 at fade:
        xalign 1.0 yalign 1.0
    sans "he's outside"
    sans "he's too embarrased to go in"
    show undyneImg mild surprise flip at fade
    undyne "Whoa"
    show undyneImg laugh flip at fade
    undyne "And he's the guy who likes to use those socks"
    show undyneImg troll flip at fade
    toriel "Tell him I want to talk with him"
    sans "are you sure?"
    toriel "Alone"
    sans "k then"
    hide sansImg
    show alphysImg pajamas sad flip zorder 3 at fade:
        xalign 1.0 yalign 1.0
    alphys "Hopefully everything is going to be alright"
    hide alphysImg
    show friskImg ilu flip zorder 3 at fade:
        xalign 1.0 yalign 1.0
    frisk "Good luck"
    hide friskImg
    show undyneImg bored flip at fade
    undyne "I still don't see the problem"
    undyne "But, ok, I guess"
    show torielImg pajamas worried at fade
    toriel "Undyne"
    toriel "Please call Asgore"
    show undyneImg mild surprise flip at fade
    undyne "Are you sure?"
    toriel "For much I dislike him, he's still the king"
    show torielImg pajamas solemn at fade
    toriel "And probably you cannot see it yet, but this can cause big problems"
    show torielImg pajamas worried at fade
    toriel "At least we have to let him know"
    undyne "Ok"
    hide undyneImg
    stop music fadeout 1
    play music "music/12 Home.mp3" fadein 1 fadeout 1
    pause(1.0)
    show papyrusImg worried flip zorder 5 at fade:
        yalign 1.0 xalign 0.8
    papyrus "MISS TORIEL"
    show torielImg pajamas embarrased at fade
    toriel "You don't have to call me that"
    show papyrusImg nervious flip at fade

    menu:
        "Toriel, I... I...":
        #   $ day2 = False
            jump tryToExplain
        "But First":
        #   $ day2 = False
            jump thanks
        "Be Quiet":
        #   $ day2 = False
            jump beQuiet
        #"Explain your Idea" if idea:
        #   $ day2 = True
        #   jump idea

label tryToExplain:
    show papyrusImg worried flip zorder 5 at fade
    show torielImg pajamas worried at fade
    papyrus "IT'S JUST"
    papyrus "I REALLY DON'T UNDERSTAND"
    papyrus "IT WAS SUPER DIFFICULT TO CONTROL"
    papyrus "THEY WERE DOING SOMETHING HORRIBLE"
    papyrus "AND SUDDENLY BECAME SOMETHING WORSE"
    papyrus "AND THEN..."
    show papyrusImg scared flip at fade
    papyrus "I WHISPERED! I NEVER DO THAT!"
    show papyrusImg surprised pointing flip at fade
    papyrus "AND THEN I DID THE MOST AMAZING ATTACK EVER"
    show papyrusImg worried flip at fade
    papyrus "BUT I COULDN'T CONTROL IT"
    show torielImg pajamas embarrased at fade
    toriel "You were angry Papyrus"
    toriel "A kind of primal anger when someone you love was in danger"
    papyrus "BUT FRISK WAS IN DANGER BEFORE THAT"
    toriel "They were also doing something unspeakeable"
    show torielImg pajamas solemn at fade
    toriel "I would felt anger too"
    show papyrusImg surprised happy flip at fade
    papyrus "REALLY?!"
    show torielImg pajamas compasionate at fade
    show papyrusImg worried flip at fade
    toriel "But"
    toriel "We need to control our emotions Papyrus"
    toriel "After all"
    toriel "My relation with Asgore ended"
    toriel "With a declaration made out with anger"
    papyrus "..."
    jump torielsAdvice

label thanks:
    show papyrusImg solemn flip at fade
    papyrus "BEFORE EVERYTHING"
    show torielImg worried at fade
    toriel "?"
    show papyrusImg worried flip at fade
    papyrus "I WANT TO THANKS YOU WITH WHAT ARE YOU DOING WITH SANS"
    toriel "What are you talking about?"
    papyrus "HE'S GETTING SO MUCH BETTER FROM HIS..."
    papyrus "'LAZINESS'"
    show torielImg pajamas compasionate at fade
    toriel "Oh, Papyrus"
    show papyrusImg solemn flip at fade
    papyrus "AND IT'S ALL THANKS TO YOU"
    show papyrusImg happy flip at fade
    papyrus "HE WAS TRYING TO DO THAT SUGARY QUICHES A BIT MORE"
    toriel "Pies"
    show papyrusImg nervious flip at fade
    papyrus "YES, YES..."
    show papyrusImg happy flip at fade
    papyrus "AND HE'S NOT GOING THAT MUCH TO GRILLBY'S TO DRINK"
    papyrus "NOW I'M HAVE TO GO AND PICK HIM UP TWO TIMES A WEEK INSTEAD OF EVERYDAY"
    show papyrusImg solemn flip at fade
    papyrus "IT'S ALL THANKS TO YOU"
    toriel "Please Papyrus"
    papyrus "YOU HAVE BEEN A BETTER FRIEND TO HIM THAN I EVER WAS"
    show papyrusImg nervious flip at fade
    papyrus "IT'S KIND OF EMBARRASING HAVING TO ADMIT THAT I WASN'T THAT GREAT ON THAT"
    show papyrusImg worried flip at fade
    toriel "Papyrus"
    toriel "Sans always talk very highly of you"
    toriel "On how you still had hope on him"
    toriel "Even if he didn't have"
    toriel "So, maybe he needed two friends who believed that"
    papyrus "THEN"
    show papyrusImg embarrased happy flip at fade
    papyrus "THANKS FOR BEEN THAT OTHER FRIEND"
    show torielImg pajamas happy at fade
    toriel "It's a pleasure"
    if resets < 3 and resets > 1:
        show torielImg worried at fade
        toriel "..."
        show papyrusImg worried flip at fade
        papyrus "..."
    elif resets < 5 and resets > 3:
        show torielImg worried at fade
        toriel "..."
        toriel "I don't know why..."
        toriel "But you and Sans remind me of someone"
        show papyrusImg surprised happy flip at fade
        papyrus "IS IT HIS NAME W.D. GASTER?"
        toriel "I'm not sure"
        toriel "..."
    elif resets > 5:
        toriel "Also..."
        toriel "I want to ask"
        toriel "Are you and Sans related to a scientist named"
        papyrus "W.D. GASTER?"
        toriel "Yes, him"
        toriel "I suddenly remember him"
        toriel "He had the same kind of accent as you and Sans"
        papyrus "HE WAS SANS' FRIEND"
        papyrus "I NEVER MET HIM MYSELF"
        toriel "Oh.."
        toriel "Thanks Papyrus"
        toriel "..."
        $ torielknows = True
    jump torielsAdvice

label beQuiet:
    show papyrusImg worried flip at fade
    show torielImg pajamas worried at fade
    papyrus "..."
    toriel "..."

label torielsAdvice:
    show papyrusImg worried flip at fade
    show torielImg pajamas ejem at fade
    toriel "Ejem!"
    show torielImg pajamas compasionate at fade
    toriel "Do you understand what you did?"
    show torielImg pajamas worried at fade
    papyrus "YES MA'AM"
    toriel "Despite there's so many years since the war"
    toriel "Some humans still fear us"
    toriel "And they will use any excuse they can find to antagonize us"
    papyrus "I JUST GAVE THEM AN EXCUSE"
    toriel "Exactly"
    toriel "I'm going to talk with Asgore about this in a moment"
    show papyrusImg scared flip at fade
    papyrus "WITH THE KING?!"
    show papyrusImg worried flip at fade
    toriel "Yes"
    show torielImg pajamas compasionate at fade
    toriel "But I don't think you are ready to confront this problem"
    show torielImg pajamas embarrased at fade
    toriel "Go to your house and try to sleep"
    toriel "Take the next day off"
    toriel "Then come to talk with me"
    toriel "We will find a way to make this not escalate too high"
    show torielImg pajamas happy at fade
    toriel "Together"
    show papyrusImg embarrased happy flip at fade
    papyrus "THANKS TORIEL"
    stop music fadeout 1
    jump day2

return

label titleScreen: 
    hide sansImg
    hide undyneImg
    papyrus "WAIT"
    show papyrusImg surprised
    papyrus "WHAATT???"
    play sound "music/fx/lawAndOrder.wav"
    scene day1Alt title
    pause(3)
    papyrus "WHAT IS THIS?"
    gaster "I CAN JUMP YOU OVER THE END OF THE DAY IN WHICH I WILL EXPLAIN WHAT JUST HAPPENED"
    gaster "PLEASE SELECT THE IF YOU WANT THAT TO HAPPEN"
    menu:
        "Jump End of the Day":
            gaster "VERY WELL"
            jump endOfDay1Trigger
        "Continue Forward":
            gaster "I'LL WAIT TO TALK WITH YOU AT THE END OF THE DAY"
            gaster "GOOD LUCK"
            jump normalPath


label gasterInformThePosition:
    stop music fadeout 1
    show papyrusImg checkThis
    papyrus "SOO..."
    show undyneImg mild surprise
    show sansImg surprised
    papyrus "SOOOOOOOOOOOO....."
    play music "music/15 sans.mp3" fadein 1
    gaster "ARGH!"
    gaster "ALRIGHT, FINE, FINE..."
    show undyneImg mild surprise flip
    show sansImg surprised flip
    gaster "THERE'S A GARAGE AT THE OTHER SIDE OF THE FORTRESS"
    gaster "YOU SHOULD KNOW THAT BY NOW"
    show papyrusImg delight
    papyrus "I ALWAYS FORGOT"
    show undyneImg explaining flip
    undyne "What are you doing Papyrus?"
    show undyneImg mild surprise
    show sansImg surprised
    hide papyrusImg
    papyrus "LET'S CHECKOUT THE OTHER SIDE OF THIS PLACE"
    papyrus "MAYBE WE CAN FIND SOMETHING THERE"
    hide undyneImg
    undyne "Papyrus stop!"
    undyne "Wait! WAIT!"
    sans "what..."
    sans "this..."
    show sansImg unsure
    sans "mmm..."
    hide sansImg
    gaster "INDEED MY DEAR SANS, INDEED"
    stop music fadeout 1
    scene black with dissolve
    play music "music/05 Ruins.mp3" fadein 1 fadeout 1
    pause(1)
    scene toriel house with dissolve
    pause(0.5)
    show torielImg pajamas happy zorder 1 at fade:
        xalign 0.1 yalign 1.0
    show sansImg happy flip zorder 2 at fade:
        xpos 0.4 ypos 0.0
    show undyneImg neutral flip zorder 1 at fade:
        xpos 0.3 ypos -0.2
    toriel "I just left Frisk sleeping in their bed"
    toriel "I'm thankful that you didn't have to do anything drastic to save them"
    undyne "It was lucky that Papyrus had the idea to search to that side"
    show torielImg pajamas worried
    show undyneImg bored flip
    show sansImg bored flip
    undyne "Very lucky..."
    show sansImg happy
    sans "he's my brother, and he's very cool"
    undyne "I know, that's the only thing you talk about"
    hide undyneImg
    toriel "I guess you are saying there's nothing to worry about"
    show sansImg bored flip
    sans "it might"
    show torielImg pajamas compasionate
    toriel "it might?"
    show torielImg pajamas embarrased
    toriel "isn't your brother like super cool?"
    show sansImg flustered flip
    sans "tori"
    toriel "What am I trying to say is, mostly, do not worry that much about it?"
    show torielImg pajamas compasionate
    toriel "I... I know what is it worrying about your family, but... sometimes..."
    sans ".."
    show sansImg happy flip
    sans "i'll see in a couple of days... i guess..."
    show torielImg pajamas worried
    toriel "I'm way more worried about those humans who kidnapped Frisk"
    sans "we'll figure out what to do"
    sans ".."
    toriel "We need to rest"
    show sansImg flustered flip
    sans "yes..."
    show sansImg happy flip
    sans "we'll talk tomorrow about this"
    hide sansImg
    toriel "Good Night"
    show torielImg pajamas worried flip
    toriel "..."
    show torielImg pajamas doubt
    toriel "Now I'm thinking, where's Papyrus?"
    return

label papyrusGasterIncidentAverted:
    $ altRoute = True
    scene black with dissolve
    pause(1.0)
    play music "music/another him.MP3" fadein 1
    scene mistColor with dissolve
    show mist at fade
    pause(1.0)
    papyrus "I DIDN'T KILL ANYONE!"
    gaster "THAT'S A GREAT THING TO ASPIRE TO, I GUESS"
    papyrus "NOBODY GETS IN TROUBLE!"
    papyrus "I'M SO HAPPY!"
    gaster "THEY KIDNAPPED YOUR FRIEND ANYWAY, THOUGH"
    papyrus "OH"
    papyrus "OH..."
    gaster "IT'S NOT YOUR FAULT AT LEAST"
    papyrus "THAT'S NOT ENOUGH"
    gaster "I TOLD YOU, WE CANNOT GO EVEN MORE IN THE PAST THAN THAT MOMENT"
    papyrus "WHY?"
    gaster "I TRIED"
    gaster "MY WORKING THEORY IS THE WEKUFES COINCIDENTLY GOT ENOUGH DETERMINATION STORED AT THAT MOMENT"
    papyrus "HOW THEY GET THEIR DETERMINATION ANYWAYS?"
    gaster "I DIDN'T CHECK OUT, BUT I IMAGINE IS SIMILAR TO HOW YOUR FRIEND THE EX-ROYAL SCIENTIST GOT THEM"
    papyrus "..."
    papyrus "THAT WERE ENOUGH QUESTIONS"
    gaster "WELL, YOU ARE FREE TO DO ANYTHING YOU WANT THE NEXT TWO DAYS"
    gaster "I HOPE YOU USE THIS TIME WELL"
    papyrus "..."
    papyrus "WELL, NOW THE QUESTIONS"
    return
    
return

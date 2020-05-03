label titleScreen: 
    hide sansImg
    hide undyneImg
    papyrus "WAIT"
    show papyrusImg surprised
    papyrus "WHAATT???"
    stop music
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
    play sound "music/fx/steps.wav"
    papyrus "LET'S CHECKOUT THE OTHER SIDE OF THIS PLACE"
    papyrus "MAYBE WE CAN FIND SOMETHING THERE"
    hide undyneImg
    play sound "music/fx/steps.wav"
    undyne "Papyrus stop!"
    undyne "Wait! WAIT!"
    sans "what..."
    sans "this..."
    show sansImg unsure
    sans "mmm..."
    hide sansImg
    play sound "music/fx/steps.wav"
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

label shortcut:
    papyrus "SOOO...."
    papyrus "SANS..."
    papyrus "WHAT'S ABOUT IF YOU USE THE SHORTCUT ON FRISK"
    undyne "Whaaa???!!"
    undyne "What are you talking about Papyrus?"
    "* Sans thinking face *"
    "* Sans dissapears *"
    "* Sans comes back, with Frisk *"
    papyrus "I KNEW YOU COULD DO IT, YOU SHOULD HEAR ME MORE IN THE FUTURE!"
    papyrus "COME ON EVERYBODY, WE NEED TO GET OUT OF HERE"
    undyne "This was a surprise, why you didn't say you could do this?!"
    sans "ahh...."
    undyne "I know you are not really into explaining your stuff"
    undyne "But we got Frisk!"
    undyne "Let's go back!"
    "* Undyne go away *"
    pause(2)
    "* Sans and Frisk dissapears *"
    "* Toriel's house *"
    toriel "Frisk is sleeping in their bed now"
    undyne "Good job Sans! That was a whole surprise!"
    undyne "Good Papyrus remembered about it!"
    sans "yeah..."
    undyne "Something wrong"
    sans "great, i forgot to be subtle"
    undyne "He figure out how the spell you use all the time works, it's nothing terrible"
    sans "it was like a trade secret of sorts..."
    undyne "Papyrus is very good at learning random things, relax"
    sans "..."
    toriel "You don't seem too convinced"
    sans "..."
    toriel "Let that rest for a couple of days, after we had rest and decided what to do with this..."
    toriel "kidnappers"
    sans "..."
    sans "fine"
    undyne "Good!"
    undyne "Now, let's go Pa..."
    undyne "Papyrus?"
    undyne "Where's Papyrus?"
    return

label papyrusGasterIncidentAverted:
    $ altRoute = True
    stop music fadeout 1
    scene black with dissolve
    pause(1.0)
    play music "music/another him.MP3" fadein 1
    scene mistColor with dissolve
    show mist at fade
    pause(1.0)
    show papyrusImg delight at fade:
        xpos -0.1
    papyrus "I DIDN'T KILL ANYONE!"
    show gaster trapped sad flip at fade:
        xpos 0.4
    gaster "THAT'S A GREAT THING TO ASPIRE TO, I GUESS"
    show papyrusImg delight flip
    papyrus "NOBODY GETS IN TROUBLE!"
    show papyrusImg delight
    papyrus "I'M SO HAPPY!"
    show gaster trapped maybe flip
    gaster "THEY KIDNAPPED YOUR FRIEND ANYWAY, THOUGH"
    stop music fadeout 1
    pause(1)
    show papyrusImg uhh
    papyrus "OH"
    papyrus "OH..."
    play music "music/15 sans.mp3" fadein 1
    show gaster neutral flip
    gaster "IT'S NOT YOUR FAULT AT LEAST"
    show papyrusImg annoyed
    papyrus "THAT'S NOT ENOUGH"
    gaster "I TOLD YOU, WE CANNOT GO EVEN MORE IN THE PAST THAN THAT MOMENT"
    show papyrusImg confused
    papyrus "WHY?"
    show gaster trapped sad flip
    gaster "I TRIED"
    show gaster neutral flip
    gaster "MY WORKING THEORY IS THE WEKUFES COINCIDENTLY GOT ENOUGH DETERMINATION STORED AT THAT MOMENT"
    show papyrusImg annoyed
    papyrus "HOW THEY GET THEIR DETERMINATION ANYWAYS?"
    gaster "I DIDN'T CHECK OUT, BUT I IMAGINE IS SIMILAR TO HOW YOUR FRIEND THE EX-ROYAL SCIENTIST GOT THEM"
    show papyrusImg uhh
    papyrus "..."
    show papyrusImg annoyed
    papyrus "THAT WERE ENOUGH QUESTIONS"
    gaster "WELL, YOU ARE FREE TO DO ANYTHING YOU WANT THE NEXT TWO DAYS"
    gaster "I HOPE YOU USE THIS TIME WELL"
    papyrus "..."
    show papyrusImg neutral
    papyrus "WELL, NOW THE QUESTIONS"
    stop music fadeout 1
    return
    
return

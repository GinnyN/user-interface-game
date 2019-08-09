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
            jump endOfDay1
        "Continue Forward":
            gaster "I'LL WAIT TO TALK WITH YOU AT THE END OF THE DAY"
            gaster "GOOD LUCK"
            jump insideBuilding


label gasterInformThePosition:
    papyrus "SOO..."
    papyrus "SOOOOOOOOOOOO....."
    gaster "ARGH!"
    gaster "ALRIGHT, FINE, FINE..."
    gaster "THERE'S A GARAGE AT THE OTHER SIDE OF THE FORTRESS"
    gaster "YOU SHOULD KNOW THAT BY NOW"
    papyrus "I ALWAYS FORGOT"
    undyne "What are you doing Papyrus?"
    papyrus "LET'S CHECKOUT THE OTHER SIDE OF THIS PLACE"
    papyrus "MAYBE WE CAN FIND SOMETHING THERE"
    undyne "Papyrus stop!"
    undyne "Wait! WAIT!"
    sans "what..."
    sans "this..."
    sans "mmm..."
    gaster "INDEED MY DEAR SANS, INDEED"
    "* The scene changes to Toriel house, with Undyne and Sans talking with Toriel *"
    toriel "I just left Frisk sleeping in their bed"
    toriel "I'm thankful that you didn't have to do anything drastic to save them"
    undyne "It was lucky that Papyrus had the idea to search to that side"
    undyne "Very lucky..."
    sans "he's my brother, and he's very cool"
    undyne "I know, that's the only thing you talk about"
    "* Undyne leaves *"
    toriel "I guess you are saying there's nothing to worry about"
    sans "it might"
    toriel "it might?"
    toriel "isn't your brother like super cool?"
    sans "tori"
    toriel "What am I trying to say is, mostly, do not worry that much about it?"
    toriel "I... I know what is it worrying about your family, but... sometimes..."
    sans ".."
    sans "i'll see in a couple of days... i guess..."
    toriel "I'm way more worried about those humans who kidnapped Frisk"
    sans "we'll figure out what to do"
    sans ".."
    toriel "We need to rest"
    sans "yes..."
    sans "we'll talk tomorrow about this"
    toriel "Good Night"
    toriel "..."
    toriel "Now I'm thinking, where's Papyrus?"
    return

label papyrusGasterIncidentAverted:
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
    return
    
return

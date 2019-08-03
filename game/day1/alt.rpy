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
    
return
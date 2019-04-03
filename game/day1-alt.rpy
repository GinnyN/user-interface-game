label titleScreen: 
    papyrus "WAIT"
    papyrus "WHAATT???"
    "* title screen appears *"
    "* pause for a couple of seconds *"
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
            jump jumpBuilding
return

label endOfDay1:
    if resets > 0:
        if resets == 1:    
            scene forest with dissolve
            show papyrusImg screamingCall at fade:
                xpos -0.1
            papyrus "GASTER!"
            papyrus "ARE YOU THERE?!"
            show papyrusImg annoyed
            papyrus "CAN YOU EXPLAIN WHAT'S GOING ON?!"
            show papyrusImg worried
            papyrus "WHY AM I..."
            papyrus "BACK..."
            papyrus "HERE..."
            show gaster trapped explain flip at fade:
                xpos 0.4
            gaster "THIS IS THE RESET I WAS TALKING ABOUT MY DEAR PAPYRUS"
            gaster "THIS IS PART OF THE POWERS OF DETERMINATION"
            show gaster trapped sorry flip
            gaster "WHEN YOU HAVE ENOUGH OF IT, OF COURSE"
            show papyrusImg uhh
            papyrus "SOO..."
            papyrus "YOU CAN DO THIS BECAUSE THOSE TANKS FILLED WITH DETERMINATION"
            show gaster trapped proud flip
            gaster "EXACTLY"
            papyrus "DO YOU THINK WE COULD USE THOSE DETERMINATION FILLED TANKS TO GET YOU OUT?"
            papyrus "THAT'S THE IDEA?"
            show gaster trapped sorry flip
            gaster "AFTER WHAT HAPPENED WITH..."
            show gaster trapped sorry
            gaster "THE CURRENT ROYAL SCIENTIST LAST EXPERIMENTS..."
            show gaster trapped maybe flip
            gaster "I DON'T FEEL, WELL, COMFORTABLE IN ASKING YOU TO GATHER MORE OF IT"
            gaster "SO, WE CAN USE WHAT THE WEKUFE HAVE ALREADY GATHERED"
            show papyrusImg neutral
            papyrus "I SEE"
            show gaster trapped explain flip
            gaster "THE THING IS..."
            gaster "I CAN ONLY SET YOU, AND ME, BACK IN TIME TO THAT EXACT MOMENT"
            gaster "WHEN YOU, SANS AND YOUR FRIEND WERE TO STORM THAT FORTRESS"
            show papyrusImg annoyed 
            papyrus "THAT'S A TERRIBLE TIME FOR SOMETHING LIKE THIS..."
            show gaster trapped sorry flip
            gaster "I KNOW..."
            show gaster trapped neutral flip
            gaster "BUT WE'LL HAVE TO WORK WITH THAT, IF WE WANT TO USE THAT DETERMINATION"
            gaster "WE CAN TRY UNTIL WE MADE IT"
            gaster "OR WE DECIDE WE CAN'T"
            gaster "IT'S UP TO US NOW"
            show papyrusImg delight
            papyrus "WE'LL FIND A WAY! I'M SURE OF IT!"
            show gaster trapped dissapointed
            gaster "I NEEDED TO HEAR THAT..."
        
        call questionsEnd from _call_questionsEnd
        show gaster trapped neutral flip
        gaster "JUST REMEMBER WE CAN TALK AGAIN AFTER THE END OF A DAY IF YOU HAVE ANY QUESTIONS"
        show papyrusImg neutral
        papyrus "I'LL REMEMBER THAT"
    return
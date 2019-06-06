label visitAlphys:
    if tryWithAlphys:
        papyrus "OK"
        papyrus "I HOPE SHE'S NOT DOING SOMETHING IMPORTANT"
        papyrus "LET'S DO THIS"
        papyrus "{cps=*0.5}DR AAALLLLLLLLLLLLLLLLLLLLL{/cps}"
        scene black with dissolve
        extend "{cps=*0.5}PHHHYYYYYYYYYYYYYYYYYYYYYYYY{/cps}"
        scene mistColor with dissolve
        extend "{cps=*0.5}YYYYYSSSSSSSSSSSSSSSSSSSSSSS{/cps}"
        alphys "Ah!"
        alphys "Papyrus..."
        alphys "I'm sorry I'm such a mess..."
        alphys "It just..."
        papyrus "WHAT HAPPENED?"
        alphys "I was watching the last episode of the new season of Mew Mew Kissy Cutie..."
        alphys "And..."
        papyrus "AND?"
        alphys "IT BECAME GOOD"
        papyrus "OH GOD!"
        alphys "IT WAS A REASON FOR EVERYTHING BETWEEN THE TWO SEASONS!"
        alphys "I CANNOT BELIEVE IT PAPYRUS!!!"
        papyrus "OK, SO YOU ARE BUSY NOW"
        alphys "Ah...."
        papyrus "I'M GOING TO COME BACK IN AROUND 25 MINUTES TO TALK TO YOU"
        alphys "I already finished the episode..."
        alphys "So..."
        alphys "I think you can talk to me anything you need to talk to me???"
        papyrus "OH"
        papyrus "NEATO!"
        "* SLAP SLAP!*"
        papyrus "DR ALPHYS"
        papyrus "IN THIS PENDRIVE THERE'S A BLUEPRINT FOR A MACHINE WHICH CAN ABSORB DETERMINATION"
        papyrus "IT'S NOT THE DT EXTRACTOR"
        alphys "Where..."
        alphys "Where did you find this?"
        papyrus "I HAVE A FRIEND WHICH IS TRAPPED..."
        papyrus "..."
        alphys "Beyond the Darkness?"
        papyrus "YES YES, EXACTLY!"
        papyrus "AND NOW HE NEEDS HELP TO GET OUT"
        papyrus "I"
        extend "... I"
        extend "... I"
        extend "... I"
        extend "... I"
        papyrus "I NEED TO KNOW IF YOU CAN HELP US"
        alphys "This are just the blueprint?"
        papyrus "IT HAS MORE FILES, BUT I DO NOT UNDERSTAND VERY WELL WHAT THOSE FILES DO"
        alphys "I ca..."
        alphys "..."
        alphys "It's going to be easy"
        papyrus "REALLY?"
        alphys "Y... Yes.."
        papyrus "THANKS YOU DR ALPHYS!!"
        alphys "I'm..."
        alphys "I'm going to need some space..."
        papyrus "TELL NO MORE"
        papyrus "THANK YOU VERY MUCH!"
        "* Papyrus Exits *"
        alphys "..."
        alphys "I'm sorry Papyrus"
        $ penAtAlphys = True
        if day > 2:
            $ alphysFailState = True
    else:
        papyrus "DR ALPHYS SAID SHE WAS WORKING ON SOMETHING IMPORTANT"
        show papyrusImg coolDude delight
        papyrus "MAYBE IS A NEW KIND OF PUZZLE!"
        show papyrusImg coolDude thinking
        papyrus "OK, MAYBE NOT"
        show papyrusImg coolDude delight
        papyrus "BUT SHOULD BE INTERESTING!"
        scene undyneAlphysHouse inside with dissolve
        play music "music/33 Quiet Water.mp3" fadein 1 fadeout 1 
        show papyrusImg coolDude me flip at fade:
            xpos 0.4
        show alphysImg casual realizing flip zorder 3 at fade:
            xpos -0.15
            ypos -0.2
        papyrus "DR ALPHYS!"
        show papyrusImg coolDude delight flip
        show alphysImg casual nostalgic
        alphys "Papyrus!"
        alphys "What"
        show alphysImg casual nostalgic flip
        alphys "eh.."
        alphys "ehhh..."
        show papyrusImg coolDude happy flip
        show alphysImg casual nostalgic
        papyrus "YOU SAID SOMETHING IN OUR LAST TRAINING ABOUT AN IMPORTANT WORK OF YOURS"
        show papyrusImg coolDude checkThis flip
        papyrus "I CAME TO CHECK IF YOU NEEDED SOME MORAL SUPPORT"
        show alphysImg casual confused mild
        alphys "ahhh..."
        papyrus "I´M YOUR PERSONAL TRAINER AFTER ALL"
        show alphysImg casual dismissive flip
        alphys "Now I need some quiet"
        show alphysImg casual confused mild
        papyrus "YOU MEAN WHITE NOISE"
        show papyrusImg coolDude happy flip
        papyrus "OR ELSE YOU'LL END UP WATCHING THE NEW SEASON OF MEW MEW"
        show alphysImg casual dismissive
        alphys "Come on Papyrus"
        alphys "The first chapter was promising    {nw}"
        alphys "{fast}But for the moment is as good as the second season    {nw}"
        alphys "{fast}Which means is trash    {nw}"
        alphys "{fast}While they admitted the second season ruined Mew Mew story arc   {nw}"
        alphys "{fast}And they are trying to fix it    {nw}"
        alphys "{fast}I don't see how that is fixing it    {nw}"
        alphys "{fast}They should try another aproach if they want to keep the franchise alive    {nw}"
        show alphysImg casual noWords
        alphys "{fast}But the 1st season is a classic already     {nw}"
        alphys "{fast}They can't fix that    {nw}"
        show papyrusImg coolDude thinking flip
        papyrus "ISN'T THE MANGA STILL GOING?"
        show alphysImg casual dismissive
        alphys "Yes, yes"
        alphys "But that a manga based on the 1st season     {nw}"
        alphys "{fast}Mew Mew is an original animation     {nw}"
        show alphysImg casual noWords
        alphys "{fast}It's not very good    {nw}"
        show alphysImg casual dismissive
        alphys "{fast}But at least is better than this 2nd and 3rd season trash     {nw}"
        show papyrusImg coolDude happy flip
        papyrus "I SEE YOU HAVEN'T LOST IT!"
        papyrus "UNDYNE IS ALWAYS TELLING ME ABOUT HOW YOU RANT ABOUT WHEN THEY SEE AN EPISODE OF THE NEW SEASON"
        show alphysImg casual tired
        alphys "Yeah, she loves see me suffer and complain"
        show papyrusImg coolDude thinking flip
        papyrus "SHE DESCRIBE IT AS 'PASSIONATE AND FOCUSED'"
        show alphysImg casual confused mild
        alphys "Why we always end up talking about how much Undyne loves me?"
        show papyrusImg coolDude explaining flip
        papyrus "I DON'T KNOW"
        papyrus "YOU STILL SEEMS HAVE SOME ISSUES WHEN IS ABOUT LIKING ANIME"
        show alphysImg casual tired
        alphys "You know"
        alphys "I lied so much some times I feel I don't deserve Undyne's love"
        show papyrusImg coolDude thinking flip
        papyrus "SANS IS GETTING BETTER ABOUT HIS LAZYNESS, BUT VERY SLOWLY"
        show papyrusImg coolDude explaining flip
        papyrus "MAYBE YOU JUST NEED MORE TIME TO UNDERSTAND UNDYNE LOVES YOU FOR HOW YOU ARE"
        alphys "Maybe..."
        show alphysImg casual explaining
        alphys "Well..."
        show alphysImg casual explaining flip
        alphys "I'd better get back to programming"
        show papyrusImg coolDude thinking flip
        papyrus "PROGRAMMING?"
        show alphysImg casual explaining
        alphys "Yes..."
        alphys "It's something very difficult, and you need time and effort to understand them"
        show papyrusImg coolDude happy flip
        papyrus "HEY! THEN IS LIKE FIGHTING!"
        papyrus "OR COOKING SPAGUETTI!"
        show papyrusImg coolDude checkThis flip
        papyrus "YOU NEED TIME AND EFFORT TO UNDERTAND IT AND GET GOOD AT IT!"
        show alphysImg casual confused mild
        alphys "Something like that"
        show alphysImg casual explaining
        alphys "But in programming you tell the computer what to do"
        show papyrusImg coolDude surprised happy flip
        papyrus "REALLY?"
        alphys "Yes"
        alphys "But in a language the computer understand"
        alphys "Because the computer doesn't understand normal language"
        show papyrusImg coolDude thinking flip
        papyrus "WHAT KIND OF THINGS YOU CAN TELL TO THE COMPUTER"
        show alphysImg casual confused mild
        alphys "For a very simplificated example"
        alphys "You can tell them that..."
        show alphysImg casual explaining
        alphys "That table is an object which can contain some other objects like cups"
        show papyrusImg coolDude explaining flip
        papyrus "SO THE OBJECT TABLE ATRIBUTTE IS CONTAIN OTHER OBJECTS?"
        show alphysImg casual confused
        alphys "Yes..."
        alphys "..."
        show alphysImg casual nostalgic
        alphys "Papyrus.."
        alphys "What's a float?"
        show papyrusImg coolDude thinking flip
        papyrus "A TYPE OF NUMBER VARIABLE THAT CAN CONTAIN DECIMAL POINTS"
        alphys "What's a factory?"
        show papyrusImg coolDude explaining flip
        papyrus "AN OBJECT WHICH PRODUCES OTHER OBJECTS"
        alphys "A singleton?" 
        show papyrusImg coolDude thinking
        papyrus "AN OBJECT WHICH HAVE A SINGLE INSTANCE DURING RUN"
        alphys "And Script Oriented Programming?"
        papyrus "A SMALL PROGRAM WHICH RUNS ON SEQUENCIAL ORDER"
        alphys "And a stack?"
        show papyrusImg coolDude thinking flip
        papyrus "A DATA STRUCTURE OF OBJECTS IN WHICH CAN ONLY ACCESS THE LAST ONE AT A TIME"
        show alphysImg casual confused
        alphys "Papyrus"
        show alphysImg casual nostalgic
        alphys "Since when you know Programming Theory and Data Structures?"
        papyrus "SINCE YOU SAID TABLE"
        show papyrusImg coolDude explaining flip
        papyrus "IT JUST CAME TO ME SUDDENLY"
        alphys "Whoa.. that's weird"
        papyrus "I KNOW"
        show papyrusImg coolDude thinking flip
        papyrus "I KNOW..."
        $ papyrusKnowsProgramming = True
        stop music
return 

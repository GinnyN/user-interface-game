label checkSans:
    if False:# papersPapyrusCreation == True:
        papyrus "SANS IS NOT HERE"
        papyrus "WHY?!"
        papyrus "I GUESS HE WILL APPEAR TO MAKE JOKES AT MY EXPENSE IN ANY SECOND"
        papyrus "BUT WHERE'S HE IS?"
        sans "sup' bro"
        papyrus "SANS! I NEED TO TALK WITH YOU!"
        sans "but bro"
        sans "i has been doing a ton of work"
        papyrus "IT'S NOT ABOUT PUNS!"
        papyrus "LISTEN"
        papyrus "I FOUND THIS PAPERS AT THE SCHOOL BASEMENT WHICH ARE A WEIRD KIND OF DIARY AND SOMEONE CALLED LIKE YOURSELF APPEAR IN THEM AND THEY WERE TALKING ABOUT MAKING A BROTHER FOR THIS PERSON CALLED EXACTLY LIKE YOU AND I SAID MAYBE IS SANS AND MAYBE THEY'RE TALKING ABOUT ME SO I CAME TO SEE IF YOU CAN TELL ME IF IT'S TRUE AND IF YOU REMEMBER ANY OF THIS"
        sans ".."
        sans "you have been with alphys way too long"
        papyrus "I WAS THINKING THAT MAYBE YOU COULD SHED SOME LIGHT ABOUT THIS"
        sans "that's dangerous"
        papyrus "WHAT?"
        papyrus "THE PAPERS?"
        sans "think"
        papyrus "SANS!"
        sans "just give me those papers and"
        papyrus "NO!"
        papyrus "YOU ALWAYS ARE DOING THINGS WITHOUT TELLING ME!"
        papyrus "I WILL NOT GIVE YOU THIS PAPERS UNTIL YOU TELL ME WHAT'S GOING ON!"
        sans "catch the stick, catch the stick"
        papyrus "OH! A STICK!"
        "Sans throws the stick and Papyrus leave the papers behind so he can catch them"
        sans "sometimes i'm glad he's kind of a dog"
        papyrus "CURSES! HE GOT ME!"
        papyrus "BUT THIS IS NOT DONE YET!"
        papyrus "HOMEWORK GRABING ATTACK!!!"
        "CHOMP!"
        sans "uh?"
        papyrus "TALK SANS!"
        sans "but... i´m too sleepy right... now..."
        sans "zzzzZZZZzzzz"
        papyrus "GREAT, THE SPECIAL ABILITY OF MY BROTHER"
        papyrus "SLEEPING EVERYWHERE AND EVERY MOMENT"
        papyrus "I WILL NOT GET ANSWERS FROM HIM"
        papyrus "I GUESS I HAVE TO ASK GASTER"
        sans "gaster?"
        papyrus "NOW WE'RE TALKING!"
        papyrus "EXPLAIN"
        sans "...."
        sans "w. d. gaster is our dad"
        papyrus "HE NEVER TOLD ME THAT"
        sans "he doesn't like the term, because he doesn't like parents"
        sans "those probable are notes from he decided to create either of us"
        papyrus "BUT WHY NOBODY ELSE REMEMBER HIM?"
        sans "you shouldn´t remember him, only me"
        sans "how do you remember him?"
        papyrus "GOTTA GO BYE"
        "*Papyrus leaves*"
        sans "i will never catch him"
        sans "but how he knows anything about gaster?"
        sans "something weird is happening"
        $ gasterPapyrusSansDad = True
        $ papersPapyrusCreation = False
    elif tryWithSans:
        papyrus "I HAVE TO TRY GET HIM TO HELP US"
        show papyrusImg coolDude grandiose
        papyrus "I KNOW THIS IS USELESS, BUT I PROMISE THIS TO GASTER!"
        gaster "YES, YOU PROMISED THIS TO ME"
        show papyrusImg coolDude angry
        papyrus "SHUT UP!"
        papyrus "I'M TRYING TO MENTALIZE WHAT I HAVE TO DO!"
        if penAtAlphys:
            papyrus "WAIT"
            papyrus "DIDN'T I GIVE THE PENDRIVE TO ALPHYS ALREADY?"
            gaster "THAT'S ACTUALLY TRUE"
            papyrus "THEN I DON'T HAVE TO TALK TO SANS ABOUT THIS!"
            sans "are you ok?"
            papyrus "SANS!?"
            papyrus "EHEM!"
            papyrus "SINCE "
            extend "WHEN YOU WERE HERE?"
            sans "..."
            sans "you know i can heard you from the beginning of the stairs, right?"
            papyrus "..."
            papyrus "..."
            papyrus "..."
            papyrus "I HAVE TO GO TO THE BATHROOM"
            "*Papyrus leaves*"
            sans "welp..."
            sans "he hopefully is ok..."
            sans "..."
            sans "why i have this feeling that he isn't?"
            "*Papyrus arrives to the forest*"
            papyrus "WHY AM I RUNNING AWAY FROM SANS THIS HAS NO SENSE!"
            gaster "DON'T WORRY, YOU AREN'T THE ONLY ONE WHO HAS RAN AWAY FROM HIM"
            papyrus "WHAT."
            papyrus "HAVE YOU?"
            gaster "OF COURSE"
            gaster "SEVERAL TIMES"
            gaster "I HAVE ALSO RAN AWAY FROM YOU, "
            extend "THE QUEEN, "
            extend "MY CREATOR..."
            papyrus "I UNDERSTAND THE LAST TWO, BUT WHY SANS?"
            gaster "WELL..."
            gaster "I DID A MISTAKE "
            extend "DURING "
            extend "THE PROCESS OF "
            extend "YOUR SPELL"
            gaster "AND INSTEAD OF YOU I END UP WITH A BUNCH OF GOAT LOOKING SKULLS?"
            papyrus "DID YOU CREATE THE BLASTERS BY MISTAKE WHILE TRYING TO CREATE ME?"
            gaster "OH NO"
            gaster "I JUST REPURPOSED THE GOAT LOOKING SKULLS AS LASERS BEAMS"
            gaster "I HOPE YOU STILL HAVE YOURS"
            papyrus "YEAH, I BARELY USE IT THOUGH"
            gaster "IT MAKE SENSE, YOU ARE STRONG AFTER ALL"
            papyrus "I REALLY LIKED TO TALK WITH YOU"
            papyrus "ABOUT HOW WE RAN AWAY FROM OUR PROBLEMS"
            gaster "BELIEVE ME MY DEAR PAPYRUS"
            gaster "YOU ARE NOT GOING TO MAKE AN HABIT OUT OF THIS"
            papyrus "BUT I HAVE TO GO"
            gaster "GOOD LUCK MY DEAR BOY"
            return
        else:
            call papyrusAskSans
    else:
        papyrus "HE'S GETTING BETTER THANKS TO TORIEL"
        papyrus "BUT HE'S STILL SLACKING OFF WAY TOO OFTEN!"
        scene elevator outside with dissolve:
            ypos -0.2
        show papyrusImg coolDude offended flip at fade:
            xpos -0.1
        play music "music/15 sans.mp3" fadein 1
        papyrus "SANS IS NO WHERE TO BE FOUND"
        papyrus "HE'S LUCKY THERE'S NO MONSTERS WANTING TO GO TO HIGH SNOWDIN"
        show papyrusImg coolDude explaining flip
        papyrus "BUT HE SHOULD BE HERE!"
        show sansImg hoddie neutral flip at fade:
            xpos 0.5
        sans "sup' bro?"
        show papyrusImg coolDude angry
        papyrus "SANS!"
        papyrus "WHERE HAVE YOU BEEN?"
        sans "just walking"
        show papyrusImg coolDude offended
        papyrus "WALKING TO GRILLSBY'S I BET"
        show sansImg hoddie content flip
        sans "no"
        sans "just walking"
        show sansImg hoddie neutral flip
        sans "the forest is very nice this time of the day"
        show papyrusImg coolDude angry
        papyrus "YOU DON'T FOOL ME"
        papyrus "YOU WERE DOING SOMETHING LAZY I'M SURE!"
        show sansImg hoddie sideglance flip
        sans "i was technically slacking off though"
        show papyrusImg coolDude thinking
        stop music
        papyrus "BUT THAT KIND OF SLACKING OFF..."
        papyrus "..."
        show sansImg hoddie neutral flip
        sans "what?"
        show papyrusImg coolDude delight
        play music "music/17 Snowy.mp3" fadein 1
        papyrus "I DO THAT AS WELL"
        show sansImg hoddie surprised flip
        sans "you? slacking off?"
        scene black with dissolve
        papyrus "IT'S JUST"
        scene freeMorning sans resetZero panoramica with dissolve:
            ypos -0.35
            linear 10 ypos 0.0
        papyrus "THE TREES ARE GREEN"
        papyrus "THE SKY IS BLUE"
        papyrus "THE AIR IS CLEAN"
        papyrus "THE OUTSIDE IS AMAZING"
        sans "just give you energy to continue"
        papyrus "YES!"
        papyrus "MAYBE IS PART OF THE REASON OF WHY YOU ARE GETTING LESS LAZY"
        sans "?!"
        sans "it seems i'm losing my edge"
        show papyrusImg coolDude offended  at fade:
            xpos -0.1
        papyrus "MAYBE YOU SHOULD USE YOUR ACTUAL FREE TIME TO DO THAT THOUGH"
        show sansImg hoddie content flip  at fade:
            xpos 0.5
        sans "don't worry"
        sans "i have that machine over there i did"
        show sansImg hoddie neutral flip
        sans "it tell me when someone is close"
        show papyrusImg coolDude delight
        papyrus "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        show sansImg hoddie done flip
        sans "i'm totally losing my edge"
        hide papyrusImg
        papyrus "TOOOOORRRRRIIIIIIIIEEEEEEEEEEEEEELLLLLLLLLLLL!!!!!!!!!!!!!!!"
        stop music
return

label papyrusAskSans:
    $ tryWithSans = False
    show papyrusImg coolDude realizing
    papyrus "OK..."
    papyrus "I BETTER DO THIS..."
    papyrus "HERE I GO..."
    show sansImg hoddie surprised flip at fade:
        xpos 0.4
    sans "papyrus?"
    show papyrusImg coolDude scared
    papyrus "SANS WHAT ARE YOU DOING HERE"
    sans "..."
    show sansImg hoddie sideglance flip
    play music "music/15 sans.mp3" fadein 1
    sans "i came for a drink"
    show papyrusImg coolDude neutral
    papyrus "OH..."
    hide papyrusImg
    papyrus "LET'S ME GET YOU SOME FOR YOU"
    show papyrusImg coolDude neutral at fade:
        xpos -0.3
    papyrus "DO YOU WANT MILK?"
    show sansImg hoddie content flip
    sans "oh sure. milk is fine"
    hide papyrusImg
    pause(0.5)
    gaster "CAN YOU HEAR ME MY DEAR SANS?"
    pause(1.0)
    gaster "NO, DOESN'T SEEM LIKE IT"
    show papyrusImg coolDude uhh at fade:
        xpos 0.0
    papyrus "SO... SANS..."
    show sansImg hoddie neutral flip
    sans "mm??"
    papyrus "HAVE YOU HEAR ABOUT W.D. GASTER?"
    hide sansImg
    sans "cough! "
    extend "cough! "
    extend "cough!"
    gaster "HOW IS HE DOING THAT?"
    gaster "HE DOESN'T HAVE A NECK!"
    show papyrusImg coolDude annoyed flip
    papyrus "SHHHHHHH....."
    show papyrusImg coolDude uhh
    show sansImg hoddie worried flip at fade:
        xpos 0.4
    sans "are you..."
    sans "talking with him?"
    sans "right now?"
    papyrus "YES... YES I AM"
    sans "what is he telling you?"
    gaster "HE'S TRYING TO PROVE YOU?"
    show papyrusImg coolDude uhh flip
    papyrus "MORE LIKE HE'S TRYING TO CHECK OUT IF I'M ACTUALLY SAYING THE TRUTH"
    gaster "TELL HIM THAT I SAY HE SHOULDN'T BE DOING THIS AND JUST GETTING TO THE POINT"
    show papyrusImg coolDude uhh
    papyrus "HE'S ANGRY BECAUSE YOU ARE MAKING TOO MANY QUESTIONS"
    papyrus "BUT"
    papyrus "I MEAN"
    show papyrusImg coolDude explaining
    papyrus "FLOWEY HAPPENED"
    show papyrusImg coolDude careful
    papyrus "SO"
    show papyrusImg coolDude uhh
    papyrus "I GUESS IS NOT OUT OF THE EQUATION"
    show sansImg hoddie annoyed flip
    sans "that doesn't tell me anything"
    papyrus "WHAT IS TELLING ME IS"
    show sansImg hoddie surprised flip
    papyrus "YOU REMEMBER HIM"
    papyrus "WHY I DIDN'T?"
    hide sansImg
    stop music fadeout(1)
    pause(1.0)
    play music "music/16 Nyeh Heh Heh!.mp3" fadein(1)
    show papyrusImg coolDude angry
    papyrus "SANS!"
    scene forest with dissolve
    show sansImg hoddie surprised at fade:
        xpos 0.6
    sans "what is happening... i don't"
    gaster "THIS IS GETTING WAY MORE COMPLICATED THAN IT SHOULD"
    show sansImg hoddie surprised flip
    papyrus "SAAAAANNNNNSSSSSSSSS!!!!!!!!"
    hide sansImg
    sans "!!!"
    show papyrusImg coolDude angry at fade:
        xpos 0.1
    papyrus "ARGH!"
    scene school outside with dissolve:
        ypos -0.3
    show torielImg teacher neutral flip at fade:
        xpos 0.3
    show sansImg hoddie surprised flip at fade:
        xpos 0.0
    toriel "Oh, Sans!"
    show sansImg hoddie surprised
    toriel "Shouldn't you been at the elevator offices right now?"
    toriel "Papyrus is not going to like this"
    scene tryWithSans jumpOver with dissolve:
        xpos 0.0
        ypos -1.0
        linear 1 ypos 0.0
    pause(0.5)
    show torielImg teacher neutral at fade:
        xpos 0.3
    show sansImg hoddie surprised at fade:
        xpos 0.0
    toriel "Yes, he didn't like it"
    hide sansImg
    pause(0.5)
    show torielImg teacher angry flip at fade:
        xpos 0.3
    show papyrusImg coolDude angry flip at fade:
        xpos -0.1
    toriel "Papyrus?"
    toriel "What is happening?"
    papyrus "SAAAANS!!!"
    hide papyrusImg
    show torielImg teacher worried flip
    pause(2.0)
    toriel "I need to stop them!"
    scene skelebroHouse outside with dissolve
    show sansImg hoddie surprised at fade:
        xpos 0.4
    pause(1.0)
    show papyrusImg coolDude angry at fade:
        xpos 0.0
    show sansImg hoddie surprised flip at fade:
        xpos 0.5
    sans "papyrus..."
    stop music fadeout(1)
    papyrus "SANS, LOOK"
    papyrus "I HAVE WAY MORE STAMINA THAN YOU WILL EVER HAVE"
    papyrus "SO PLEASE HELP ME"
    papyrus "STOP RUNNING AWAY AND TELL ME"
    sans "how..."
    sans "how are you talking to him"
    papyrus "THERE SOME BEINGS KIDNAPPING HUMAN KIDS TO EXTRACT THEIR DETERMINATION"
    papyrus "THE SAME ONES WHO KIDNAPPED FRISK SOME DAYS AGO"
    papyrus "THAT DETERMINATION CAUSED AN ANOMALY"
    sans "that..."
    dtSans "make sense"
    papyrus "GASTER TOLD ME HE MADE SURE YOU AND ME WILL REMEMBER HIM AFTER THE EXPERIMENT WHICH TRAPPED HIM"
    papyrus "BUT IT SEEMS ONLY YOU DID!"
    papyrus "WHY?"
    show sansImg hoddie surprised
    sans "it was an accident"
    sans "you didn't have enough determination inyected"
    show sansImg hoddie surprised flip
    sans "when we realized it was too late"
    show papyrusImg coolDude uhh
    papyrus "OK..."
    papyrus "THEN... WHY YOU DIDN'T TOLD ME WHEN I FORGOT EVERYTHING!?"
    show sansImg hoddie surprised
    sans "i..."
    sans "i..."
    show papyrusImg coolDude angry
    papyrus "WHY?!"
    dtSans "I..."
    scene tryWithSans sansShattering frame1 with dissolve
    pause(0.25)
    play sound "music/fx/soulShatter.wav"
    scene tryWithSans sansShattering frame2 with dissolve
    pause(0.25)
    scene tryWithSans sansShattering frame3 with dissolve
    hide sansImg
    show papyrusImg coolDude realizing at fade:
        xpos 0.4
    papyrus "SANS?"
    show gaster trapped sorry at fade:
        xpos 0.1
    gaster "NO..."
    papyrus "HOW?!"
    gaster "THE PAIN OF HAVING TO EXPLAIN YOU WAS TOO GREAT..."
    gaster "AND HE HAS 1 HP..."
    papyrus "NO..."
    papyrus "I..."
    gaster "NO... YOU DIDN'T"
    show papyrusImg coolDude realizing flip
    papyrus "I KILLED HIM"
    show gaster trapped angry
    gaster "PAPYRUS PLEASE"
    gaster "WE CAN STILL RESET THE TIMELINE"
    show papyrusImg coolDude realizing
    papyrus "NO"
    gaster "WHAT?"
    papyrus "I'M SORRY GASTER, BUT I CANNOT MAKE THE LIFE OF MY BROTHER THAT MEANINGLESS"
    gaster "WHAT ARE YOU TALKING ABOUT?"
    papyrus "IF WE RESET THE TIMELINE EVERY SINGLE TIME I DAMAGE PEOPLE, THEIR LIFE BECOME TRIVIAL"
    papyrus "I DON'T WANT TO THEIR LIFE TO BE TRIVIAL"
    show papyrusImg coolDude angry flip
    papyrus "I HAVE TO PAY FOR MY ACTIONS!"
    gaster "NO, NO"
    gaster "I WILL NOT"
    toriel "Papyrus!"
    hide gaster
    show papyrusImg coolDude realizing
    pause(1.0)
    show torielImg teacher worried at fade:
        xpos 0.1
    toriel "Where's Sans?"
    toriel "Why..."
    toriel "Why are ashes in your clothes?"
    papyrus "TORIEL..."
    show papyrusImg coolDude realizing flip
    papyrus "I..."
    gaster "I'M SORRY PAPYRUS"
    gaster "I UNDERSTAND WHAT ARE YOU FEELING BUT"
    gaster "IF I CAN AVOID A WORLD IN WHICH ONE OF MY CHILDREN IS DEAD"
    gaster "I WILL"
    show papyrusImg coolDude angry flip
    papyrus "NO"
    show papyrusImg coolDude angry
    papyrus "GASTER WAI"
    $ resets += 1
    $ papyrusMourn = True
    jump day1
    return
  
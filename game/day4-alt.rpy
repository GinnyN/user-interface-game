 label alphysTalksToSans:
    hide torielImg
    alphys "Sans, I need to talk with you about something"
    show sansImg hoddie surprised flip
    sans "really?"
    alphys "Yes, it`s something important..."
    stop music fadeout(1)
    scene black with dissolve
    pause(0.5)
    play music "music/22 Snowdin Town.mp3" fadein 1
    pause(1)
    scene skelebroHouse outside with dissolve
    show papyrusImg uhh flip at fade with dissolve:
        xpos -0.1
    papyrus "I WONDER IF DR ALPHYS GOT ANYTHING DONE"
    papyrus "TODAY IT`S THE LAST DAY, I NEED THAT PROGRAM"
    show sansImg hoddie angry flip at fade with dissolve:
        xpos 0.3
    sans "hello bro"
    show papyrusImg scared
    papyrus "SANS!" 
    show papyrusImg sorry
    papyrus "WHERE HAVE YOU BEEN?"
    sans "i was talking with alphys and she told me something very..."
    sans "very"
    sans "interesting"
    papyrus "OH"
    show papyrusImg surprised
    papyrus "AHHHHHHHHH"
    sans "i know you are unable to do things quietly"
    sans "so i think is better to explain what`s going on"
    show papyrusImg annoyed
    papyrus "I CAN`T"
    papyrus "YOU WILL NOT BELIEVE ME!"
    show alphysImg casual angry flip at fade with dissolve:
        xpos 0.5
        ypos -0.2
    alphys "It`s a complex machine"
    alphys "but your story about this being trapped somewhere in the universe, is even more intriging"
    papyrus "I KNOW IT'S WEIRD"
    papyrus "BUT I KINDA CANNOT TELL YOU"
    show papyrusImg annoyed flip
    papyrus "SO I WILL NOT CONTINUE"
    show sansImg hoddie worried flip
    sans "come on bro"
    sans "don´t make this more difficult than it should be"
    show papyrusImg sorry
    papyrus "YOU WILL KNOW EVERYTHING ONCE I FINISH WITH THIS, I PROMISE!"
    alphys "Do you?"
    if alphysFailState:
        alphys "Then I will not start progress unless you tell us what's going on!"     
        show papyrusImg surprised
        papyrus "YOU HAVE NOT DID ANYTHING?"
        alphys "Of course not!"
        alphys "I need to know where did you get all of this!"
        show alphysImg casual confused flip
        alphys "Plus I was busy and I didn't have any time?"
        show papyrusImg dissapointed
        papyrus "THIS IS NOT GOOD"
        gaster "INDEED MY DEAR PAPYRUS"
        gaster "TODAY IS THE LAST DAY, WE CANNOT WAIT ANY LONGER"
        papyrus "I KNOW"
        show sansImg hoddie surprised flip
        sans "to whom are you speaking to?"
        papyrus "GASTER"
        dtSans "Gaster?"
        alphys "Who?"
        show papyrusImg annoyed
        papyrus "BUT IT DOESN'T MATTER IF I TELL YOU, WE WILL HAVE TO RESET ANYWAYS"
        gaster "THAT'S CORRECT"
        gaster "WE'RE GOING TO HAVE TO DISCUSS IT AT THE END OF THE FIRST DAY"
        gaster "GOOD LUCK"
        alphys "But who..."
        $ alphysFailStateBoleean = True
        $ resets += 1
        jump day1
    else:
        alphys "Here! I have the pendrive with the program right here"
        alphys "But I will not give it to you until you explain yourself"
        papyrus "!?"
        papyrus "DR ALPHYS, PLEASE"
        papyrus "I..."
        papyrus "I..."
        sans "..."
        show sansImg hoddie worried flip
        sans "papyrus..."
        sans "you has been very suspicious lately"
        sans "are you"
        extend " traveling in time?"
        show papyrusImg surprised
        show alphysImg casual confused flip
        alphys "Hey!"
        alphys "What are you talking about?"
        gaster "THE ANSWER WILL BE YES,  MY DEAR SANS"
        show sansImg hoddie surprised flip
        show alphysImg casual noWords flip
        show papyrusImg sorry
        sans "!?"
        alphys "But, who's...'"
        gaster "BUT THE HUMANS HAVE AN ESPECIFIC TERM FOR THIS KIND OF TRAVEL"
        show sansImg hoddie surprised
        gaster "THEY CALL IT 'GROUNDHOG DAY LOOP'"
        show sansImg hoddie surprised flip
        show alphysImg casual noWords
        gaster "AFTER A MOVIE, I'LL BET"
        show papyrusImg curious
        papyrus "!!!!!!!"
        papyrus "HOMEWORK GRABING ATTACK!!!"
        "And Papyrus grabs the pendrive from Alphys hands, like a dog"
        alphys "What?!"
        "Papyrus run away"
        alphys "Do you know who was that voice?"
        sans "yes"
        sans "..."
        sans "but i can't tell you"
        alphys "Ok, what´s going on with you skeletons and your secrets?"
        sans "this is the main reason i don´t like to involve anyone else"
        "Sans goes away"
        alphys "But..."
        alphys "but..."
        alphys "I DESERVE AN EXPLANATION"
        "Cuts to Papyrus more in the forest"
        papyrus "HOW ARE YOU DOING THAT?"
        gaster "IT SEEMS, MY DEAR PAPYRUS, THAT I CAN PROJECT MY VOICE DURING THIS DAY TO THE REST OF THE WORLD"
        gaster "I SHOULD NOT DO THAT AGAIN, UNLESS THERE'S AN SPECIFIC NEED"
        papyrus "BUT I HAVE THE PENDRIVE"
        papyrus "THIS SHOULD RETURN YOUR BODY TO YOUR NATURAL STATE"
        gaster "ARE YOU SURE MY DEAR BOY?"
        papyrus "OF COURSE!"
        papyrus "DR ALPHYS IS THE SMARTEST MONSTER OF NEWER HOME"
        papyrus "I´M PRETTY SURE SHE COULD MADE IT WHILE WATCHING THE LAST EPISODE OF KISSY CUTIE MEW MEW AND HAVING ONE HAND TIED TO HER BACK"
        gaster "I DON'T KNOW WHAT ARE YOU TALKING ABOUT, BUT I TRUST YOU"
        gaster "MOVE POST HASTE! SO WE SHALL END THIS NIGHTMARE ONCE AND FOR ALL!"
        papyrus "YES SIR!"
        "Papyrus ran away. Sans appears just behind him"
        if gasterPapyrusSansDad:
            sans "i knew it"
            sans "but how papyrus is in the middle of all of this"
            sans "i'd better figure out"
        else:
            sans "that ham was definitely his"
            sans "but how?"
            sans "and why papyrus?"
            sans "argh!"
        $ program = True
        $ tryWithAlphys = False
    return
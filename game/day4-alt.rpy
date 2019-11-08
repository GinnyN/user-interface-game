label alphysTalksToSans:
    hide torielImg
    alphys "Sans, I need to talk with you about something"
    show sansImg hoddie surprised flip
    sans "really?"
    alphys "Yes, it`s something important..."

label getPenFromAlphys:
    $ penAtAlphys = False
    $ tryWithAlphys = False
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
    play music "music/15 sans.mp3" fadein(1)
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
        stop music
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
        jump day1
    else:
        if firstTry:
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
            play music "music/24 Bonetrousle.mp3" fadeout 1
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
            scene day4 homeworkAttack with vpunch
            alphys "What?!"
            play sound "music/fx/steps.wav"
            show alphysImg casual noWords at fade with dissolve:
                xpos 0.1
                ypos -0.2
            alphys "Do you know who was that voice?"
            show sansImg hoddie angry at fade with dissolve:
                xpos 0.0
            sans "yes"
            sans "..."
            sans "but i can't tell you"
            show alphysImg casual angry flip
            alphys "Ok, what´s going on with you skeletons and your secrets?"
            sans "this is the main reason i don´t like to involve anyone else"
            hide sansImg
            play sound "music/fx/steps.wav"
            show alphysImg casual angry
            alphys "But..."
            show alphysImg casual angry flip
            alphys "but..."
            hide alphysImg
            alphys "I DESERVE AN EXPLANATION"
            stop music fadeout(1.0)
            scene black with dissolve
            pause(1.0)
            play music "music/33 Quiet Water.mp3" fadein(1) fadeout(1) 
            scene forest with dissolve
            show papyrusImg annoyed at fade with dissolve:
                xpos 0.1
            papyrus "HOW ARE YOU DOING THAT?"
            gaster "IT SEEMS, MY DEAR PAPYRUS, THAT I CAN PROJECT MY VOICE DURING THIS DAY TO THE REST OF THE WORLD"
            gaster "I SHOULD NOT DO THAT AGAIN, UNLESS THERE'S AN SPECIFIC NEED"
            show papyrusImg delight
            papyrus "BUT I HAVE THE PENDRIVE"
            papyrus "THIS SHOULD RETURN YOUR BODY TO YOUR NATURAL STATE"
            gaster "ARE YOU SURE MY DEAR BOY?"
            show papyrusImg serious
            papyrus "OF COURSE!"
            show papyrusImg delight
            papyrus "DR ALPHYS IS THE SMARTEST MONSTER OF NEWER HOME"
            show papyrusImg checkThis
            papyrus "I´M PRETTY SURE SHE COULD MADE IT WHILE WATCHING THE LAST EPISODE OF KISSY CUTIE MEW MEW AND HAVING ONE HAND TIED TO HER BACK"
            gaster "I DON'T KNOW WHAT ARE YOU TALKING ABOUT, BUT I TRUST YOU"
            gaster "MOVE POST HASTE! SO WE SHALL END THIS NIGHTMARE ONCE AND FOR ALL!"
            hide papyrusImg
            papyrus "YES SIR!"
            pause(1.0)
            show sansImg hoddie angry at fade with dissolve:
                xpos 0.3
            if gasterPapyrusSansDad:
                sans "i knew it"
                sans "but how papyrus is in the middle of all of this"
                sans "i'd better figure out"
            else:
                sans "that ham was definitely his"
                sans "but how?"
                sans "and why papyrus?"
                sans "argh!"
            hide sansImg
            $ program = True
            $ tryWithAlphys = False
        else:
            alphys "Then I will not start progress unless you tell us what's going on!"
            papyrus "WHAT?"
            papyrus "BUT HALF OF THE PROGRESS IS ALREADY DONE!"
            alphys "Well, yes, that code is mine"
            alphys "Somehow..."
            alphys "But I still cannot figure out what the variables 'undyne' do"
            alphys "I think is going to be easier if I do everything again"
            sans "wait, do you call your variables after your crushes?"
            alphys "Why, you don't?"
            sans "i mean, if i never wanna understand what i did, yes, i might"
            alphys "It's... it's just..."
            alphys "I'm not good at variables names... so... I just use the first word it comes in my mind"
            "..."
            papyrus "AW.... THAT'S ADORABLE..."
            sans "yes... it's adorable..."
            "..."
            alphys "Ok, I'll use a thesaurus next time"
            papyrus "WELL, AT LEAST I TRIED"
            papyrus "I'M OUT!"
            "Papyrus leaves"
            sans "wait... wait... papyrus where you going?"
            "Sans leaves"
            alphys "Nah, I'm not going to do that"
            $ endingSans = True
        jump endingResolve
    return
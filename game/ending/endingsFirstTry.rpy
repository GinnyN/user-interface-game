label endingsFirstTry:
    stop music fadeout(1.0)
    scene black with dissolve
    pause(1.0)
    play music "music/47 Ooo.mp3" fadein 1
    scene wekufeLab with dissolve
    show papyrusImg annoyed flip at fade with dissolve:
        xpos 0.4
    papyrus "ARE THE WEKUFES GONE?"
    show gaster trapped oh at fade with dissolve:
        xpos -0.1
    gaster "YES, THEY ARE"
    gaster "I CANNOT FIND ANY, MOST PROBABLY THEY ARE GONE"
    show papyrusImg delight
    papyrus "IT'S TIME TO SET THIS ON!"
    hide papyrusImg
    pause(1.0)
    show papyrusImg explainingPointing at fade with dissolve:
        xpos 0.4
    papyrus "IT'S GOING TO TAKE A COUPLE OF MINUTES TO LOAD"
    show papyrusImg delight flip
    papyrus "ARE YOU EXCITED?!"
    gaster "I CANNOT SHAKE THIS FEELING WE ARE FORGETING SOMETHING"
    show papyrusImg worried flip
    papyrus "DO YOU WANT TO STOP THE PROCESS?"
    show gaster trapped explain
    gaster "NO, NO"
    show gaster trapped oh
    gaster "I MIGHT BE JUST PARANOID"
    show papyrusImg delight flip
    papyrus "WHAT DO YOU THINK IS GOING TO HAPPEN WHEN YOU COME BACK?"
    papyrus "PEOPLE WILL REMEMBER YOU, LIKE YOU WERE NEVER GONE?"
    papyrus "I'LL REMEMBER EVERYTHING ABOUT SCIENCE?"
    gaster "I'LL BLOW UP IN MILLIONS OF SMALL PIECES AND I'LL COVER ALL THE BUILDINGS OF THE NEW MONSTERS KINGDOM IN A WHITE POWDER?"
    show papyrusImg annoyed flip
    papyrus "GASTER!"
    show gaster trapped sorry
    gaster "IT'S BETWEEN THE REALM OF POSSIBILITY"
    papyrus "NOW I'M FINISHING DEALING WITH SANS'S LAZINESS, I'LL HAVE TO DEAL WITH YOUR NEGATIVENESS?"
    show gaster trapped oh
    gaster "IS IT THAT A WORD?"
    gaster "..."
    show gaster trapped maybe
    gaster "WELL, I TOLD YOU, I'M A BIT PARANOID AT TIMES"
    papyrus "NYEH.."
    show papyrusImg delight flip
    papyrus "I CANNOT WAIT FOR THAT!"
    show gaster trapped happy
    gaster "MY DEAR PAPYRUS..."
    sans "this is the lab i told you about"
    show papyrusImg scared flip
    show gaster trapped oh flip
    papyrus "SANS?"
    gaster "LET'S ME SEE..."
    scene day4 sansFriskWekufeLab with dissolve:
        ypos 0.0
        linear 10 ypos -0.95
    pause(1)
    show friskImg worried at fade with dissolve:
        xpos 0.3
        ypos 0.15
    frisk "You sure they are here..."
    show sansImg hoddie worried at fade with dissolve:
        xpos 0.1
    sans "i'm not sure if papyrus is with someone"
    sans "i just know papyrus came here"
    sans "and that i know that voice..."
    show friskImg worried flip
    frisk "Someone you knew from before?"
    sans "a... friend..."
    frisk "Is it their name..."
    frisk "Gaster?"
    show sansImg hoddie surprised
    sans "how do you know that?"
    frisk "I found a monster"
    frisk "In greyscale"
    frisk "Who commented me about it"
    sans "oh..."
    show friskImg worried
    frisk "I think it was a malfunction..."
    show sansImg hoddie worried
    sans "on reality?"
    frisk "..."
    show friskImg worried flip
    frisk "Yeah..."
    sans "well.."
    sans "we better found them"
    sans "papyrus has been very weird lately"
    frisk "Did you noticed?"
    show sansImg hoddie sideglance
    sans "ehh..."
    sans "i thought it was just him been him"
    sans "he always does weird stuff..."
    hide friskImg
    frisk "I don't think so.."
    show sansImg hoddie surprised
    sans "wait..."
    hide sansImg
    sans "frisk..."
    scene wekufeLab with dissolve
    show papyrusImg annoyed flip at fade with dissolve:
        xpos 0.4
    show gaster trapped oh at fade with dissolve:
        xpos -0.1
    gaster "THEY ARE SANS AND THE FALLEN HUMAN"
    papyrus "THEIR NAME IS FRISK"
    show papyrusImg uhh flip
    papyrus "WAIT"
    papyrus "WHY AM I GETTING UPSET AT YOU CALLING FRISK FALLEN HUMAN?"
    show papyrusImg annoyed flip
    papyrus "AND WHY DO YOU NOT CALL THEM BY THEIR NAME?"
    show gaster trapped happy
    gaster "YOU ARE ALREADY GETTING SOME OF YOUR MEMORY BACK"
    gaster "IT'S NOT CONVENIENT FOR ME, BUT MEMORY IS MEMORY"
    show papyrusImg delight
    papyrus "IT HAS FINISHED LOADING!"
    show gaster trapped oh
    gaster "WE MUST DECIDE IF WE CONTINUE"
    gaster "DO WE?"
    jump endingMenuFirstTry

label endingMenuFirstTry: 
    menu:
        "Of Course!":
            jump startEndingGasterFirstTry
        "I have 2nd thoughts":
            jump resetOrEndingFirstTry

label startEndingGasterFirstTry:
    $ firstTry = False
    show papyrusImg delight flip
    papyrus "OF COURSE!"
    papyrus "LET'S DO THIS!"
    stop music fadeout(1)
    show gaster trapped happy
    show papyrusImg delight
    papyrus "I PRESS ENTER!"
    gaster "AND NOW WE..."
    scene white with dissolve
    play sound "music/fx/iau.wav"
    pause(2)
    scene day4 gasterFree with dissolve:
        ypos -1.0
        linear 1 ypos -0.3
    pause(2)
    gaster "IT WORKED"
    show gaster free happy at fade with dissolve:
        xpos -0.1
    gaster "IT WORKED PAPYRUS!"
    gaster "..."
    show gaster free surprised
    gaster "PAPYRUS!"
    play music "music/81 An Ending.mp3" fadein(5)
    scene day4 papyrusTrapped with dissolve:
        ypos -0.8
        linear 10 ypos -0.1
    pause(1)
    papyrus "I THINK THERE'S SOMETHING WE DIDN'T ACCOUNT FOR"
    show gaster free worried at fade with dissolve:
        xpos -0.1
    gaster "OH... NO..."
    show papyrusImg trapped sad flip at fade with dissolve:
        xpos 0.4
    papyrus "IF YOU ASK ME..."
    papyrus "I THINK WE NEED TO LEARN MORE..." 
    papyrus "ABOUT..." 
    papyrus "WHAT..." 
    papyrus "IS BEYOND..." 
    papyrus "THE DARKNESS..."
    gaster "THERE'S NOTHING WE CAN COMPREHEND FROM THERE"
    show papyrusImg trapped angry flip
    papyrus "I REFUSE THAT STATEMENT!"
    gaster "IT DOESN'T HAVE TO BE YOU"
    hide gaster
    pause(1)
    gaster "THE SYSTEM SAYS THERE'S SOME DETERMINATION LEFT"
    show gaster free happy at fade with dissolve:
        xpos -0.1
    gaster "WE CAN RESET TO TRY AGAIN!"
    show papyrusImg trapped sad flip
    papyrus "THAT'S NOT AN OPTION WE CAN TAKE"
    show gaster free worried
    gaster "I KNOW..."
    gaster "BUT PLEASE, SHOW THEM THE MENU..."
    gaster "THEY MIGHT WANT TO TRY"
    menu:
        "Reset":
            show gaster free happy
            gaster "OH, THANKS YOU!"
            gaster "WE WILL TALK IN THE PAST, MY DEAR PAPYRUS..."
            show papyrusImg trapped sad
            papyrus "..."
            $ firstTry = True
            jump day1
        "Continue":
            gaster "NO..."
            show papyrusImg trapped happy flip
            papyrus "DO NOT WORRY ABOUT ME!"
            papyrus "YOU..." 
            show papyrusImg trapped sad flip
            papyrus "WILL..." 
            papyrus "FIND..." 
            papyrus "A..."
            show gaster free angry
            gaster "WHAT IF I DON'T?"
            gaster "WHAT IF I DIE AND YOU ARE STILL TRAPPED IN THE DARKNESS!?"
            show papyrusImg trapped happy flip
            papyrus "I KNOW YOU'LL DO YOUR BEST..."
            gaster "WHAT IS IT NOT GOOD ENOUGH?!"
            show papyrusImg trapped sad flip
            papyrus "..."
            papyrus "YOU WORRY TOO MUCH"
            papyrus "I'M NOT OK WITH THIS"
            papyrus "BUT I..." 
            papyrus "CAN HANDLE IT"
            papyrus "I WILL HANDLE IT!"
            show gaster free worried
            gaster "I KNOW YOU ARE STRONG PAPYRUS"
            gaster "WHAT I DON'T KNOW IF I AM AS STRONG AS YOU ARE"
            show papyrusImg trapped angry flip
            papyrus "YOU HAVE ALREADY DONE THIS!"
            papyrus "WHY ARE YOU ASKING?!"
            show gaster free surprised
            show papyrusImg trapped happy flip
            frisk "Papyrus!?"
            scene day4 sansFriskFindPapyrusGaster with dissolve:
                xpos 0.0
                linear 20 xpos -0.25
            pause(2.0)
            frisk "What's happened to you?"
            show friskImg angry mild flip zorder 5 at fade with dissolve:
                xpos 0.4
                ypos 0.15
            frisk "What you did to him!?"
            show papyrusImg trapped sad flip zorder 3 at fade with dissolve:
                xpos 0.4
            papyrus "HE WAS TRAPPED IN THE DARKNESS"
            show friskImg worried
            papyrus "WE GOT HIM..."
            papyrus "OUT.."
            show gaster free worried zorder 2 at fade with dissolve:
                xpos -0.1
            gaster "BUT IT SEEMS IT NEEDS A MONSTER FOR SOME REASON"
            show friskImg worried flip
            gaster "SO, PAPYRUS HAS TOOK MY PLACE"
            gaster "BY ACCIDENT"
            show sansImg hoddie surprised flip zorder 4 at fade with dissolve:
                xpos 0.2
            dtSans "That's why you are here?"
            show sansImg hoddie surprised
            dtSans "That what you were doing?"
            papyrus "YES, I DIDN'T TELL YOU..."
            papyrus "I THOUGHT WOULD BE..."
            show papyrusImg trapped sad
            papyrus "USELESS..."
            papyrus "I GUESS..."
            show papyrusImg trapped sad flip
            gaster "THE LOOP WAS TOO SHORT"
            show sansImg hoddie surprised flip
            gaster "IT WASN'T FEASIBLE"
            sans "but... at least..."
            papyrus "NOT FOR LONG"
            papyrus "FRISK!"
            hide gaster
            hide sansImg
            show friskImg worried zorder 5 at fade with dissolve:
                xpos 0.0
                ypos 0.15
            papyrus "PLEASE TAKE CARE OF THIS BONEHEADS"
            frisk "Why are you saying that?"
            gaster "THE COMPUTER!"
            gaster "I FORGOT THE COMPUTER!"
            papyrus "PLEASE, MAKE SURE SANS DOES NOT LAZY AROUND TOO MUCH"
            papyrus "AND TAKE THE W.D. IN A TRIP BEFORE ANYTHING"
            papyrus "HE NEEDS TO SEE THE SURFACE BEFORE LOCKING HIMSELF IN A LAB"
            frisk "Sure"
            show friskImg happy
            frisk "And then we will get you out of there, right?"
            show papyrusImg trapped happy flip
            papyrus "EXACTLY"
            papyrus "YOU ALWAYS GET..."
            play sound "music/fx/iau.wav"
            hide papyrusImg with pixellate
            show friskImg surprised
            frisk "What happened?"
            show gaster free worried zorder 3 at fade with dissolve:
                xpos 0.2
            gaster "THE COMPUTER WAS PROGRAMMED TO FRY ITSELF"
            gaster "WITHOUT THIS COMPUTER, THERE'S NO WAY WE CAN COMMUNICATE WITH PAPYRUS ANY LONGER"
            show sansImg hoddie worried zorder 4 at fade with dissolve:
                xpos 0.5
            dtSans "That... means..."
            dtSans "..."
            dtSans "..."
            show gaster free compassionate
            gaster "SANS... MY DEAR BOY..."
            gaster "LET'S GO BACK"
            hide gaster
            hide sansImg
            show friskImg worried flip
            gaster "WE HAVE A LOT TO THINK AND CRY BEFORE ANYTHING"
            hide friskImg
            stop music fadeout(2.0)
            pause(2.0)
            jump neutralEndingGaster
            
    
label resetOrEndingFirstTry:
    show papyrusImg annoyed flip
    papyrus "WHY IS THAT OPTION THERE?"
    gaster "DO YOU NOT HAVE 2ND THOUGHTS?"
    papyrus "I MEAN..."
    show papyrusImg confused flip
    papyrus "I SHOULD TRUST EVERYTHING IS GOING TO BE ALRIGHT"
    show papyrusImg annoyed flip
    papyrus "RIGHT?"
    gaster "I DON'T KNOW"
    papyrus "HOW YOU DO IT?"
    show gaster trapped maybe
    gaster "I ALWAYS HAVE 2ND THOUGHTS"
    show gaster trapped oh
    gaster "I MOSTLY IGNORE THEM OR ELSE I WILL GET NOTHING DONE"
    papyrus "SO..."
    papyrus "IT SEEMS WE CANNOT TRUST ANY OF OUR METAPHORICAL GUTS"
    gaster "I KNOW IT JUST GOING TO DEPEND ON WHAT IS BEYOND OUR COMPREHENSION"
    papyrus "YOU MEAN"
    gaster "EXACTLY"
    gaster "THEY ARE ALL POWERFULL AND ALL CURIOUS AFTER ALL"
    menu:
        "Reset":
            papyrus "THEY WANT TO STILL POKE AROUND?"
            show gaster trapped sorry
            gaster "I SHALL NOT DELAY THIS ANY MORE"
            $ resetWithoutMeaning = True
            jump day1
        "Use the Program Anyway":
            show papyrusImg dissapointed flip
            papyrus "I DO NOT UNDERSTAND"
            show gaster trapped maybe
            gaster "NEITHER DO I BUT OK"
            show gaster trapped explain
            gaster "FIRE THE PROGRAM AWAY!"
            jump startEndingGasterFirstTry
        "Do not use the Program":
            papyrus "..."
            papyrus "..."
            papyrus "..."
            papyrus "..."
            papyrus "..."
            papyrus "..."
            show papyrusImg angry
            papyrus "WHO'S STOPING ME?"
            show gaster trapped angry
            gaster "PAPYRUS?"
            gaster "WHAT ARE YOU DOING?"
            papyrus "I'M GOING TO FIRE THE PROGRAM!"
            show gaster trapped sorry
            gaster "THERE'S NO NEED PAPYRUS.."
            show papyrusImg angry flip
            papyrus "SCREW THEIR CURIOSITY!"
            papyrus "I WILL NOT LET THEM KNOW WHAT'S GOING TO HAPPEN IF I CAN MANAGE IT"
            papyrus "NOW I HAVE THE POWER TO CHANGE SOMETHING FOR THE BETTER"
            papyrus "I WILL NOT LET AN ENTITLED"
            papyrus "BEING..." 
            show papyrusImg uhh flip
            papyrus "BEYOND..." 
            show papyrusImg angry flip
            papyrus "THAT TO TOY WITH US!"
            gaster "I GUESS THERE'S NO WAY TO STOP YOU NOW"
            pause(1)
            show gaster trapped explain
            gaster "FIRE THE PROGRAM AWAY!"
            jump startEndingGasterFirstTry
return 

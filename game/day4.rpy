label day4:
    $ day = 4
    scene black with dissolve
    play music "music/05 Ruins.mp3" fadein 1 fadeout 1
    pause(1)
    scene toriel house with dissolve
    show torielImg teacher worried zorder 2 at fade:
        xpos 0.0
    show alphysImg casual neutral flip zorder 3 at fade:
        xpos 0.3
        ypos -0.2
    toriel "Did you find anything about those human traffickers?"
    alphys "Everything we found is in the cloud, we just need to send them to the humans` authorities"
    show torielImg teacher neutral
    toriel "Good"
    show alphysImg casual nostalgic flip
    alphys "What are we going to do with those monsters the kids are saying they brought them?"
    show torielImg teacher unsure
    toriel "That`s complicated"
    show torielImg teacher worried
    toriel "We started this trying to avoid what Papyrus did affect our relationship with the humans"
    toriel "But now more monsters are involved"
    toriel "And we have no idea what those monsters want to do with those poor kids"
    show sansImg hoddie neutral flip zorder 3 at fade:
        xpos 0.6
        ypos -0.05
    sans "hi"
    show alphysImg casual neutral zorder 3 at fade:
        xpos 0.1
        ypos -0.2
    show torielImg teacher neutral
    toriel "Oh, Sans!"
    toriel "Did you finish what I asked you?"
    show alphysImg casual neutral flip
    alphys "You asked him something?"
    show alphysImg casual neutral
    sans "she asked me to figure out if there some weird buildings in mount ameni"
    sans "i found something"
    show sansImg hoddie unsure flip
    sans "and i had to run away for my life"
    show torielImg teacher worried
    show alphysImg casual tired
    toriel "Oh Sans"
    show sansImg hoddie neutral flip
    sans "i`m ok. they just saw me"
    sans "they`re probably going to check for those kids they had in the cave"
    show sansImg hoddie annoyed flip
    sans "i`m the worst spy you could find, been honest"
    toriel "What we`re going to do now?"
    show sansImg hoddie neutral flip
    sans "beats me"
    alphys "Yes..."
    alphys "They will be certainly angry if they find we already rescue those kids"
    toriel "One part of me wants to talk with those monsters and give them a chance"
    show torielImg teacher angry
    toriel "Another wants to roast them for make those poor kids suffer like that"
    show alphysImg casual nostalgic flip
    show sansImg hoddie sideglance flip
    alphys "OK, ok, I got it"
    sans "hehehehehehe..."
    show torielImg teacher worried
    toriel "Maybe we should just capture them and work on rehabilitation"
    toriel "We can`t have them still capturing kids just because"
    show sansImg hoddie neutral flip
    sans "it must be a reason"
    sans "i`m not saying that justify it"
    sans "i`m just saying that they must need so many kids for some sort of weird plan"
    show alphysImg casual neutral
    alphys "And you think that because..."
    sans "just a hunch"
    show torielImg teacher worried
    toriel "Then we will just have to storm the place"
    toriel "It`s the quicker way to end with all this situation"
    toriel "I`ll call Asgore"

    if penAtAlphys:
        jump alphysTalksToSans
        
    if resets == 0:
        jump meetingGaster
    
    if program and firstTry:
        jump endingsFirstTry
    
    if not firstTry:
        jump endingResolve
    else:
        jump endingNothing
        
label endingNothing:
    scene black with dissolve
    pause(1.0)
    gaster "THIS IS THE FINAL DAY"
    gaster "PAPYRUS, I'M GOING TO RESET THE TIMELINE"
    gaster "PLEASE BE CAREFUL"
    jump day1

label meetingGaster:
    stop music fadeout(1)
    scene black with dissolve
    pause(1)
    scene skelebroHouse outside with dissolve
    show papyrusImg coolDude thinking zorder 0 at fade:
        xpos 0
    papyrus "I HAVE THIS TINGLING SENSATION THAT THEY WILL NOT ALLOW ME TO JOIN WHATEVER THEY WANT TO DO TODAY"
    papyrus "EVEN IF I WAS RIGHT YESTERDAY, THEY HAVE A POINT"
    papyrus "A REALLY SMALL POINT, BUT STILL"
    papyrus "..."
    papyrus "SOMETIMES I WONDER IF THEY HAVE MEETINGS WHICH I DON'T GET INVITED..."
    papyrus "OR THE INVITATION WAS LOST IN THE MAIL???"
    show papyrusImg coolDude explaining
    papyrus "I ALWAYS SEEM TO MISS SOME CRUCIAL INFORMATION OR SOMETHING"
    play music "music/47 Ooo.mp3" fadein 1
    pause(1)
    show papyrusImg coolDude surprised
    papyrus "?!"
    papyrus "AHHHHHH????!!!!"
    papyrus "FROM WHERE THIS IS COMING FROM..."
    scene mistColor with dissolve
    show mist zorder 0 at fade
    "???" "{font=fonts/NewAster.ttf} {cps=*0.2} MY... BO... CO... HE... CLO...{/cps}{/font}"
    show papyrusImg coolDude surprised zorder 1 at fade:
        xpos 0
    papyrus "A VOICE!"
    papyrus "DO YOU NEED HELP?!"
    papyrus "WHERE DO I GO?!"
    "???" "{font=fonts/NewAster.ttf}{cps=*0.2} HE... THIS... YYYY {/cps}{/font}"
    papyrus "THAT WAY?"
    papyrus "JUST WAIT MISTER! I'M COMING FOR YOU!"      
    hide papyrusImg
    play sound "music/fx/steps.wav"
    pause(1)
    show papyrusImg coolDude thinking zorder 1 at fade:
        xpos 0
    papyrus "MISTER! CAN YOU TELL ME IF I'M CLOSE!?"
    "???" "{font=fonts/NewAster.ttf} {cps=*0.5}THAT WAY MY... YES.. YOU ARE... CLOSER... {/cps}{/font}"
    show papyrusImg coolDude delight
    papyrus "GOOD TO KNOW!"
    hide papyrusImg
    play sound "music/fx/steps.wav"
    papyrus "HELP ON THE WAY!"
    scene wekufeLab with dissolve:
        ypos 0.0
        linear 20 ypos -0.3
    pause(1.0)
    stop music fadeout(1)
    show papyrusImg coolDude surprised zorder 1 at fade:
        xpos 0
    papyrus "WOWIE..."
    papyrus "WHAT IS THIS?!"
    "???" "{font=fonts/NewAster.ttf}PAPYRUS! MY DEAR BOY! YOU MADE IT!{/font}"
    papyrus "?!"
    scene day4 gaster with dissolve:
        ypos -0.5
        linear 5 ypos 0.0
    pause(3.0)
    papyrus "AN ANALGAMATE?!"
    "???" "{font=fonts/NewAster.ttf} AH? NO NO MY DEAR PAPYRUS... {/font}"
    "???" "{font=fonts/NewAster.ttf} DON'T YOU REMEMBER ME? {/font}"
    "???" "{font=fonts/NewAster.ttf} I'M YOUR OLD FRIEND AND FORMER BOSS IN THE ROYAL LABORATORY {/font}"
    gaster "W.D. GASTER"
    stop music fadeout(1)
    play music "music/gaster theme.MP3" fadein 1
    pause(5)
    papyrus "WHO ARE YOU AGAIN?"
    stop music
    scene wekufeLab with hpunch
    play sound "music/fx/thump.wav"
    gaster "YOU DEFINITELY DO NOT REMEMBER ME..."
    show gaster trapped dissapointed flip zorder 1 at fade:
        xpos 0.4
    show papyrusImg coolDude thinking zorder 1 at fade:
        xpos -0.1
    papyrus "SHOULD I?"
    show gaster trapped angry flip
    gaster "YES, YES, YOU SHOULD"
    gaster "BEFORE I DISSAPEARED"
    gaster "I INJECTED ENOUGH DETERMINATION IN YOU AND SANS FOR BOTH TO SURVIVE WITH YOUR MEMORIES INTACT"
    show gaster trapped dissapointed flip
    gaster "IT SEEMS YOUR LEVELS WEREN'T HIGH ENOUGH"
    gaster "WHICH I FOUND HIGHLY SUSPICIOUS"
    show papyrusImg coolDude careful
    papyrus "I DON'T FOLLOW"
    show papyrusImg coolDude thinking
    papyrus "CAN YOU START FROM WAAAAYYY BEFORE THAT"
    show gaster trapped ok flip
    gaster "WELL, SINCE WE HAVE A PROBLEM WITH MEMORY LOSS, I MUST START FROM THE BEGINNING THEN"
    show gaster trapped ehem flip
    gaster "EHEM!"
    play music "music/gaster theme.MP3" fadein 1
    show papyrusImg coolDude thinking zorder 1 at fade:
        xpos -0.1
    show gaster trapped neutral flip zorder 1 at fade:
        xpos 0.4
    gaster "MY NAME IS W.D. GASTER"
    gaster "AND I WAS THE OLD ROYAL SCIENTIST BEFORE THE CURRENT ONE"
    gaster "BETWEEN MY ACCOMPLISHMENT ARE THE CORE AND THE DT EXTRACTOR"
    show papyrusImg coolDude surprised happy
    papyrus "THE CORE???!!"
    papyrus "DID YOU BUILD THE CORE?!!"
    show gaster trapped proud flip
    gaster "I DESIGN IT"
    gaster "THE CONSTRUCTION DUTIES WENT TO DIFFERENT VERY TALENTED PEOPLE, MOST OF THEM FIRE ELEMENTALS"
    show papyrusImg coolDude delight
    papyrus "WOWIE!"
    show gaster trapped dissapointed flip
    gaster "WHERE WAS I?"
    show gaster trapped proud flip
    gaster "OF COURSE"
    show papyrusImg coolDude neutral
    show gaster trapped neutral flip
    gaster "BETWEEN MY DUTIES WAS TRYING TO FIND A WAY TO SHATTER THE BARRIER WHICH KEPT US UNDERGROUND"
    gaster "BUT MY STUDIES FOUND IT WAS IMPOSSIBLE UNLESS A MONSTER ABSORB ENOUGH HUMANS SOULS IN THE PROCESS"
    show gaster trapped sorry flip
    gaster "THAT WASN'T GOOD ENOUGH FOR THE QUEEN I'M AFRAID"
    show gaster trapped neutral flip
    gaster "SO I KEPT SEARCHING..."
    show gaster trapped sorry flip
    gaster "WE EVEN WENT BACK TO WAR..."
    show gaster trapped proud flip
    gaster "BUT EVENTUALLY I COULD FIGURE OUT A WAY TO OBTAIN DETERMINATION FROM BEYOND THE REALITY, WHERE EVERYTHING IS SHROUDED IN DARKNESS"
    show papyrusImg coolDude thinking
    papyrus "BEYOND..."
    papyrus "REALITY?"
    show gaster trapped explain flip
    gaster "AT LEAST THAT WAS THE HYPOTESIS, SO WE TRIED OUT SEVERAL EXPERIMENTS"
    show gaster trapped sorry flip
    gaster "WE FORGOT THEM ALMOST IMMEDIATLY"
    show gaster trapped explain flip
    gaster "UNTIL ONE OF MY ASSISTANTS DECIDED TO INJECT HIMSELF WITH DETERMINATION"
    show papyrusImg coolDude careful
    papyrus "THEY... "
    papyrus "MELTED AWAY TOO?"
    show gaster trapped dissapointed flip
    gaster "NO"
    gaster "SORRY, BUT THIS WAS COMMON KNOWLEDGE IN THE OLD MONSTER SCIENTIFIC COMMUNITY"
    gaster "I GUESS WE BEEN SO SECRETIVE ABOUT IT WAS THE REASON FOR THAT TRAGEDY..."
    show papyrusImg coolDude thinking
    papyrus "YOU KNEW ABOUT THE MONSTER BODIES MELTING WHEN THEY HAVE TOO MANY DETERMINATION?"
    show gaster trapped angry flip
    gaster "THE MONSTER SCIENTIFIC COMMUNITY KNEW THAT FOR CENTURIES"
    show gaster trapped dissapointed flip
    gaster "BUT WE NEVER WROTE IT DOWN, AS WAS CONSIDERED TABOO, AND WAS REDISCOVERED AGAIN AND AGAIN"
    show gaster trapped dissapointed
    gaster "I WROTE IT DOWN, ACTUALLY..."
    gaster "..."
    show gaster trapped neutral flip
    gaster "THANKS TO HIM WE WERE ABLE TO DISCOVER THAT, WITH ENOUGH DETERMINATION, WE COULD REMEMBER WHAT WE WERE DOING"
    gaster "EVENTUALLY I WANTED TO MAKE A BREAK THROUGH"
    show gaster trapped explain flip
    gaster "TO FIGURE OUT WHICH WAS BEYOND THE PORTAL WE CREATED"
    gaster "MY ASSISTANTS WERE INJECTED WITH ENOUGH DETERMINATION TO REMEMBER ME, BUT NOT MELT"
    gaster "AND THEN I JUMPED INTO THE PORTAL"
    show papyrusImg coolDude scared
    papyrus "WHAT HAPPENED?"
    papyrus "WHAT HAPPENED!?"
    show gaster trapped sorry flip
    gaster "I BECAME ONE WITH EVERYTHING"
    show papyrusImg coolDude thinking
    papyrus "WHAT?"
    show gaster trapped descisive flip
    gaster "I BECAME ONE WITH THE COMPLETE REALITY, WHICH HAS IT'S OWN BATTLE TO KEEP EXISTING"
    show gaster trapped explain flip
    gaster "BUT"
    gaster "SOMEHOW I WAS ABLE TO SEE ONE SINGLE SPACE OF TIME, TRHU THE EYES OF A SINGLE LIVING BEING"
    gaster "A FALLEN HUMAN"
    show papyrusImg coolDude realizing
    papyrus "FRISK?"
    papyrus "YOU MEAN FRISK?!"
    show gaster trapped dissapointed flip
    gaster "THAT WAS THEIR NAME?"
    gaster "HOW ODD"
    gaster "IT REMIND ME A BIT OF THE FALLEN PRINCE"
    show gaster trapped explain flip
    gaster "IN ANY CASE"
    show gaster trapped neutral flip
    gaster "I WAS NOT ABLE TO SPEAK TO THEM, OR UNDERSTAND THEM, BUT TO SHOW THEM SIMPLIFIED WAYS TO INTERACT AND UNDERSTAND HOW WE AS MONSTERS WORK"
    gaster "AFTER THAT, I TRIED MY BEST"
    gaster "NOT ALWAYS WORKED"
    show papyrusImg coolDude explaining
    papyrus "WHAT ARE YOU SAYING?"
    papyrus "THEY SAVED US!"
    show papyrusImg coolDude delight
    papyrus "AND YOU HELPED!"
    show gaster trapped angry flip
    gaster "I DIDN'T"
    show papyrusImg coolDude realizing
    gaster "SINCE I CAN'T WATCH OUTSIDE THAT SPACE OF TIME"
    gaster "I HAVE SEEN THE SAME STORY REPEATED GAIN AND AGAIN"
    gaster "SOMETIMES THEY DIE EVEN BEFORE GETTING OUT OF THE RUINS"
    show gaster trapped sorry flip
    gaster "OTHER..."
    gaster "I HAVE SEEN FRIENDS BEEN KILLED FOR STAND WITH THEIR IDEALS"  
    show papyrusImg coolDude explaining
    papyrus "DON'T BE SILLY!"
    show papyrusImg coolDude delight
    papyrus "FRISK IS MY BEST FRIEND"
    papyrus "THEY WILL NEVER DO SOMETHING LIKE THAT"
    show gaster trapped sorry
    gaster "..."
    show gaster trapped sorry flip
    gaster "I UNDERSTAND"
    gaster "SORRY FOR SUGGEST OTHERWISE"
    show papyrusImg coolDude thinking
    papyrus "WELL... THEN WHY ARE YOU HERE?"
    papyrus "YOU SAID YOU CANNOT SEE BEYOND THAT TIME SPACE, AND NOT AWAY FROM FRISK'S PERSPECTIVE"
    show papyrusImg coolDude explaining
    papyrus "THEN WHY WE CAN TALK?"
    show gaster trapped explain
    gaster "THIS MACHINE, IS THE PROBLEM"
    show papyrusImg coolDude thinking
    papyrus "THOSE ARE..."
    papyrus "A COMPUTER.."
    papyrus "WITH TANKS"
    gaster "THE CREATURES WHICH DEVELOPED THIS HORRIFING CREATURE DECIDED THEY JUST NEEDED TO COLLECT ENOUGH DETERMINATION TO INJECT IN THEIR LEADER"
    show gaster trapped dissapointed flip
    gaster "A POWERFUL BEING THEY CALLED ELWEKUFE"
    show gaster trapped explain
    gaster "SADLY FOR THEM, THEIR FIRST TEST RUNS FAILED MISERABLY, AND NOW THEY HAVE DISCOVERED THAT THE OWNERS OF THIS LAND, OUR KINGDOM, ARE IN THEIR TOES"
    gaster "SO, THEY HAVE ABANDONED THIS PLACE AND WILL TRY TO START SOMEWHERE ELSE ANEW"
    show gaster trapped proud
    gaster "BUT THEIR EXPERIMENT ALSO HAD AN INTERESTING SIDE EFFECT"
    show gaster trapped explain flip
    gaster "SO MANY DETERMINATION STORED IN JUST ONE PLACE WILL OBVIOUSLY AFFECT THE FABRIC OF REALITY"
    gaster "BUT, LUCKY FOR US, ONLY AFFECTED ONE THING OF IT"
    show papyrusImg coolDude realizing
    papyrus "YOU"
    papyrus "YOU WANT HELP TO ESCAPE THE FABRIC OF REALITY"
    show gaster trapped proud flip
    gaster "AS PERSPECTIVE AS USUAL"
    show papyrusImg coolDude thinking
    papyrus "THEN, WHY DID YOU CALLED ME?"
    show papyrusImg coolDude explaining
    papyrus "WOULDN'T DR. ALPHYS OR EVEN SANS BEEN MORE QUALIFIED THAN ME TO HELP YOU?"
    show gaster trapped descisive flip
    gaster "BUT"
    gaster "PAPYRUS, MY DEAR..."
    show gaster trapped descisive
    gaster "..."
    show gaster trapped descisive flip
    gaster "I SEE"
    gaster "YOU FORGOT ABOUT ME"
    show gaster trapped dissapointed flip
    gaster "AND SINCE I TAUGHT YOU EVERYTHING YOU KNEW ABOUT MONSTER SCIENCE, YOU HAVE FORGOT ABOUT THAT AS WELL"
    show papyrusImg coolDude thinking
    papyrus "I KNEW ABOUT SCIENCE?"
    show gaster trapped angry flip
    gaster "MY DEAR..."
    gaster "OF COURSE YOU KNEW!"
    gaster "IT WASN'T FOR YOU WE HAD NEVER FIGURE OUT HOW TO REMEMBER ANYTHING A..."
    show gaster trapped angry
    gaster "..."
    show gaster trapped explain flip
    gaster "IT DOESN'T MATTER"
    show gaster trapped neutral flip
    gaster "IN ANY CASE YOU WERE THE ONLY ONE WHO HEARD THE PLEA I JUST SENT TO EVERYBODY"
    show gaster trapped angry flip
    gaster "MEANING THAT EVEN IF YOU DON'T FEEL QUALIFIED ENOUGH"
    show papyrusImg coolDude careful
    papyrus "PLEASE DON'T SAY IT"
    show gaster trapped explain flip
    gaster "YOU ARE THE ONLY ONE WHO CAN HELP ME"
    papyrus "OH NO..."
    show gaster trapped neutral flip
    gaster "SO, PAPYRUS..."
    gaster "WILL YOU HELP ME ESCAPE THE FABRIC OF REALITY?"
    papyrus "..."
    
    menu:
        "Of Course!":
            jump cont1

label cont1:
    show papyrusImg coolDude delight
    papyrus "OF COURSE I WILL HELP YOU!"
    show gaster trapped angry flip
    gaster "WHY IT HAS 1 OPTION?"
    show papyrusImg coolDude thinking
    papyrus "???"
    gaster "YOU SHOULD... NO... MUST HAVE THE OPTION TO SAY NO"
    show gaster trapped descisive flip
    gaster "AGAIN!"
    gaster "TWO OPTIONS!"
    menu:
        "Of Course!":
            jump cont2
        "Of Course!":
            jump cont2
label cont2:
    show gaster trapped angry flip
    gaster "WHY THE TWO OPTIONS ARE THE SAME???!!!"
    show papyrusImg coolDude explaining
    papyrus "WHY WILL I NOT HELP YOU?"
    papyrus "EVERYTHING YOU SAID IS SUSPICIOUS, BUT NOBODY DESERVE TO LIVE LIKE THAT FOR THIS LONG"
    show papyrusImg coolDude delight
    papyrus "AND IF YOU TURN OUT TO BE A BAD GUY, WE WILL STOP YOU"
    show papyrusImg coolDude neutral
    papyrus "IT'S NOT MY FIRST RODEO ON SOMETHING LIKE THIS"
    show gaster trapped neutral
    gaster "OF COURSE, I FORGOT ABOUT THE YOUNG PRINCE"
    show papyrusImg coolDude thinking
    papyrus "!???"
    show gaster trapped neutral flip
    gaster "VERY WELL..."
    gaster "THERE IN THE COMPUTER ARE LEFT BLUPRINTS AND READINGS"
    $ pen = True
    gaster "I PUT THEM IN A PENDRIVE, RIGHT HERE"
    show papyrusImg coolDude neutral
    gaster "SINCE I TOUCHED IT, IT SHOULD SURVIVE TIME AND SPACE"
    gaster "WITH THIS INFORMATION, YOU SHOULD BE ABLE TO FORMULATE SOMETHING TO HELP ME"
    papyrus "I'M GOING TO EXPLAIN THIS TO EVERYBODY"
    show papyrusImg coolDude delight
    papyrus "I HAVE LITTLE PROOF, BUT THE BLUPRINT MUST BE ENOUGH FOR THEM TO BELIEVE ME!"
    show gaster trapped dissapointed flip
    gaster "MY DEAR PAPYRUS..."
    gaster "IT'S THERE SOMETHING ELSE I MUST TELL YOU"
    show gaster trapped dissapointed
    show papyrusImg coolDude scared
    gaster "THE COMPUTER IS GOING TO SELF DESTRUCT TODAY"
    gaster "AND THAT MEANS YOU WOULDN'T BE ABLE TO HELP ME WITHOUT ALL THIS DETERMINATION"
    show papyrusImg coolDude realizing
    papyrus "HAVE YOU"
    show gaster trapped explain flip
    gaster "OF COURSE"
    gaster "I WOULDN'T CALLED YOU BEFORE EVEN TRYING"
    papyrus "THEN..."
    papyrus "WHAT DO YOU SUGGEST"
    show gaster trapped descisive flip
    gaster "RESET"
    show papyrusImg coolDude scared
    papyrus "??!!!"
    show gaster trapped dissapointed
    gaster "I'M SORRY PAPYRUS"
    scene black with dissolve
    pause(2)
    jump day1
return

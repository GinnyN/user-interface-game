label day3:
    call freeMorning

label forest:
    scene skelebroHouse outside with dissolve
    show papyrusImg neutral zorder 0 at fade:
        xpos 0
    papyrus "EVERYTHING HAS BEEN ACCOUNTED FOR"
    show papyrusImg serious
    papyrus "AND NOW, DIRECTLY TO THE CASTLE!"
    hide papyrusImg
    papyrus "THE KING AND UNDYNE ARE WAITING FOR ME"
    papyrus "TODAY IS THE DAY WE TRAP THOSE AWFUL PEOPLE!"
    if resets < 1:
        pause (0.5)
        "???" "{font=fonts/NewAster.ttf} ... {/font}"
        "???" "{font=fonts/NewAster.ttf} DE... {/font}"
        "???" "{font=fonts/NewAster.ttf} PA... {/font}"
        "???" "{font=fonts/NewAster.ttf} US... {/font}"
        "???" "{font=fonts/NewAster.ttf} ... {/font}"

# label newHome:
    scene day3 intro background with dissolve:
        ypos 0.0
        linear 10 ypos -1.0
    show day3F intro foreground at fade:
        ypos 0.0
        linear 7 ypos -1.1
    play music "music/33 Quiet Water.mp3" fadein 1 fadeout 1 
    pause (1.0)
    asgore "Remember that we need to just trap them"
    asgore "We don't need them neither maimed or dead"
    undyne "But also we need to remember to be as scary as we can"
    undyne "If those humans suddenly discover they can produce more determination than us"
    papyrus "WE'RE DOOMED!"
    undyne "Exactly"
    asgore "I don't think you will have that problem"
    asgore "You are plenty scary yourself"
    show undyneImg armor cocky zorder 1 at fade:
        xpos -0.1
        ypos 0.1
    undyne "Pfff"
    undyne "Yeah, says the guy with the horns and the trident!"
    show undyneImg armor smile
    asgore "Maybe you have a point there"
    show papyrusImg angry  zorder 0 at fade:
        xpos 0.5
    papyrus "WE'RE READY!"
    papyrus "LET'S DO THIS!!!"
    hide papyrusImg
    play sound "music/fx/steps.wav"
    asgore "Between you and me"
    asgore "I think he's the scariest"
    undyne "MMmmm"

#Outside Forest
    papyrus "I'M PRETTY SURE MY DOG LIKE NOSE CAN GUIDE US LIKE THE LAST TIME"
    papyrus "BUT THEY DECIDED TO SEPARATE TO COVER MORE AREA"
    papyrus "WELL, THEY WILL BE SURPRISED WHEN I FIND THE PLACE WHERE THE REST OF THOSE EVIL BEINGS ARE FIRST!"
    papyrus "*SNIFF SNIFF*"
    papyrus "WHAT?!"
    "Monster 1" "* Did you said the place of those humans was around here"
    "Monster 2" "* Yes! After what happened two days ago the..."
    papyrus "HEY!"
    "Monster 1" "* Ohh... Hey!"
    papyrus "I DIDN'T KNEW THE KING AND UNDYNE RECLUTED MORE MONSTERS TO HELP OUT!"
    "Monster 1" "* Uhhh..."
    "Monster 2" "* Yes... we..."
    "Monster 2" "* are helping out"
    papyrus "GREAT!"
    papyrus "I ALREADY CHECKED OUT THAT AREA AND I'M GOING TO CHECK OUT THERE"
    papyrus "YOU CAN GO THAT WAY AND CHECK THERE"
    papyrus "I'LL GIVE YOU A HEAD START!"
    "Monster 1" "* Yes.. yes..."
    "Monster 2" "* We're going to check out there"
    "Monster 1" "* Thanks..."
    "Papyrus leaves"
    "Monster 1" "* He's talking about the king of all monsters?"
    "Monster 2" "* He likes humans" 
    "Monster 2" "* He basically adopted one too!"
    "Monster 1" "* We need to move quickly, before he realize anything"
    menu:
        "Help them out":
            jump helpthemout
        "Let's them go alone":
            jump leaveThemAlone

label leaveThemAlone:
    $ whoRescueMauricio = True
    "Monster 1" "* Let´s move"
    papyrus "HOPEFULLY THOSE TWO ARE GOING TO BE OK"
    papyrus "SNIFF, SNIFF.."
    papyrus "LET'S FOLLOW THE SCENT"
    "Papyrus follow the scent until he found an abandoned castle"
    papyrus "ANOTHER OF THIS HUMAN BUILDINGS"
    papyrus "I'D BETTER TELL UNDYNE AND THE KING"
    asgore "This must be one of the buildings of the monster during the war"
    asgore "The humans must have found it and restore it"
    papyrus "WOWIE"
    papyrus "A PIECE OF MONSTERS' HISTORY!"
    undyne "Let's better check inside before any human appears"
    undyne "For their own sake"
    papyrus "HEEEEYYYY!!!! KIDNAPPEEEEERRRRRRSSSSSS!!!"
    undyne "Stop doing that Papyrus!"
    papyrus "I'M SORRY"
    asgore "Calm down everyone"
    asgore "Let's keep moving"
    papyrus "UH?"
    papyrus "WHAT'S THAT?"
    papyrus "HEY! YOU!"
    "Human Kid" "* AAAHHGGG"
    "Human Kid" "* A MONSTER!"
    papyrus "YES, A MONSTER!"
    papyrus "WHO CAME TO SAVE YOU FROM THE EVIL..."
    "Human Kid" "* Monsters?"
    papyrus "COME AGAIN?"
    "Human Kid" "* A black one, kind of furry with horns"
    papyrus "..."
    papyrus "COME ON HUMAN, I'LL TAKE YOU OUT OF HERE"
    "Human Kid" "* But... my brother..."
    papyrus "IS HE HERE?"
    "Human Kid" "* I don't know"
    papyrus "I'LL LEAVE YOU WITH A GOOD FRIEND OF MINE"
    papyrus "SHE LOVES KIDS"
    papyrus "I'LL SEARCH FOR YOUR BROTHER AFTER THAT"
    
    alphys "Toriel is not here! She's with Sans at the humans'"
    papyrus "YOU RIGHT!"
    papyrus "THEN WE'LL HAVE TO TAKE CARE OF THE HUMAN"
    metatton "Sorry I'm asking, but did you tell Undyne and the King about this?"
    papyrus "OOOPPPSSS"
    papyrus "I'D BETTER BE GOING!"
    frisk "Don't worry, you'll be fine"
    frisk "They are my friends"
    
    papyrus "UNDYNE!"
    papyrus "YOUR MAJESTY!"
    papyrus "WHERE'S EVERYBODY?"
    "Monster 1" "ARGH!"
    "Monster 2" "The Skeleton!"
    papyrus "HEY YOU!"
    
    $ time = resets + papyrusTraining
    $ timer_range = resets + papyrusTraining
    $ timer_jump = 'papyrusAttackAsgore'

    if time > 1:
        show screen countdown

        menu:
            "Try to convince them peacefully":
                hide screen countdown
                jump convincePeacefully

    else:
        jump areYouKidnappingHumanKids

label areYouKidnappingHumanKids:
    papyrus "ARE YOU KIDNAPPING HUMAN KIDS????"
    "Monster 1" "..."
    "Monster 2" "run"
    papyrus "HEY YOU! WAIT!"
    "Papyrus run to the ceiling following one of the monsters"
    papyrus "EXPLAIN TO ME WHAT ARE YOU DOING?!"
    papyrus "THERE WAS A HUMAN CHILD HERE AND THEY WASN'T HAPPY"
    "Monster 1" "NO, YOU ARE THE ONE WHO DON'T GET IT!"
    "Monster 1" "HUMANS ARE EVIL!"
    papyrus "SO YOU ARE COOPERATING WITH EVIL HUMANS FOR WHAT?"
    papyrus "NOT ALL HUMANS ARE EVIL, LIKE MONSTERS"
    papyrus "BUT ALL HUMANS ARE REDEEMABLE, LIKE MONSTERS TOO"
    "Monster 1" "You don't get it"
    papyrus "WHAT I HAVE TO GET I'M SO TIRED OF THAT"
    "Monster 1 jumps from the ceiling to the floor"
    papyrus "WAIT, WHAT RE YOU DOING?!"
    asgore "That's also my question"
    papyrus "!?"
    jump backNewerHome

label helpthemout:
    $ whoRescueMauricio = False
    papyrus "NOW I THINK ABOUT IT"
    "Monster 1 and 2" "* AAAHHHH!!!"
    papyrus "I'LL BETTER GO WITH YOU GUYS'"
    papyrus "NOBODY KNOWS WHAT COULD HAPPEN IF I LEAVE YOU ALONE IN A PLACE THIS DANGEROUS!"
    "Monster 1" "* (We need to get rid of him)"
    "Monster 2" "* (Yes, but how?)"
    "* Papyrus ends alone hanging from his pants from a tree in a cliff"
    papyrus "HOW I LET THIS HAPPENING?"
    papyrus "WELL, AT LEAST THEY PROMISE ME THEY WILL FIND SOME HELP"
    papyrus "BUT IT'S GETTING LATE ALREADY"
    papyrus "MMM..."
    "* Papyrus calls a bone and throw it to the cliff, letting a big giantic bone grow from there. He grabs it when it's growing and eventually reach the top of the cliff safe"
    papyrus "THE GREAT PAPYRUS HAS DONE IT AGAIN!"
    papyrus "NOW I NEED TO FIND THOSE MONSTERS"
    papyrus "THEY MUST BE WORRIED SICK I FELL INTO THIS PLACE"
    "* Papyrus decides to go and check for the monsters he found. He search a lot everywhere and doesn't find them still"
    papyrus "HELLOOOOO???"
    papyrus "WHERE ARE YOU GUYS???"
    papyrus "MMM...."
    papyrus "HOPEFULLY THEY ARE ALRIGHT"
    "* The two monsters pass near Papyrus running and one of them is holding a human child"
    papyrus "A HUMAN?!"
    papyrus "ARE THEY KIDNAPPING A HUMAN CHILD!?"
    papyrus "NOT ON THE WITNESS OF THE GREAT PAPYRUS!"
    "Papyrus kicks the floor and make a bone appear in front of the monster not carrying the child, letting the other escape"
    papyrus "WRONG MONSTER!"
    papyrus "BUT I CAN STILL FIX THIS!"
    "Papyrus tries again, but it's interrupted by one of Undyne's Spears"
    papyrus "UNDYNE?!"
    papyrus "WHAT ARE YOU DOING?!"
    papyrus "THEY ARE ESCAPING!!!"
    undyne "WHAT ARE YOU DOING YOU IDIOT?!"
    undyne "These monsters has nothing to do with anything!!!!"
    papyrus "UNDYNE PLEASE!"
    papyrus "THEY ARE CARRYING A SCARED HUMAN CHILD"
    papyrus "AND THEY ARE RUNNING AWAY FROM US"
    undyne "Because they are smart and trying to get away from the evil humans!"
    papyrus "BUT UNDYNE!"
    papyrus "I'M SURE THE CHILD IS NOT AGREEING WITH THIS!"
    papyrus "OH GOD!"
    papyrus "THE CHILD!"
    undyne "Papyrus wait!"
    "Papyrus run thru the forest while Undyne is trying to catch up with her armor not cooperating"
    undyne "This stupid bonehead is getting away somehow!"
    asgore "Leave this to me"
    undyne "But..."
    "Asgore shoots one of his tridents and traps Papyrus inside them, unable to move"
    papyrus "YOUR MAJESTY! PLEASE!"
    papyrus "I NEED TO SAVE THAT CHILD!!"
    asgore "And you need to calm down Papyrus"
    asgore "False accusations go nowhere here"
    papyrus "THOSE AREN'T FALSE"

    $ time = resets + papyrusTraining
    $ timer_range = resets + papyrusTraining
    $ timer_jump = 'papyrusAttackAsgore'

    if time > 1:
        show screen countdown

        menu:
            "Sucker Punch":
                hide screen countdown
                jump papyrusSuckerPunch

    else:
        jump papyrusAttackAsgore

label papyrusAttackAsgore:
    papyrus "I CHALLENGE YOU TO A DUEL!"
    papyrus "IF I WIN YOU HAVE TO BELIEVE ME!"
    asgore "That's not how trust works Papyrus"
    asgore "But if it's the only way I can bring you back to Newer Home"
    papyrus "WHAT ARE YOU..."
    jump backNewerHome

label backNewerHome:
    "Back to Newer Home, Sans and Toriel are formally dressed just back from the meeting with the human autorities"
    sans "what just happened?"
    sans "we were at the middle of an meeting"
    toriel "Hopefully they are already captured the humans"
    undyne "Not really"
    "Asgore is carrying Papyrus upside down"
    papyrus "..."
    "Pfff!"
    sans "papyrus?"
    sans "What just happened?"
    undyne "We found by cheer luck some monsters in the forest"
    undyne "And Papyrus started to attack them with no reason at all"
    papyrus "UNDYNE!"
    papyrus "I TOLD YOU THE REASON!"
    undyne "PAPYRUS SHUT UP"
    undyne "THIS IS GETTING WAY OUT OF HAND"
    toriel "UNDYNE"
    toriel "What do you think you are doing?"
    undyne "It's just..."
    undyne "grrrr...."
    undyne "argh"
    sans "What the matter, uh?"
    undyne "Those monsters did nothing"
    asgore "..."
    undyne "And he is attacking them"
    undyne "This is exactly what I..."
    undyne "grrr...."
    sans "exactly you what?"
    sans "come on, say it!"
    undyne "You don't get it"
    sans "i'll tell you what i`m getting then"
    sans "so maybe you"
    papyrus "EVERYBODY JUST STOP!"
    papyrus "I CAN`T TAKE THIS ANYMORE!"
    "Papyrus ran away"
    asgore "Oh no"
    sans "bro..."
    toriel "Now you did it"
    asgore "I'm scared about the same thing, though"
    sans "what?"
    asgore "Not in the way of he will go out of control again"
    asgore "But in a way he will start to look too hard trying to fix that mistake"
    undyne "He always tries too hard..."
    undyne "..."
    undyne "And I always thought he will die at the hands to a powerful enemy if I teach him to fight"
    sans "..."
    toriel "Everybody is stressed out, specially him"
    toriel "I think the best we can do is just rest and tomorrow study his accusations"
    toriel "Let`s give him the benefit of the doubt this time"

    "Papyrus is under a tree near to his house."

    papyrus "BEEN GREAT IS GETTING MORE DIFFICULT AT THE TIME GOES ON"
    papyrus "I HAVE TO STILL WORK ON IT"
    papyrus "but..."
    papyrus "..."
    papyrus "NO BUTS PAPYRUS, NOT THIS TIME"
    papyrus "THE GREAT PAPYRUS HAS..."
    papyrus "NO."
    papyrus "WILL SOLVE THIS MESS SOMEHOW"
    papyrus "BUT NOW I HAVE TO WORK IN THE HOW"
    papyrus "HOW?"
    papyrus "MMMMMMMMMMMM"
    papyrus "UH? FRISK?"
    frisk "Hi"
    papyrus "WHAT'S THE MATTER?"
    if whoRescueMauricio:
        frisk "Do you remember the kid you saved?"
        papyrus "OH RIGHT"
        frisk "They`re name is Mauricio"
        frisk "They told me they remembered where their sibling is hidden"  
    else:
        frisk "Did you know Dogamy and Dogaressa found a kid in the woods?"
        papyrus "MAYBE IS..."
        papyrus "OK, GO ON"
        frisk "They said they were kidnapped by some humans and then given to some..."
        papyrus "MONSTERS??"
        frisk "Yes, how to..."
        papyrus "I FOUND THEM IN THE WOODS"
        frisk "Well, they said their sibling were also kidnapped"
        frisk "And that maybe they remember where their sibling is"
    papyrus "REALLY??"
    papyrus "WOWIE!"
    papyrus "WE SHOULD GO AT ONCE!"
    frisk "Are you sure?"
    papyrus "YES!"
    frisk "Let's me send a text to my mom first"
    papyrus "YES YES, YOU SHOULD TELL TORIEL"
    papyrus "DONE?"
    frisk "Done"
    papyrus "OK!"
    papyrus "TO"
    papyrus "..."
    papyrus "TO WHERE?"
    frisk "To"

    " Cuts to Toriel telling Sans and Asgore what`s just happened "

    sans "mount anemi"
    sans "that name is kind of weird"
    asgore "It's near from here"
    asgore "I`ll call U..."
    asgore "I`ll go myself to see what`s going on"
    sans "what are you implying?"
    asgore "Just that I don`t want for them to get any trouble"
    toriel "That mount is barely on the humans` maps"
    toriel "I texted Alphys about it"
    sans "then is a perfect place for humans doing illegal things"
    sans "ok, let`s go..."
    sans "wait did you texted alphys?"
    toriel "Yes, I just..."
    toriel "Oh uh"

    " You can hear Undyne screaming out of screen "

    undyne "AAAAHHHHHHHHHRRRRGGGGGGGGGGG!!!!!"
    undyne "PAPYRUS!!"
    undyne "AT LEAST WAIT UNTIL TOMORROW DAMMIT!!!!"
    asgore "We should go at once"
    sans "Yes, yes"

    "After a moment in Mount Anemi"

    papyrus "WHERE DID THEY SAID THEIR SIBLING WERE?"
    frisk "In a cave near to where the snow started"
    papyrus "THIS IS CHILLIER THAN HIGH SNOWDIN"
    papyrus "ARE YOU OK FRISK?"
    frisk "..."
    papyrus "HA! I KNEW IT!"
    papyrus "COME ON FRISK, I DON'T HAVE SKIN, I'LL BE OK!"
    papyrus "TAKE MY SCARF"
    frisk "But"
    frisk "But it's part of your battle body..."
    papyrus "WHAT`S A BATTLE BODY GOOD FOR IF IT CAN`T HELP MY FRIENDS?"
    papyrus "WHAT?"
    frisk "Nothing, let`s keep moving"
    papyrus "YES!"

    "Papyrus and Frisk move into the mountain, while Sans appears just behind them"

    sans "they seem to be fine"
    sans "mmmm"
    sans "i think we`ll be better to follow them and see where this goes"
    sans "but this just leave me with"
    sans "mmm"

    "Sans moves 3 steps to the left and them points to the ground"

    sans "done"

    "Sans hides. Undyne appears "

    undyne "ARGH!"
    undyne "Not Frisk too!!!"
    undyne "PA..."
    undyne "!?"

    "Undyne end ups trapped in a booby trap on the floor"

    undyne "SANS!"
    undyne "I KNOW THIS IS YOU!"
    sans "i totally forgot about practical jokes"
    sans "i should do this more often"
    sans "ppfff"
    undyne "You..."
    asgore "What`s going..."
    asgore "ppfff"
    undyne "Asgore..."
    undyne "Not you too.."
    asgore "I`m sorry Undyne..."
    asgore "It`s just..."
    asgore "Pffff"
    undyne "GET ME OUT GET ME OUT GET ME OUT!"

    "Meanwhile, Papyrus and Frisk are still searching"

    papyrus "OH LOOK FRISK!"
    frisk "A giant hole on the floor!"
    papyrus "LET`S SEE THERE"
    papyrus "HEEEYYYY!!!"
    "Kid 1" "It`s another monster!"
    "Kid 2" "Hide! Hide!"
    frisk "It`s ok! Papyrus is my friend!"
    "Kid 3" "A human?"
    "Kid 1" "It`s a kid like us!"
    "Kid 2" "They came to rescue us?"
    papyrus "YES"
    frisk "We came in the name of Mauricio!"
    "Kid 3" "That`s my brother"
    "Kid 3" "Is he alright?"
    papyrus "HE`S FINE!"
    papyrus "NOW WE NEED TO GET YOU GUYS OUT OF THERE!"

    "Back with Undyne, Sans and Asgore"

    asgore "This is a very good trap Sans"
    sans "i actually surprised myself"
    undyne "ARGH! I got out!"
    undyne "I`ll talk with you later punk!"
    sans "look at me i`m so scared"
    undyne "Now I will"

    "Papyrus appears, dressed only with his pants"

    papyrus "WHAT ARE YOU DOING HERE PLAYING IN THE DIRT?"
    undyne "ARGH! PAPYRUS!"
    undyne "How you..."
    papyrus "CAN WE LEAVE THIS FOR LATER?"
    papyrus "FRISK AND I FOUND 5 KIDNAPPED KIDS IN A CAVE"
    papyrus "THEY ARE FREEZING AND I`M RUNNING OUT OF CLOTHES"
    asgore "Five?!"
    "Asgore goes out"
    sans "well, i got my jacket"
    "Sans goes out"
    undyne "Papyrus... I..."
    papyrus "I TOLD YOU, WE BETTER LEAVE THIS FOR LATER"
    papyrus "I`M FINE"
    papyrus "THOSE KIDS ARE MORE IMPORTANT"
    undyne "Heh..."
    undyne "You right..."
    
    label endOfDay3:
        if resets > 1:
            call questionsEnd
        jump day4
return



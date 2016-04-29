label day3:
    $ fromDay = 3
    jump freeMorning

label forest:
    scene skelebroHouse outside with dissolve
    papyrus "WELL, THAT WAS FUN"
    papyrus "AND NOW, DIRECTLY TO THE CASTLE!"
    "WHOOOSHH"
    papyrus "THE KING AND UNDYNE ARE WAITING FOR ME"
    papyrus "TODAY IS THE DAY WE TRAP THOSE AWFUL PEOPLE!"

# label newHome:
    asgore "Remember that we need to just trap them"
    asgore "We don't need them neither maimed or dead"
    undyne "But also we need to remember to be as scary as we can"
    undyne "If those humans suddenly discover they can produce more determination than us"
    papyrus "WE'RE DOOMED!"
    undyne "Exactly"
    asgore "I don't think you will have that problem"
    asgore "You are plenty scary yourself"
    undyne "Pfff"
    undyne "Yeah, says the guy with the horns and the trident!"
    asgore "Maybe you have a point there"
    papyrus "WE'RE READY!"
    papyrus "LET'S DO THIS!!!"
    "Papyrus leaves"
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
                jump papyrusSuckerPunch

    else:
        jump papyrusAttackAsgore

label helpthemout:
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
    "Asgore is carrying Papyrus upside down "

return



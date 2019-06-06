label pendriveBrainStorm:
    papyrus "WHAT DO I DO WITH THIS THING?"
    gaster "WELL, THAT'S A FLASH STORAGE UNIT, PEOPLE CALL IT PENDRIVE MOSTLY FOR ITS FORM"
    gaster "I THINK IS SOMEWHAT OLD, SO IT CAN HOLD AROUND 1GB, MAYBE A BIT MORE"
    gaster "YOU CAN USE IT TO SAVE DIFFERENT KIND OF COMPUTER FILES, LIKE EXECUTABLES, TEXT FILES, IMAGE FI.."
    papyrus "NO"
    extend ", NO "
    extend ", NO NO NO NO NO "
    extend ", NOOOOOOO... "
    papyrus "WHAT I AM ASKING IS WHAT DO I DO WITH THE FILES YOU PUT ALREADY HERE.."
    gaster "OH "
    extend "I UNDERSTAND"
    gaster "WHAT I DID PUT ON THAT PENDRIVE WERE THE SOFTWARE THEY USED FOR THE DETERMINATION TANKS"
    gaster "THE BLUEPRINTS OF THE TANKS, THE SOURCE CODE OF THE SOFTWARE"
    gaster "AND THE SERVER IN WHICH THAT SOFTWARE RUNS"
    gaster "IT ALSO HAD SOME DOCUMENTATION BUT I DON'T KNOW IF ITS RELIABLE ENOUGH"
    gaster "I DISCOVERED THAT THE SOFTWARE THEY USE TO CONTROL THE TANKS HAS AN API, SO IT SHOULD BE SOMEWHAT PAINLESS TO USE WITHOUT DESTROYING EVERYTHING"
    gaster "SO, WE JUST NEED SOMEONE WHO KNOWS A LOT ABOUT MONSTERS SCIENCE, DETERMINATION AND PROGRAMMING"
    papyrus "I HAVE 2 ANSWERS FOR THAT QUESTION AND I DON'T LIKE EITHER OF THOSE TWO"
    gaster "YOU HAVE 2 ANSWERS?"
    if pendriveTree < 1:
        $ pendriveTree += 1
    return

label pendriveSans:
    gaster "HAVE YOU THOUGHT ABOUT ASKING YOUR BROTHER?"
    papyrus "DOES HE REMEMBER YOU?"
    gaster "WHAT THAT HAS TO DO WITH THIS?"
    gaster "DIDN'T YOU SAID SEVERAL TIMES THAT HE LIKES SCIENCE, ESPECIALLY WHEN IS REAL?"
    gaster "HE MIGHT BE INTERESTED IF YOU ASK HIM"
    gaster "THIS IS, IN FACT, REAL SCIENCE"
    pause(1.0)
    gaster "PAPYRUS?"
    gaster "IT'S THERE SOMETHING WRONG?"
    papyrus "..."
    if pendriveTreeSans < 1:
        $ pendriveTreeSans += 1
    return

label pendriveSansTwo:
    gaster "PAPYRUS?"
    gaster "PLEASE CAN YOU TELL ME WHAT THE PROBLEM WITH YOUR BROTHER?"
    papyrus "I DON'T W{cps=*0.2}AAAAAAA{/cps}NNN{cps=*0.2}AAAAAAAAA{/cps}"
    gaster "WHY?"
    gaster "HE'S YOUR BROTHER"
    gaster "HE LOVES YOU"
    papyrus "I KN{cps=*0.2}OOOWWW...{cps=*0.2}"
    papyrus "IT'S JUST"
    papyrus "IF HE DOES REMEMBER YOU, HE WILL BE TOO SUSPICIOUS TO BE OF ANY HELP"
    papyrus "IF HE DOES NOT REMEMBER YOU, HE WILL NOT BELIEVE ME NO MATTER WHICH PROOF I HAVE AND WILL TRY TO CONVINCE ME YOU ARE A SOME SORT OF IMAGINARY FRIEND"
    papyrus "IT'S NOT GOING TO BE THE FIRST TIME"
    gaster "I STILL DON'T SEE WHY YOU SHOULDN'T TRY"
    gaster "IF IT DOESN'T WORK WE CAN LOOP BACK AND IT WILL LIKE NEVER HAPPENED"
    papyrus "I DON'T LIKE THAT EITHER"
    gaster "..."
    gaster "PAPYRUS..."
    gaster "PLEASE..."
    papyrus "{cps=*1.5}OK FINE I'LL ASK HIM{/cps}"
    gaster "THANKS YOU"
    papyrus "IT'S NOT GOING TO WORK THOUGH"
    gaster "BUT WE'RE GOING TO TRY AND THAT'S IMPORTANT"
    papyrus "YEAH... YOU RIGHT..."
    if pendriveTreeSans < 2:
        $ tryWithSans = True
        $ pendriveTreeSans += 1
    return

label pendriveAlphys:
    gaster "WHAT'S ABOUT THE ROYAL SCIENTIST?"
    papyrus "WHO?"
    gaster "THE ROYAL SCIENTIST"
    gaster "YOUR FRIEND"
    gaster "THE SPOUSE OF YOUR OTHER FRIEND"
    gaster "THE FRIEND WHO SANS MET BEFORE YOU"
    papyrus "AH YOU MEANT DR ALPHYS!"
    papyrus "SHE'S NOT THE ROYAL SCIENTIST ANYMORE"
    gaster "WHAT? WHY?"
    gaster "THIS MAKES NO SENSE, EVERYBODY HAS AN ACCIDENT"
    gaster "YOU CANNOT GO AND DO SOMETHING LIKE THAT TO A PROMISING CAREER!"
    gaster "I'M GOING TO COMPLAIN TO THE KING ABOUT THIS! I..."
    gaster "I CANNOT GO AND COMPLAIN ABOUT THIS"
    papyrus "DO YOU NEED A MOMENT?"
    gaster "NO..."
    gaster "I..."
    gaster "I AM FINE"
    if pendriveTreeAlphys < 1:
        $ pendriveTreeAlphys += 1
    return

label pendriveAreYouOk:
    papyrus "ARE YOU SURE YOU ARE OK?"
    gaster "IT'S "
    extend "THAT "
    extend "FEELING"
    gaster "YOU KNOW THE ONE"
    gaster "THE ONE WHEN YOU REALIZE YOU WANT TO HELP SOMEONE BUT YOU ARE COMPLETELY USELESS TO DO IT"
    papyrus "DO YOU REALLY THINK DR ALPHYS IS GOOD AT SCIENCE?"
    gaster "YES"
    gaster "OF COURSE"
    gaster "VERY, VERY TALENTED INDEED"
    gaster "SHE BASICALLY REDISCOVERED GOOD CHUNK OF THE THEORY OF DETERMINATION AFTER I..."
    gaster "SCREW EVERYTHING UP"
    papyrus "WOWIE!"
    gaster "I MUST HAVE SOME SORT OF ADMIRATION FOR A WORK LIKE THAT, NO MATTER HOW ACTUALLY..."
    gaster "FINISHED"
    papyrus "I GUESS IT WOULD NOT BEEN THAT TERRIBLE IF SHE HAD INFORMED WHAT HAPPENED WHEN ACTUALLY HAPPENED"
    gaster "THAT'S WHAT I'M SAYING"
    gaster "PLUS, SHE WAS EXPERIMENTING WITH DYING MONSTERS"
    gaster "WHAT THEY WERE EVEN EXPECTING TO HAPPEN?"
    papyrus "NOW YOU ARE SAYING THAT I KINDA SEE TORIEL'S POINT"
    gaster "IT WAS HER?"
    gaster "..."
    gaster "OF COURSE IT WAS HER"
    if pendriveTreeAlphys < 2:
        $ pendriveTreeAlphys += 1
    return

label pendriveAlphysThree:
    gaster "IN WHAT THEY ARE WASTING HER TALENTS ANYWAY?"
    papyrus "WHO?"
    gaster "YOUR FRIEND"
    gaster "THE ONE WHO DID THE EXPERIMENTS"
    papyrus "DR ALPHYS?"
    papyrus "SHE'S WORKING AS AN ARCHIVIST UNDER TORIEL!"
    gaster "OF COURSE IT HAS TO BE THE QUEEN"
    papyrus "DR ALPHYS ALWAYS TELLS ME THAT IS DIFFICULT FOR HER TO LEARN THE NEW CRAFT, BUT TORIEL HAS TOLD ME SHE'S GREAT IT AND SHE'S DOING A GREAT JOB"
    gaster "OH"
    papyrus "DR ALPHYS IS SO GOOD AT GETTING INFORMATION THAT TORIEL IS ALWAYS ASKING HER ABOUT DIFFERENT STUFF, INCLUDING A LOT OF HUMANS RELATED THINGS"
    papyrus "APPARENTLY, THE IDEA IS, IF TORIEL IS UNAVAILABLE, DR ALPHYS CAN PERFECTLY REPLACE HER"
    papyrus "I THINK IT SUITS HER"
    gaster "LOOK AT THAT"
    gaster "SO, YOU THINK SHE CAN HELP US"
    papyrus "DO I THINK THAT?"
    papyrus "OF COURSE I THINK THAT!"
    papyrus "I HAVE NO WAY TO KNOW THIS BUT I'M SURE THIS GOING TO BE REALLY EASY FOR HER"
    papyrus "SHE'S THAT AWESOME"
    gaster "GO AHEAD MY DEAR PAPYRUS"
    if pendriveTreeAlphys < 3:
        $ pendriveTreeAlphys += 1
        $ tryWithAlphys = True
    return

label pendriveAlphysFailState:
    papyrus "DID SHE SAID SHE NEEDS MORE TIME?"
    gaster "WHAT I DID UNDERSTAND FROM WHAT SHE SAID"
    gaster "APPARENTLY THE DAY YOU GAVE HER THE FILES WAS NOT IDEAL TO WORK IN A PROGRAM TO ACCELERATE THIS PROCESS"
    papyrus "SO, THEN, WHAT WE GOING TO DO?"
    gaster "YOU HAVE TO FIND A MOMENT DURING DAY 2 OF THE LOOP TO GIVE THE FILES TO HER"
    papyrus "BUT..."
    papyrus "I'M ALWAYS SUPER DISTRACTED DURING THE 2ND DAY"
    papyrus "I EVEN GET KINDA DRUNK FOR A MOMENT AND THAT SO NOT ME"
    papyrus "IN WHICH MOMENT I CAN DO IT?"
    gaster "I'M NOT SURE ABOUT THAT PAPYRUS"
    gaster "I'M SURE MUST BE SIMPLE WAY TO SOLVE THIS PUZZLE, BUT IT'S MUST BE ON THE SECOND DAY"
    gaster "MONSTERS ARE A FICKLE BUNCH"
    gaster "EVEN IF YOU GIVE HER THIS DURING DAY 2, THERE'S NOT GUARANTEE IS GOING TO WORK"
    papyrus "WOWZIE"
    if day == 1:
        papyrus "WHAT ABOUT IF I GO NOW?"
        gaster "LET'S ME CHECK"
        pause(2.0)
        gaster "THEY ARE SLEEPING"
        papyrus "UNDYNE IS GOING TO SENT MY HEAD IN A BOX TO SANS IF I GO NOW"
        gaster "AFTER WHAT HAPPENED TODAY?"
        papyrus "YES!"
        gaster "IF YOU SAY SO"
    papyrus "..."
    papyrus "OK, BUT IF I FAIL DURING THE 2ND DAY?"
    papyrus "I WILL NEED TO LIVE THE NEXT 2 DAYS BEFORE TRYING AGAIN?"
    gaster "I CANNOT SENT YOU BACK TO ANY MOMENT EXCEPT WHEN YOU WERE ABOUT TO SAVE YOUR FRIEND, BUT"
    papyrus "BUT?"
    gaster "I CAN TRIGGER IT AT ANY MOMENT ACTUALLY..."
    papyrus "YOU COULD HAVE DONE THAT SINCE THE BEGINNING"
    gaster "OF COURSE..."
    papyrus "WELL, YES, THIS IS THE FIRST TIME WE HAVE A TIME CONSTRAIN TO THE PLAN..."
    papyrus "JUST PUT THEM ON THE OPTIONS"
    $ resetFromQuestionMenu = True
    gaster "DONE"
    papyrus "THANK YOU!"
    if pendriveTreeAlphys < 4:
        $ pendriveTreeAlphys += 1
    return
label pendriveBrainStorm:
    show papyrusImg uhh
    papyrus "WHAT DO I DO WITH THIS THING?"
    show gaster trapped explain flip
    gaster "WELL, THAT'S A FLASH STORAGE UNIT, PEOPLE CALL IT PENDRIVE MOSTLY FOR ITS FORM"
    show gaster trapped explain
    gaster "I THINK IS SOMEWHAT OLD, SO IT CAN HOLD AROUND 1GB, MAYBE A BIT MORE"
    show gaster trapped explain flip
    gaster "YOU CAN USE IT TO SAVE DIFFERENT KIND OF COMPUTER FILES, LIKE EXECUTABLES, TEXT FILES, IMAGE FI.."
    show papyrusImg nope
    papyrus "NO"
    extend ", NO "
    extend ", NO NO NO NO NO "
    extend ", NOOOOOOO... "
    show papyrusImg explainingPointing
    papyrus "WHAT I AM ASKING IS WHAT DO I DO WITH THE FILES YOU PUT ALREADY HERE.."
    show gaster trapped sorry flip
    gaster "OH "
    extend "I UNDERSTAND"
    show gaster trapped neutral flip
    show papyrusImg neutral
    gaster "WHAT I DID PUT ON THAT PENDRIVE WERE THE SOFTWARE THEY USED FOR THE DETERMINATION TANKS"
    gaster "THE BLUEPRINTS OF THE TANKS, THE SOURCE CODE OF THE SOFTWARE"
    gaster "AND THE SERVER IN WHICH THAT SOFTWARE RUNS"
    gaster "IT ALSO HAD SOME DOCUMENTATION BUT I DON'T KNOW IF ITS RELIABLE ENOUGH"
    show gaster trapped explain flip
    gaster "I DISCOVERED THAT THE SOFTWARE THEY USE TO CONTROL THE TANKS HAS AN API, SO IT SHOULD BE SOMEWHAT PAINLESS TO USE WITHOUT DESTROYING EVERYTHING"
    show gaster trapped neutral flip    
    gaster "SO, WE JUST NEED SOMEONE WHO KNOWS A LOT ABOUT MONSTERS SCIENCE, DETERMINATION AND PROGRAMMING"
    show papyrusImg annoyed
    papyrus "I HAVE 2 ANSWERS FOR THAT QUESTION AND I DON'T LIKE EITHER OF THOSE TWO"
    show gaster trapped dissapointed flip
    gaster "YOU HAVE 2 ANSWERS?"
    if pendriveTree < 1:
        $ pendriveTree += 1
    return

label pendriveSans:
    show gaster trapped neutral flip
    gaster "HAVE YOU THOUGHT ABOUT ASKING YOUR BROTHER?"
    show papyrusImg annoyed
    papyrus "DOES HE REMEMBER YOU?"
    show gaster trapped dissapointed flip
    gaster "WHAT THAT HAS TO DO WITH THIS?"
    gaster "DIDN'T YOU SAID SEVERAL TIMES THAT HE LIKES SCIENCE, ESPECIALLY WHEN IS REAL?"
    show gaster trapped neutral flip
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
    show gaster trapped dissapointed flip
    gaster "PAPYRUS?"
    show papyrusImg annoyed flip
    gaster "PLEASE CAN YOU TELL ME WHAT THE PROBLEM WITH YOUR BROTHER?"
    show papyrusImg dissapointed
    papyrus "I DON'T W{cps=*0.2}AAAAAAA{/cps}NNN{cps=*0.2}AAAAAAAAA{/cps}"
    show gaster descisive flip
    gaster "WHY?"
    gaster "HE'S YOUR BROTHER"
    gaster "HE LOVES YOU"
    papyrus "I KN{cps=*0.2}OOOWWW...{cps=*0.2}"
    show papyrusImg annoyed
    papyrus "IT'S JUST"
    papyrus "IF HE DOES REMEMBER YOU, HE WILL BE TOO SUSPICIOUS TO BE OF ANY HELP"
    show papyrusImg dissapointed
    papyrus "IF HE DOES NOT REMEMBER YOU, HE WILL NOT BELIEVE ME NO MATTER WHICH PROOF I HAVE AND WILL TRY TO CONVINCE ME YOU ARE A SOME SORT OF IMAGINARY FRIEND"
    show papyrusImg annoyed
    papyrus "IT'S NOT GOING TO BE THE FIRST TIME"
    show gaster trapped maybe flip
    gaster "I STILL DON'T SEE WHY YOU SHOULDN'T TRY"
    gaster "IF IT DOESN'T WORK WE CAN LOOP BACK AND IT WILL LIKE NEVER HAPPENED"
    show papyrusImg serious
    papyrus "I DON'T LIKE THAT EITHER"
    show gaster trapped sorry flip
    gaster "..."
    gaster "PAPYRUS..."
    gaster "PLEASE..."
    show papyrusImg dissapointed
    papyrus "{cps=*1.5}OK FINE I'LL ASK HIM{/cps}"
    show gaster trapped neutral flip
    gaster "THANKS YOU"
    show papyrusImg serious
    papyrus "IT'S NOT GOING TO WORK THOUGH"
    show gaster trapped ok flip
    gaster "BUT WE'RE GOING TO TRY AND THAT'S IMPORTANT"
    show papyrusImg dissapointed
    papyrus "YEAH... YOU RIGHT..."
    if pendriveTreeSans < 2:
        $ tryWithSans = True
        $ pendriveTreeSans += 1
    return

label pendriveAlphys:
    show gaster trapped maybe flip
    show papyrusImg neutral
    gaster "WHAT'S ABOUT THE ROYAL SCIENTIST?"
    show papyrusImg uhh
    papyrus "WHO?"
    show gaster trapped explain flip
    gaster "THE ROYAL SCIENTIST"
    gaster "YOUR FRIEND"
    gaster "THE SPOUSE OF YOUR OTHER FRIEND"
    gaster "THE FRIEND WHO SANS MET BEFORE YOU"
    show papyrusImg delight
    papyrus "AH YOU MEANT DR ALPHYS!"
    show papyrusImg neutral
    papyrus "SHE'S NOT THE ROYAL SCIENTIST ANYMORE"
    show gaster trapped angry flip
    gaster "WHAT? WHY?"
    show gaster trapped angry
    gaster "THIS MAKES NO SENSE, EVERYBODY HAS AN ACCIDENT"
    show gaster trapped angry flip
    gaster "YOU CANNOT GO AND DO SOMETHING LIKE THAT TO A PROMISING CAREER!"
    hide gaster
    play sound "music/fx/steps.wav"
    gaster "I'M GOING TO COMPLAIN TO THE KING ABOUT THIS! I..."
    show gaster trapped dissapointed flip at fade:
        xpos 0.4
    play sound "music/fx/steps.wav"
    pause(0.5)
    gaster "I CANNOT GO AND COMPLAIN ABOUT THIS"
    show papyrusImg worried
    papyrus "DO YOU NEED A MOMENT?"
    gaster "NO..."
    gaster "I..."
    gaster "I AM FINE"
    if pendriveTreeAlphys < 1:
        $ pendriveTreeAlphys += 1
    return

label pendriveAreYouOk:
    show papyrusImg worried
    papyrus "ARE YOU SURE YOU ARE OK?"
    show gaster trapped dissapointed flip
    gaster "IT'S "
    extend "THAT "
    extend "FEELING"
    show gaster trapped maybe flip
    gaster "YOU KNOW THE ONE"
    show gaster trapped dissapointed flip
    gaster "THE ONE WHEN YOU REALIZE YOU WANT TO HELP SOMEONE BUT YOU ARE COMPLETELY USELESS TO DO IT"
    show papyrusImg uhh
    papyrus "DO YOU REALLY THINK DR ALPHYS IS GOOD AT SCIENCE?"
    show gaster trapped descisive flip
    gaster "YES"
    gaster "OF COURSE"
    show gaster trapped explain flip
    gaster "VERY, VERY TALENTED INDEED"
    show gaster trapped descisive flip
    gaster "SHE BASICALLY REDISCOVERED GOOD CHUNK OF THE THEORY OF DETERMINATION AFTER I..."
    show gaster trapped dissapointed flip
    gaster "SCREW EVERYTHING UP"
    show papyrusImg surprised happy
    papyrus "WOWIE!"
    show gaster trapped explain flip
    gaster "I MUST HAVE SOME SORT OF ADMIRATION FOR A WORK LIKE THAT, NO MATTER HOW ACTUALLY..."
    show gaster trapped dissapointed flip
    gaster "FINISHED"
    show papyrusImg confused
    papyrus "I GUESS IT WOULD NOT BEEN THAT TERRIBLE IF SHE HAD INFORMED WHAT HAPPENED WHEN ACTUALLY HAPPENED"
    show gaster trapped angry flip
    gaster "THAT'S WHAT I'M SAYING"
    gaster "PLUS, SHE WAS EXPERIMENTING WITH DYING MONSTERS"
    show gaster trapped explain flip
    gaster "WHAT THEY WERE EVEN EXPECTING TO HAPPEN?"
    show papyrusImg nope
    papyrus "NOW YOU ARE SAYING THAT I KINDA SEE TORIEL'S POINT"
    show gaster trapped ehem flip
    gaster "IT WAS HER?"
    gaster "..."
    show gaster trapped angry flip
    gaster "OF COURSE IT WAS HER"
    if pendriveTreeAlphys < 2:
        $ pendriveTreeAlphys += 1
    return

label pendriveAlphysThree:
    show gaster trapped angry flip
    gaster "IN WHAT THEY ARE WASTING HER TALENTS ANYWAY?"
    show papyrusImg uhh
    papyrus "WHO?"
    gaster "YOUR FRIEND"
    gaster "THE ONE WHO DID THE EXPERIMENTS"
    papyrus "DR ALPHYS?"
    show papyrusImg neutral
    papyrus "SHE'S WORKING AS AN ARCHIVIST UNDER TORIEL!"
    show gaster trapped dissapointed flip
    gaster "OF COURSE IT HAS TO BE THE QUEEN"
    papyrus "DR ALPHYS ALWAYS TELLS ME THAT IS DIFFICULT FOR HER TO LEARN THE NEW CRAFT, BUT TORIEL HAS TOLD ME SHE'S GREAT IT AND SHE'S DOING A GREAT JOB"
    show gaster trapped sorry flip
    gaster "OH"
    papyrus "DR ALPHYS IS SO GOOD AT GETTING INFORMATION THAT TORIEL IS ALWAYS ASKING HER ABOUT DIFFERENT STUFF, INCLUDING A LOT OF HUMANS RELATED THINGS"
    papyrus "APPARENTLY, THE IDEA IS, IF TORIEL IS UNAVAILABLE, DR ALPHYS CAN PERFECTLY REPLACE HER"
    show papyrusImg delight
    papyrus "I THINK IT SUITS HER"
    gaster "LOOK AT THAT"
    show gaster trapped neutral flip
    gaster "SO, YOU THINK SHE CAN HELP US"
    show papyrusImg confused
    papyrus "DO I THINK THAT?"
    show papyrusImg delight
    papyrus "OF COURSE I THINK THAT!"
    papyrus "I HAVE NO WAY TO KNOW THIS BUT I'M SURE THIS GOING TO BE REALLY EASY FOR HER"
    papyrus "SHE'S THAT AWESOME"
    show gaster trapped ok flip
    gaster "GO AHEAD MY DEAR PAPYRUS"
    if pendriveTreeAlphys < 3:
        $ pendriveTreeAlphys += 1
        $ tryWithAlphys = True
    return

label pendriveAlphysFailState:
    show papyrusImg uhh
    papyrus "DID SHE SAID SHE NEEDS MORE TIME?"
    show gaster trapped explain flip
    gaster "WHAT I DID UNDERSTAND FROM WHAT SHE SAID"
    show gaster trapped neutral flip
    gaster "APPARENTLY THE DAY YOU GAVE HER THE FILES WAS NOT IDEAL TO WORK IN A PROGRAM TO ACCELERATE THIS PROCESS"
    show papyrusImg annoyed
    papyrus "SO, THEN, WHAT WE GOING TO DO?"
    gaster "YOU HAVE TO FIND A MOMENT DURING DAY 2 OF THE LOOP TO GIVE THE FILES TO HER"
    papyrus "BUT..."
    show papyrusImg confused
    papyrus "I'M ALWAYS SUPER DISTRACTED DURING THE 2ND DAY"
    show papyrusImg dissapointed
    papyrus "I EVEN GET KINDA DRUNK FOR A MOMENT AND THAT SO NOT ME"
    show papyrusImg uhh
    papyrus "IN WHICH MOMENT I CAN DO IT?"
    show gaster trapped dissapointed flip
    gaster "I'M NOT SURE ABOUT THAT PAPYRUS"
    show gaster trapped neutral flip
    gaster "I'M SURE MUST BE A SIMPLE WAY TO SOLVE THIS PUZZLE, BUT IT'S MUST BE ON THE SECOND DAY"
    show gaster trapped maybe flip
    gaster "MONSTERS ARE A FICKLE BUNCH"
    show gaster trapped neutral flip
    gaster "EVEN IF YOU GIVE HER THIS DURING DAY 2, THERE'S NOT GUARANTEE IS GOING TO WORK"
    show papyrusImg surprised
    papyrus "WOWZIE"
    if day == 1:
        show papyrusImg annoyed
        papyrus "WHAT ABOUT IF I GO NOW?"
        hide gaster
        gaster "LET'S ME CHECK"
        pause(2.0)
        show gaster trapped neutral flip at fade:
            xpos 0.4
        gaster "THEY ARE SLEEPING"
        show papyrusImg dissapointed
        papyrus "UNDYNE IS GOING TO SENT MY HEAD IN A BOX TO SANS IF I GO NOW"
        show gaster trapped dissapointed flip
        gaster "AFTER WHAT HAPPENED TODAY?"
        papyrus "YES!"
        show gaster trapped maybe flip
        gaster "IF YOU SAY SO"
    show papyrusImg uhh
    papyrus "..."
    show papyrusImg annoyed
    papyrus "OK, BUT IF I FAIL DURING THE 2ND DAY?"
    papyrus "I WILL NEED TO LIVE THE NEXT 2 DAYS BEFORE TRYING AGAIN?"
    show gaster trapped explain flip
    gaster "I CANNOT SENT YOU BACK TO ANY MOMENT EXCEPT WHEN YOU WERE ABOUT TO SAVE YOUR FRIEND, BUT"
    papyrus "BUT?"
    show gaster trapped dissapointed flip
    gaster "I CAN TRIGGER IT AT ANY MOMENT ACTUALLY..."
    papyrus "YOU COULD HAVE DONE THAT SINCE THE BEGINNING"
    show gaster trapped dissapointed
    gaster "OF COURSE..."
    show papyrusImg confused
    papyrus "WELL, YES, THIS IS THE FIRST TIME WE HAVE A TIME CONSTRAIN TO THE PLAN..."
    show papyrusImg annoyed
    papyrus "JUST PUT THEM ON THE OPTIONS"
    $ resetFromQuestionMenu = True
    show gaster trapped neutral flip
    gaster "DONE"
    show papyrusImg delight
    papyrus "THANK YOU!"
    if pendriveTreeAlphys < 4:
        $ pendriveTreeAlphys += 1
    return
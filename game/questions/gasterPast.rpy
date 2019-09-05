label gasterGerson:
  show gaster trapped oh flip
  gaster "WAIT"
  gaster "ARE THEY STILL CALLING HIM KING FLUFFYBUNS?"
  show papyrusImg neutral
  papyrus "THAT'S JUST GERSON, HE HAD A SHOP AT WATERFALL AND UNDYNE LOVED TO HEAR SOME WAR STORIES FROM HIM"
  papyrus "I JUST HEARD HIM CALLING HIM LIKE THAT ONCE AND..."
  papyrus "KIND OF JUST STUCK"
  gaster "IS THE HAMMER OF JUSTICE STILL ALIVE?"
  show gaster trapped dissapointed flip
  gaster "OH, I REMEMBER HIM SELLING THOSE AWFUL APPLE CRABS"
  gaster "HE NEVER LIKED ME"
  gaster "I GUESS IS BECAUSE FOR BEEN A SKELETON I WAS KIND OF USELESS"
  show papyrusImg worried
  papyrus "YOU SAY YOU DESIGNED THE CORE"
  gaster "BUT THAT IS NOT FOR WHAT WE SKELETONS WERE CREATED FOR I'M AFRAID"
  papyrus "GERSON HAS NEVER STRUCK ME AS A JUDGEMENTAL TYPE"
  papyrus "ARE YOU SURE YOU DID NOT IMAGINED THAT?"
  gaster "WELL..."
  show gaster trapped sad flip
  gaster "YOU DIDN'T MET HIM DURING THE WAR..."
  gaster "AND YOU DIDN'T FAIL TO FULLFILL YOUR DUTIES..."
  gaster "SO..."
  show gaster trapped dissapointed flip
  gaster "BOTH, I GUESS..."
  if gasterPast < 1:
    $ gasterPast = gasterPast + 1
  return

label gasterDuties:
  show papyrusImg worried
  papyrus "DID YOU SAID SOMETHING ABOUT FAILING TO FULLFILL DUTIES?"
  show gaster trapped sad flip
  gaster "YES, I DO REMEMBER SAYING THAT"
  show papyrusImg uhh
  papyrus "WHY ARE YOU SAYING THAT?"
  show papyrusImg worried
  papyrus "BECAUSE, I'M GUESSING THIS NEED REPEATING"
  papyrus "YOU SAID YOU DESIGNED THE CORE"
  show gaster trapped explain flip
  gaster "I'M REALLY GOOD AT THE THEORY OF MAGIC AND SCIENCE"
  show gaster trapped maybe flip
  gaster "ACTUALLY APPLY IT, NOT THAT MUCH"
  show papyrusImg annoyed
  papyrus "OH"
  gaster "ON PEACE, IS IT NOT SO BAD"
  show gaster trapped sad flip
  gaster "BUT YOU DON'T CREATE SKELETONS ON PEACE TIME"
  gaster "AND I WAS PULL OUT FROM THE SKELETONS UNIT AT THE HEAT OF THE WAR"
  gaster "CONSIDERING I SURVIVED SOMEHOW"
  show gaster trapped dissapointed flip
  gaster "I HAVE NO IDEA IF THAT IS A GOOD THING OR NOT"
  papyrus "..."
  if gasterPast < 2:
    $ gasterPast = gasterPast + 1
  return
  
label gasterWar:
  show papyrusImg surprised happy
  papyrus "WERE YOU ALIVE DURING THE GREAT WAR?"
  show gaster trapped oh flip
  gaster "THE ONE AGAINST HUMANS?"
  gaster "YES, YES I WAS"
  show papyrusImg curious
  papyrus "THEN YOU MUST BE REALLY OLD"
  show gaster trapped sorry flip
  gaster "I'M QUITE OLD TECHNICALLY"
  gaster "I'M NOT AS OLD THE HAMMER OF JUSTICE"
  gaster "OR THE KING OR QUEEN FOR THAT MATTER"
  gaster "BUT I WAS CREATED DURING THE WAR"
  show papyrusImg annoyed
  papyrus "YOU KEEP SAYING CREATED"
  show gaster trapped angry flip
  gaster "BUT... MY DE..."
  show gaster trapped dissapointed flip
  gaster "OF COURSE, OF COURSE, YOU MUST HAVE FORGOT ABOUT THAT AS WELL"
  gaster "SINCE, LIKE I HAVE ALREADY TOLD YOU, I CREATED YOU"
  papyrus "THEN..."
  show gaster trapped sorry flip
  gaster "I WAS CREATED DURING THE HEAT OF THE WAR, TO BE PART OF THE SKELETON UNITS"
  gaster "I WAS CONSIDERED DEFECTIVE AND SENT TO THE BACKLINES TO HELP IN ANYTHING I COULD"
  gaster "AND IT WASN'T UNTIL THE MONSTERS GOT TRAPPED ON THE UNDERGROUND I COULD BE..."
  gaster "USEFUL, IN A SENSE"
  if gasterPast < 2:
    $ gasterPast = gasterPast + 1
  return

label gasterCreation:
  show papyrusImg sorry
  papyrus "SO..."
  papyrus "HOW YOU GO ON TO CREATE SKELETONS?"
  show gaster trapped oh flip
  gaster "COME AGAIN?"
  papyrus "YOU KNOW..."
  papyrus "USUALLY YOU NEED TWO PEOPLE WHO LOVE EACHOTHER VERY MUCH..."
  papyrus "AND THE BEES AND THE FLOWERS AND..."
  show gaster trapped descisive flip
  gaster "DO YOU MEAN SEX?"
  show gaster trapped angry flip
  gaster "NO, NO, NO, NO, THAT'S GROSS, NOOOOO"
  show papyrusImg uhh
  papyrus "SO YOU DON'T NEED A SKELETON PARTNER TO CREATE A SMALLER SKELETON?"
  gaster "WHERE DID YOU..."
  gaster "..."
  show gaster trapped dissapointed flip
  gaster "OF COURSE, OF COURSE..."
  gaster "WELL..."
  show gaster trapped maybe flip
  gaster "YOU USE MAGIC"
  show papyrusImg confused
  papyrus "WE USE MAGIC FOR EVERYTHING, WE'RE MONSTERS"
  papyrus "WE USE MAGIC EVEN FOR S.."
  show gaster trapped descisive flip
  gaster "I KNOW I KNOW"
  show gaster trapped angry flip
  gaster "AND, IN THE NAME OF THE DELTARUNE, IT IS THE GROSSEST SPELL I HAVE EVER HAD THE DISPLEASURE TO LEARN ABOUT"
  show papyrusImg nope
  papyrus "THAT'S PROBABLY THE FIRST TIME I HEARD THAT SAYING, YOU REALLY ARE OLD!"
  show papyrusImg annoyed
  papyrus "AND REALLY CRANKY"
  show gaster trapped dissapointed flip
  gaster "I'M FINE"
  gaster "I´M COMPLETELY FINE"
  if gasterPast == 2:
    $ gasterPast = gasterPast + 1
  return

label skeletonKind:
  show papyrusImg uhh
  papyrus "OK"
  papyrus "AHH..."
  papyrus "IF YOU DON'T CREATE SKELETONS LIKE THE OTHER MONSTERS..."
  show papyrusImg annoyed
  papyrus "HOW... YOU DO IT... THEN???"
  show gaster trapped sad flip
  gaster "THE HISTORY OF US THE SKELETON KIND IS QUITE INTERESTING"
  gaster "WE ACTUALLY ARE A WEIRD KIND OF FAILED EXPERIMENT"
  show gaster trapped maybe flip
  gaster "THAT AT THE END WAS QUITE USEFUL ANYWAY"
  papyrus "WHAT."
  show gaster trapped neutral flip
  gaster "THE NAME OF THE MONSTER ACREDITED WITH THE ORIGINAL SPELL WAS LOST TO THE ANNALS OF TIME BUT"
  gaster "THE LEGEND SAYS THEY WERE INSPIRED BY THE HUMAN REMAINS FOUND IN AN ABANDONED HUMAN PRISON LONG TIME AGO"
  papyrus "WAIT."
  gaster "THE ORIGINAL IDEA IT SEEMS TO BE THAT, IF YOU CREATE A MONSTER USING HUMAN REMAINS"
  gaster "WILL HAVE THE MAGIC CAPABILITIES OF A MONSTER AND THE PHYSICAL STRENGTH OF A HUMAN"
  show papyrusImg surprised
  papyrus "HUMANS HAVE SKELETONS INSIDE THAT FLESHY BODY OF THEM?!"
  show gaster trapped oh flip
  gaster "I KNOW, CRAZY"
  show papyrusImg neutral
  show gaster trapped neutral flip
  gaster "THE SPELL WAS REFINED DURING THE YEARS AND NOW YOU DON'T NEED HUMANS REMAINS TO CREATE SKELETONS"
  gaster "JUST THE SPELL"
  gaster "THE ACTUAL PROBLEM WITH A SKELETON WAS, WHILE OUR MAGIC CAPABILITIES ARE EQUAL OR MAYBE EVEN BETTER THAN ANOHTER KIND OF MONSTER IN AVERAGE"
  gaster "OUR PHYSICAL CAPABILITIES ARE NOT GOOD ENOUGH TO EVEN COMPARE WITH HUMANS"
  gaster "WE'RE BETTER THAN THE AVERAGE MONSTER THOUGH"
  gaster "SO, WHILE THE EXPERIMENT COULD BE CONSIDERED A FAILURE"
  gaster "WE TURN OUT TO BE QUITE USEFUL ANYWAY AND WORTH KEEPING AROUND"
  gaster "ESPECIALLY WHEN YOU NEED SOLDIERS IN A HURRY"
  show papyrusImg annoyed
  papyrus "THAT WASN'T AN ANSWER TO MY QUESTION"
  show gaster trapped ok flip
  gaster "YOU NEED TO START SINCE THE BEGINNING MY DEAR PAPYRUS"
  if gasterPast == 3:
    $ gasterPast = gasterPast + 1
  
  return

label superSoldiers:
  show papyrusImg annoyed
  papyrus "ARE YOU SAYING THAT SKELETONS WERE LIKE THE SUPER SOLDIERS OF MONSTER KIND?"
  show gaster trapped oh flip
  gaster "NO... WE WEREN..."
  gaster "..."
  show gaster trapped dissapointed flip
  gaster "NOW YOU ARE SAYING THAT IT MAKE SENSE..."
  show gaster trapped sad flip
  gaster "BUT, THE SPELL DOES NOT CREATE CONSISTENT RESULTS, AND SKELETONS ARE AS VARIED AS ANY OTHER MONSTER KIND"
  show gaster trapped neutral flip
  gaster "WHEN THE FIRST SKELETONS WERE CREATED, THEY LEARNED HOW TO DO THE SPELL AND STARTED TO BE A NORMAL PART OF THE MAKEUP OF OUR PEOPLE"
  show gaster trapped angry flip
  gaster "AND, UNLIKE THE GROSSEST SPELL IN EXISTENCE"
  show papyrusImg delight
  papyrus "I HEARD IS KINDA FUN"
  gaster "DON'T... EVEN... THINK ABOUT IT..."
  gaster "..."
  show gaster trapped dissapointed flip
  gaster "WHERE WAS I?"
  show papyrusImg neutral
  papyrus "YOU WERE SAYING THAT THE SPELL TO CREATE SKELETONS WAS BETTER THAN SEX"
  show gaster trapped explain flip
  gaster "OF COURSE IT IS! DON'T EVEN MENTION IT!"
  show gaster trapped sad flip
  gaster "1- IT'S NOT GROSS"
  gaster "2- IT'S ONLY NEEDS 1 MONSTER"
  show gaster trapped maybe flip
  gaster "(WHILE I HAVE TO CONCEDE IT'S NEEDS A POWERFUL AND EDUCATED ONE)"
  show gaster trapped sad flip
  gaster "AND 3- IT DOESN'T CREATE A USELESS SMALL MONSTER YOU HAVE TO KEEP EDUCATING UNTIL THEY BECOME USEFUL"
  show gaster trapped proud flip
  gaster "BUT A FULLY INDEPENDENT AND FUNCTIONAL ADULT SKELETON" 
  show papyrusImg surprised
  papyrus "WAIT, I NEVER WAS A CHILD?"
  show gaster trapped oh flip
  gaster "WHAT ARE YOU TALKING ABOUT?"
  show papyrusImg surprised flip
  papyrus "I DIDN'T HAVE A CHILDHOOD?"
  gaster "WHY DO YOU SOUND SO DISTRESSED, I DON'T GET IT"
  show papyrusImg surprised
  papyrus "AAAHHHHH!!!!"
  if gasterPast == 4:
    $ gasterPast = gasterPast + 1
  return

label noChildhood:
  show papyrusImg surprised
  papyrus "WAS I NEVER BEEN A CHILD?!"
  show gaster trapped oh flip
  gaster "I STILL DON'T SEE THE PROBLEM..."
  papyrus "HOW THAT IS NOT A PROBLEM?"
  show gaster trapped angry flip
  gaster "BEEN A KID IS THE WORST"
  show papyrusImg annoyed
  papyrus "AH?"
  gaster "YOU ARE BORN, BEEN ABLE TO DO ABSOLUTLY NOTHING AND THE ONLY THING YOU CAN DO IS TRUST IN WHOEVER DECIDED TO TAKE CARE OF YOU"
  show gaster trapped sad flip
  gaster "IF THEY ARE GOOD PEOPLE AND BEEN ABLE TO DEAL WITH THEIR OWN PROBLEMS WITH ENOUGH STABILITY, YOU'RE FINE"
  show gaster trapped angry flip
  gaster "THEY FAIL IN ANY OF THOSE CATEGORIES AND YOUR LIFE BECOMES A LIVING HELL UNTIL YOU GET OUT"
  gaster "AND ANYWAY YOU HAVE TO LEARN TO LIVE WITH THE SCARS OF THEIR MISTAKES!"
  papyrus "THAT'S A STRONG OPINION"
  gaster "AND THEN THEY GO"
  gaster "'HOW YOU DARE TO DO THIS TO ME I'M YOUR MOTHER/FATHER/PARENTAL FIGURE'"
  gaster "AND I'M LIKE"
  gaster "'I WANT TO PUNCH YOU IN THE FACE!'"
  show papyrusImg nope
  papyrus "HOW MANY PARENTS DID YOU PUNCH IN THE FACE?"
  gaster "NONE"
  gaster "I WOULD MAKE THE LIFE OF THOSE KIDS WAY WORSE"
  gaster "BUT YOU GUYS GOT SOME OF THEM INTERESTED IN SCIENCE, THAT WAS, SOMETHING HELPFUL"
  show papyrusImg annoyed
  papyrus "OH!"
  papyrus "..."
  if gasterPast == 5:
    $ gasterPast = gasterPast + 1
  return

label blankScienceEncyclopedia:
  papyrus "THEY JUST FOUND IN THE LIBRARY A BLANK BOOK"
  gaster "THAT MUST BE THE SCIENCE ENCYCLOPEDIA"
  papyrus "SO, YOU WROTE IT"
  gaster "EXACTLY"
  gaster "THAT WAS WHAT THE QUEEN ASKED ME TO DO, AFTER THE HAMMER OF JUSTICE SUGGESTED IT"
  gaster "ALL THAT INVESTIGATION WAS WHAT LEAD TO ME BECOMING ROYAL SCIENTIST"
  papyrus "I SEE"
  papyrus "I FOUND THAT FUNNY THOUGH"
  papyrus "I REALLY DON'T KNOW WHY"
  gaster "THIS JUST MAKES ME RESPONSIBLE OF WHAT HAPPENED DURING THE INVESTIGATION OF THE LAST ROYAL SCIENTIST"
  gaster "MY CARELESSNESS LEAD TO A HUGE TRAGEDY AND I CANNOT STRESS ENOUGH THAT"
  papyrus "IN A WAY MAKE ME WONDER HOW SHE KNOWS WHAT SHE KNOWS ABOUT SCIENCE"
  gaster "I DIDN'T TEACH HER SCIENCE"
  gaster "IT COULD BE SOMEONE ELSE, MAYBE WHO LEARNT USING THE BOOKS"
  gaster "OR SHE TAUGHT HERSELF"
  gaster "AFTER ALL KNOWLEDGE IT'S NOT MINE"
  papyrus "SO, IT DOESN'T BUBBLE"
  gaster "YOU FORGOT BECAUSE I TAUGHT YOU AND THAT MEMORY IS RELATED TO ME"
  gaster "I DIDN'T TAUGHT HER, SO THAT MEMORY IS NOT RELATED TO ME"
  papyrus "INTERESTING"
  papyrus "THEN MOST PROBABLY WAS DR. ALPHYS DIDN'T KNEW ANYTHING ABOUT DETERMINATION WHEN SHE STARTED HER EXPERIMENTS"
  gaster "I HAVE DONE WORSE, I DON'T HAVE ANY MORAL GROUND"
  papyrus "THEN, IF SOMEONE TAUGHT HER, WHO COULD BE?"
  gaster "MY BET WOULD BE SANS"
  papyrus "BUT SHE'S LIKE 3 YEARS OLDER THAN HIM"
  gaster "BUT SANS HAS BEEN AN ADULT FOR LONGER"
  papyrus "RIGHT, WE SKELETONS CANNOT BE KIDS"
  gaster "BUT ALSO CAN BE YOU"
  papyrus "UH?"
  papyrus "BUT WOULD KNOW THAT, RIGHT?"
  gaster "THE BRAIN IS REALLY GOOD AT MAKING PATTERNS OUT OF NOTHING"
  gaster "MAYBE SHE REMEMBERING YOU OR SANS WAS TIED TO REMEMBERING ME"
  papyrus "SO, IS A TREE, AND THE ACTION JUST GO ONE LEVEL DEEP"
  papyrus "AND THE LEAVES GET LOOSE"
  gaster "EXACTLY"
  papyrus "..."
  gaster "IN A WAY, THAT'S WHY WE HAVE DATA STRUCTURES"
  if gasterPast == 6:
    $ gasterPast = gasterPast + 1
  return 

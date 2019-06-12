label foundSomePapers:
  show papyrusImg annoyed
  papyrus "DID YOU SAID YOUR DOCUMENTS DIDN'T SURVIVE YOU BEEN FORGOTTEN?"
  show gaster trapped neutral flip
  gaster "I DON'T HAVE ACTUAL PROOF REALLY"
  gaster "BUT I IMAGINE IF THAT AMALGAMATES THING HAPPENED IT'S MUST BE BECAUSE THOSE TRACES OF ME DISSAPEARED AS WELL"
  papyrus "WE FOUND SOME PAPERS OF YOURS IN THE SCHOOL BASEMENT"
  show gaster trapped dissapointed flip
  gaster "THE SCHOOL..."
  show papyrusImg explainingPointing
  papyrus "WE DUMPED EVERYTHING OF THE LABORATORY THERE"
  show papyrusImg neutral
  papyrus "AND DR. ALPHYS HAS BEEN WORKING CLASSIFICATING EVERYTHING SINCE THEN"
  papyrus "SHE SAID THIS WEEK SHE FOUND TONS OF DOCUMENTS WRITTEN WITH 'WEIRD SYMBOLS'"
  show gaster trapped oh flip
  gaster "DO NOT TELL ME WHAT HAPPENED WAS SHE COULDN'T READ THEM?"
  show papyrusImg confused
  papyrus "SHE COULD HAVE ASKED SANS ABOUT IT, THAT'S NOT THE POINT"
  show papyrusImg explainingPointing
  papyrus "THE POINT HERE IS THOSE DOCUMENTS JUST APPEARED THIS LAST 3 DAYS"
  show gaster trapped happy flip
  gaster "IT'S THE DETERMINATION STORED BY THE WEKUFE"
  gaster "IT'S NOT ONLY AFFECTING THE FACT I CAN TALK WITH YOU"
  gaster "BUT MY IMPRINT IS ALSO BACK"
  show papyrusImg surprised
  papyrus "WAIT, THEN WHY THE CORE DIDN'T JUST..."
  papyrus "POOF!"
  show gaster trapped sad flip
  gaster "MY THEORY IS THOSE DOCUMENTS WERE BLANK PAGES UNTIL YESTERDAY"
  gaster "AND NOBODY PAID ANY MIND TO THEM"
  gaster "JUST LIKE NOBODY SEEMS TO HAVE ASKED THEMSELVES WHO DESIGNED THE CORE"
  show papyrusImg annoyed
  papyrus "THAT KINDA MAKE SENSE"
  show gaster trapped neutral flip
  gaster "DID YOU READ THEM? IS THERE SOMETHING ABOUT MY TRANSCRIPTS ABOUT DETERMINATION?"
  gaster "MAYBE WITH BOTH MY OLD NOTES ABOUT THE ORIGINAL INVESTIGATION AND SKELETON CREATION PLUS THE DISCOVERIES OF THE CURRENT ROYAL SCIENTIST CAN HELP INTO GET ME OUT!"  
  show papyrusImg uhh
  papyrus "I THINK THOSE ARE ABOUT THE TIME YOU DECIDED TO CREATE ME????"
  gaster "..."
  show gaster trapped maybe flip
  gaster "NOTHING AGAINST MY NOTES ABOUT YOU AND SANS BUT..."
  show gaster trapped dissapointed flip
  gaster "I DON'T THINK ME COMPLAINING ABOUT YOU IS GOING TO HELP ME COME BACK"
  show papyrusImg confused
  papyrus "I WOULDN'T CALL THAT COMPLAINING..."
  gaster "DID I CALLED YOU 'ASSISTANT' SEVERAL TIMES IN A ROW?"
  show papyrusImg uhh
  papyrus "YES?"
  show gaster trapped sad flip
  gaster "THEN I WAS COMPLAINING"
  if sansPapyrusPast < 1:
    $ sansPapyrusPast = sansPapyrusPast + 1
  return

label sansWantsABrother:
  show papyrusImg serious
  papyrus "SO, DID YOU CREATE ME BECAUSE SANS WAS BORED?"
  show gaster trapped maybe flip
  gaster "I DID ASSUME HE WAS PRANKING BECAUSE HE WAS BORED BUT I ACTUALLY I DID MAKE THE WRONG ASSUMPTION ON THAT REGARD"
  show gaster trapped sad flip
  gaster "BUT HIM WANTING A LITTLE BROTHER WAS SOMETHING HE DIRECTLY TOLD ME"
  gaster "LIKE, 3 TIMES A DAY"
  show gaster trapped dissapointed flip
  gaster "I TOLD HIM, SEVERAL TIMES, THAT 1. YOU WERE NOT GOING TO BE A CHILD AND 2. YOU WERE NOT GOING TO BE REALLY HIS BROTHER BECAUSE THAT'S NOT HOW SKELETONS WORK, BUT..."
  gaster "EH"
  show gaster trapped maybe flip
  gaster "YOU TWO ARE BROTHERS"
  show papyrusImg uhh
  papyrus "NOW I'M THINKING ABOUT IT, WHY DID YOU CREATE SANS IN THE FIRST PLACE?"
  papyrus "I DON'T KNOW WHY, BUT I HAVE THIS FEELING YOU REALLY NEVER WANTED ANY COMPANY"
  show gaster trapped dissapointed flip
  gaster "THE QUEEN FORCED ME"
  show papyrusImg delight
  papyrus "TORIEL MUST HAS LOOKED AT YOU AND THOUGHT YOU WERE TOO LONELY"
  gaster "WELL, THAT'S ALSO THE THEORY I DO HAVE"
  show gaster trapped maybe flip
  gaster "BUT SHE TRIED TO CONVINCE ME UNDER THE ARGUMENT THAT SKELETONS SHOULD NOT GO EXTINCT AGAIN"
  show gaster trapped sad flip
  gaster "I TOLD HER SHE COULD DO THAT HERSELF, THAT'S THE IDEA BEHIND THE CREATION OF SKELETONS AFTER ALL"
  show gaster trapped dissapointed flip
  gaster "BUT THEN SHE TOLD ME THAT IT WAS AN ORDER"
  show papyrusImg surprised
  papyrus "WOWIE"
  show papyrusImg delight
  papyrus "EVERYTHING IS ALWAYS MORE DRY THAN I CAN IMAGINE"
  gaster "I THINK SHE ALSO WROTE A SOME SORT OF RULE WHICH IT SAYS THAT, UNTIL CERTAIN THEREHOLD OF SKELETON POPULATION IS REACHED, EVERY SINGLE SKELETON SHOULD CREATE A NEW ONE AFTER REACHING CERTAIN AGE"
  gaster "BUT I DON'T THINK ANYONE REMEMBERS, BECAUSE"
  show gaster trapped maybe flip
  gaster "I'M TRAPPED IN THE DARKNESS"
  show papyrusImg surprised happy
  papyrus "THAT MEANS THAT EVENTUALLY I HAVE TO CREATE MY OWN LITTLE BROTHER?"
  show gaster trapped angry flip
  gaster "PAPYRUS, PLEASE"
  gaster "1. WE DON'T HAVE THE SAME BIOLOGICAL STRUCTURE THAN OTHER KIND OF MONSTERS, THERE BEFORE WE DON'T HAVE THE SAME FAMILY STRUCTURE"
  gaster "AND 2. EVEN IF WE COULD, YOU WILL NOT CREATE A LITTLE BROTHER"
  show gaster trapped sad flip
  gaster "YOU WILL CREATE YOUR SON"
  show gaster trapped sad
  gaster "OR DAUGHTER"
  show gaster trapped sad flip
  gaster "OR CHILD"
  show papyrusImg nope
  papyrus "WAIT"
  show papyrusImg surprised happy
  papyrus "YOU CAN CREATE SKELETONS OF DIFFERENT GENDERS?"
  show gaster trapped angry flip
  gaster "OF COURSE YOU CAN"
  gaster "I JUST GOT UNLUCKY AND CREATED 2 MALES"
  show papyrusImg delight
  papyrus "WHAT? DID YOU WISH I WERE A GIRL?"
  gaster "OF COURSE NOT PAPYRUS, HOW COULD EVER THOUGHT THAT"
  show gaster trapped sad flip
  gaster "I WANTED SANS TO BE A GIRL"
  if sansPapyrusPast < 2:
    $ sansPapyrusPast = sansPapyrusPast + 1
  return

label skeletonWave:
  show papyrusImg uhh
  papyrus "THEN WE ARE LIKE, THE 2ND WAVE OF SKELETONS?"
  show gaster trapped maybe flip
  gaster "IF YOU MEAN WE ARE THE SKELETONS CREATED AFTER THE EXTINCTION OF THE 1ST TRIBE, THEN YOU ARE CORRECT"
  show papyrusImg surprised happy
  papyrus "THEN WE SHOULD USE AFROS AND ELEPHANT PANTS!"
  show gaster trapped angry flip
  gaster "HAVE YOU BEEN WATCHING HUMAN MEDIA?"
  show papyrusImg delight
  papyrus "OF COURSE!"
  show papyrusImg confused
  papyrus "I MEAN, I LOVE MY SEXY RECTANGLE, BUT HE CAN PRODUCE CERTAIN AMOUNT OF CONTENT IN A YEAR..."
  show gaster trapped dissapointed flip
  gaster "I WILL NOT ASK ANY FURTHER"
  gaster "..."
  show gaster trapped neutral flip
  gaster "WHILE I'M CURIOUS OF WHY YOU AREN'T THAT PERTURBED OVER THE FACT THAT HUMANS DESTROYED ALL OF THE ORIGINAL SKELETONS"
  show papyrusImg neutral
  papyrus "WE WERE ALWAYS TOLD THE HUMANS DECIMATED THE MONSTERS"
  papyrus "I ASSUMED SOMETHING AMONG THOSE LINES HAPPENED WHEN YOU SAID 'SKELETON TRIBE'"
  papyrus "THE MONSTERS HAVE NOT ORGANIZED IN SPECIES TRIBES IN CENTURIES I BELIEVE"
  papyrus "AND FRISK AND I CONFIRMED WE WERE THE ONLY SKELETONS AROUND"
  gaster "VERY WELL"
  show gaster trapped sad flip
  gaster "AS INSIGHTFUL AS USUAL"
  papyrus "WHAT I'M WONDERING THOUGH, IF YOU HAVE EVER MET ANOTHER SKELETON APART OF SANS AND ME"
  gaster "I..."
  gaster "HAVEN'T"
  show gaster trapped neutral flip
  gaster "HOW DID YOU THOUGHT OF THAT?"
  papyrus "I ASSUMED YOU WANTED TO CREATE A SKELETON OF ANOTHER GENDER BECAUSE YOU WANTED TO MEET AN SKELETON OF ANOTHER GENDER"
  papyrus "PLUS, YOU ALWAYS SAID YOU WERE CREATED AFTER THE TRIBE WAS NO MORE FOR BEEN PART OF A NEW UNIT IN THE WAR"
  show papyrusImg explainingPointing
  papyrus "MEANING THAT ALL THE SKELETON CREATED WENT TO FIGHT, EXCEPT YOU"
  gaster "AHHH..."
  gaster "VERY WELL"
  show papyrusImg surprised happy
  papyrus "BUT NOW I THINK ABOUT IT, MAYBE YOU FAIL IN CREATING A GIRL SKELETON BECAUSE YOU NEVER MET A GIRL SKELETON"
  show gaster trapped dissapointed flip
  gaster "I DON'T THINK SO..."
  gaster "IT MIGHT HELP THOUGH"
  show papyrusImg delight
  papyrus "WE SHOULD ASK SOMEBODY TO HELP INTO CREATE A GIRL SKELETON!"
  show gaster trapped oh flip
  gaster "NO PAPYRUS, NO"
  papyrus "I KNOW!"
  papyrus "WE SHOULD ASK TORIEL!"
  gaster "WHAT?!"
  papyrus "MAYBE SHE CAN HELP US IN CREATE A LITTLE SISTER!"
  show gaster trapped angry flip
  gaster "PAPYRUS, PLEASE!"
  show gaster trapped sad flip
  gaster "1. ..."
  gaster "..."
  show gaster trapped maybe flip
  gaster "I HAD ALREADY EXPLAIN YOU THAT"
  show gaster trapped sad flip
  gaster "AND 2. IF TORIEL WERE TO CREATE A FEMALE SKELETON, SHE WOULD NOT BE YOUR 'LITTLE SISTER'"
  gaster "SHE WOULD BE YOUR AUNT"
  show papyrusImg nope
  show gaster trapped oh flip
  stop music
  pause(3.0)
  papyrus "I THINK YOU SHOULDN'T HAVE SAID THAT"
  gaster "I'M SURE NEITHER SANS OR THE KING KNOWS ABOUT IT"
  papyrus "THEN WE NEVER HAD THIS CONVERSATION"
  gaster "GOOD"
  play music "music/another him.MP3" fadein 1
  if sansPapyrusPast == 2:
    $ sansPapyrusPast = sansPapyrusPast + 1
  return
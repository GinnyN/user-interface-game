label fileAlphysTryAgain:
  show papyrusImg confused
  papyrus "WHAT WE'RE GOING TO DO WITH THIS PROGRAM?"
  show gaster trapped dissapointed flip
  gaster "SOMETHING IS WEIRD ABOUT THAT, BUT I'M NOT ENOUGH GOOD A CODER TO FIGURE OUT WHAT"
  show papyrusImg uhh
  papyrus "WHO'S THE BEST CODER YOU KNOW?"
  show gaster trapped happy flip
  gaster "YOU"
  show papyrusImg dissapointed
  papyrus "WE'RE DOOM"
  papyrus "WE'RE DOOMED, DOOMED, DOOOMED, DOOOOOOOOOMEEEDDDDDDD"
  show gaster trapped oh flip
  gaster "BUT YOU ARE"
  show papyrusImg confused
  papyrus "BUT I DON'T REMEMBER ANYTHING!"
  show papyrusImg dissapointed
  papyrus "I HAVE VAGUE RECOLECTIONS OF THEORY I GUESS"
  show papyrusImg confused
  papyrus "BUT THIS IS A MYSTERY TO ME!"
  show papyrusImg uhh
  papyrus "..."
  pause(2)
  gaster "PAPYRUS?"
  show papyrusImg explainingPointing
  papyrus "MAYBE IF I READ THE CODE I WILL UNDERSTAND IT"
  show papyrusImg delight
  papyrus "LIKE, EVERYTHING WOULD COME BACK TO MY BRAIN IF I SEE ACTUAL CODE"
  show gaster trapped dissapointed flip
  gaster "YOU MIGHT"
  gaster "BUT THAT DOESN'T MEAN THE CODE IS GOOD"
  show papyrusImg annoyed
  papyrus "IT WORKS"
  show gaster trapped sad flip
  gaster "I'M NOT TALKING ABOUT THAT"
  papyrus "HOW CAN I SAY THAT LOUDER?"
  show gaster trapped sorry flip
  gaster "PAPYRUS MY BOY..."
  gaster "THE CODE CAN BE THE BEST AND MOST EFFECTIVE CODE IN THE WHOLE KINGDOM, BUT..."
  show gaster trapped sad flip
  gaster "IF IT DOES NOT FOLLOW CERTAIN STANDARD FOR CLEAN CODE, IT'S GOING TO BE VERY DIFFICULT TO UNDERSTAND EVEN FOR SOMEONE AS GOOD AS YOU WERE"
  papyrus "YOU SAID DR ALPHYS IS REALLY TALENTED"
  show gaster trapped oh flip
  gaster "THIS HAS NOTHING TO DO WITH THAT"
  gaster "IF YOUR FRIEND HAS NEVER WORKED WITH SOMEONE ELSE BEFORE SHE PROBABLY DOES NOT HAVE A STANDARD"
  gaster "AND NOT EVEN THAT COULD ASSURE YOU WE COULD BE ABLE TO READ THE CODE"
  show papyrusImg uhh
  papyrus "ARE YOU SAYING THIS IS IMPOSSIBLE?"
  gaster "NO"
  show gaster trapped maybe flip
  gaster "JUST, DON'T EXPECT MUCH"
  papyrus "WHY NOT?"
  show gaster trapped sorry
  gaster "..."
  show gaster trapped maybe flip
  gaster "I JUST DON'T WANNA SEE YOUR DISSAPOINTED SAD FACE"
  show papyrusImg serious
  papyrus "THIS IS MY DISSAPOINTED ANGRY FACE"
  show gaster trapped oh flip
  gaster "..."
  if program2ndChance < 1:
      $ program2ndChance = program2ndChance + 1
return

label papyrusWantsToTry:
  show papyrusImg confused
  papyrus "BUT WHY I CAN'T DO IT?!"
  show gaster trapped dissapointed flip
  gaster "I DIDN'T SAY THAT"
  show papyrusImg serious
  papyrus "YOU * SAID * THAT!"
  show gaster trapped oh flip
  gaster "..."
  show gaster trapped maybe flip
  gaster "OK, I CANNOT PROVE THIS"
  show gaster trapped dissapointed flip
  gaster "BUT"
  show gaster trapped explain flip
  gaster "I THINK THERE'S A GOOD REASON WE'RE ALWAYS ON AUTOMATIC PILOT IN EVERY SINGLE RESET"
  show papyrusImg dissapointed
  papyrus "OH"
  papyrus "I KINDA SEE NOW"
  show gaster trapped oh flip
  gaster "IT DOESN'T SEEM TO ME WE ARE LEARNING THAT MUCH WITH ALL THOSE REPEATS"
  show papyrusImg annoyed
  papyrus "IT'S LIKE MY BRAIN KNOWS YESTERDAY WAS YESTERDAY"
  papyrus "AND JUST DO THE SAME ALL THE TIME"
  show gaster trapped sad flip
  gaster "THAT! THAT."
  gaster "EXACTLY"
  papyrus "UNLESS SOMETHING DRASTIC HAPPENS"
  show gaster trapped oh flip
  gaster "..."
  gaster "YES"
  show papyrusImg delight
  papyrus "AND IF I JUST REPEAT THIS AND STUDY A LOT?"
  gaster "I DON'T THINK IS GOING TO WORK"
  show papyrusImg annoyed
  papyrus "WHY?"
  gaster "..."
  show papyrusImg dissapointed
  papyrus "I ALWAYS FORGET WERE FRISK IS KEPT WHEN WE GO RESCUE THEM"
  gaster "EXACTLY"
  papyrus "AAAAAAHHHHHH"
  if program2ndChance < 2:
      $ program2ndChance = program2ndChance + 1
return

label changeOfPlans:
  show papyrusImg surprised happy
  papyrus "WHAT ABOUT IF I ASK HER?"
  show gaster trapped oh flip
  gaster "THE ROYAL SCIENTIST YOU SAID?"
  show gaster trapped dissapointed flip
  gaster "I MEAN, SHE DID IT IN A DIFFERENT VERSION OF THIS TIMELINE"
  show gaster trapped dissapointed
  gaster "MEANING SHE MIGHT KNOW WHAT SHE WROTE IN THE LAST TIMELINE"
  show gaster trapped dissapointed flip
  gaster "BUT AT THE SAME TIME READING CODE WHICH IS YOURS BUT NOT REMEMBER WHEN OR WHY YOU DID IT"
  show gaster trapped dissapointed
  gaster "OR EVEN IF SHE REMEMBERS ANYWAY FOR SOME REASON"
  show gaster trapped dissapointed flip
  gaster "DOES NOT GUARANTEE THAT SHE MIGHT KNOW WHAT TO DO"
  show gaster trapped dissapointed
  gaster "MY EXPERIENCE SEEING YOU AND SANS WORK ACTUALLY TELL ME THE OPPOSITE OF THAT"
  show papyrusImg delight
  papyrus "SO, YOU ARE SAYING WE SHOULD TRY!"
  show gaster trapped oh flip
  gaster "I DON'T THINK I SAID THAT"
  show papyrusImg explainingPointing
  papyrus "YOU ARE SAYING YOU DON'T KNOW"
  papyrus "SO?"
  show papyrusImg checkThis
  papyrus "WE SHOULD TRY!"
  papyrus "BECAUSE WE DON'T KNOW!"
  gaster "..."
  gaster "I..."
  show gaster trapped dissapointed flip
  gaster "I GUESS YOU CAN SAY THAT"
  show papyrusImg delight
  papyrus "YAAYYYYY"
  if program2ndChance < 3:
      $ program2ndChance = program2ndChance + 1
  $ tryWithAlphys = True
return

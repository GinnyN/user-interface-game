label fileAlphysTryAgain:
  show papyrusImg confused
  papyrus "WHAT WE'RE GOING TO DO WITH THIS PROGRAM?"
  gaster "SOMETHING IS WEIRD ABOUT THAT, BUT I'M NOT ENOUGH GOOD A CODER TO FIGURE OUT WHAT"
  show papyrusImg uhh
  papyrus "WHO'S THE BEST CODER YOU KNOW?"
  gaster "YOU"
  show papyrusImg dissapointed
  papyrus "WE'RE DOOM"
  papyrus "WE'RE DOOMED, DOOMED, DOOOMED, DOOOOOOOOOMEEEDDDDDDD"
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
  gaster "YOU MIGHT"
  gaster "BUT THAT DOESN'T MEAN THE CODE IS GOOD"
  show papyrusImg annoyed
  papyrus "IT WORKS"
  gaster "I'M NOT TALKING ABOUT THAT"
  papyrus "HOW CAN I SAY THAT LOUDER?"
  gaster "PAPYRUS MY BOY..."
  gaster "THE CODE CAN BE THE BEST AND MOST EFFECTIVE CODE IN THE WHOLE KINGDOM, BUT..."
  gaster "IF IT DOES NOT FOLLOW CERTAIN STANDARD FOR CLEAN CODE, IT'S GOING TO BE VERY DIFFICULT TO UNDERSTAND EVEN FOR SOMEONE AS GOOD AS YOU WERE"
  papyrus "YOU SAID DR ALPHYS IS REALLY TALENTED"
  gaster "THIS HAS NOTHING TO DO WITH THAT"
  gaster "IF YOUR FRIEND HAS NEVER WORKED WITH SOMEONE ELSE BEFORE SHE PROBABLY DOES NOT HAVE A STANDARD"
  gaster "AND NOT EVEN THAT COULD ASSURE YOU WE COULD BE ABLE TO READ THE CODE"
  show papyrusImg uhh
  papyrus "ARE YOU SAYING THIS IS IMPOSSIBLE?"
  gaster "NO"
  gaster "JUST, DON'T EXPECT MUCH"
  papyrus "WHY NOT?"
  gaster "..."
  gaster "I JUST DON'T WANNA SEE YOUR DISSAPOINTED SAD FACE"
  show papyrusImg serious
  papyrus "THIS IS MY DISSAPOINTED ANGRY FACE"
  gaster "..."
  if program2ndChance < 1:
      $ program2ndChance = program2ndChance + 1
return

label papyrusWantsToTry:
  papyrus "BUT WHY I CAN'T DO IT?!"
  gaster "I DIDN'T SAY THAT"
  papyrus "YOU * SAID * THAT!"
  gaster "..."
  gaster "OK, I CANNOT PROVE THIS"
  gaster "BUT"
  gaster "I THINK THERE'S A GOOD REASON WE'RE ALWAYS ON AUTOMATIC PILOT IN EVERY SINGLE RESET"
  papyrus "OH"
  papyrus "I KINDA SEE NOW"
  gaster "IT DOESN'T SEEM TO ME WE ARE LEARNING THAT MUCH WITH ALL THOSE REPEATS"
  papyrus "IT'S LIKE MY BRAIN KNOWS YESTERDAY WAS YESTERDAY"
  papyrus "AND JUST DO THE SAME ALL THE TIME"
  gaster "THAT! THAT."
  gaster "EXACTLY"
  papyrus "UNLESS SOMETHING DRASTIC HAPPENS"
  gaster "..."
  gaster "YES"
  papyrus "AND IF I JUST REPEAT THIS AND STUDY A LOT?"
  gaster "I DON'T THINK IS GOING TO WORK"
  papyrus "WHY?"
  gaster "..."
  papyrus "I ALWAYS FORGET WERE FRISK IS KEPT WHEN WE GO RESCUE THEM"
  gaster "EXACTLY"
  papyrus "AAAAAAHHHHHH"
  if program2ndChance < 2:
      $ program2ndChance = program2ndChance + 1
return

label changeOfPlans:
  papyrus "WHAT ABOUT IF I ASK HER?"
  gaster "THE ROYAL SCIENTIST YOU SAID?"
  gaster "I MEAN, SHE DID IT IN A DIFFERENT VERSION OF THIS TIMELINE"
  gaster "MEANING SHE MIGHT KNOW WHAT SHE WROTE IN THE LAST TIMELINE"
  gaster "BUT AT THE SAME TIME READING CODE WHICH IS YOURS BUT NOT REMEMBER WHEN OR WHY YOU DID IT"
  gaster "OR EVEN IF SHE REMEMBERS ANYWAY FOR SOME REASON"
  gaster "DOES NOT GUARANTEE THAT SHE MIGHT KNOW WHAT TO DO"
  gaster "MY EXPERIENCE SEEING YOU AND SANS WORK ACTUALLY TELL ME THE OPPOSITE OF THAT"
  papyrus "SO, YOU ARE SAYING WE SHOULD TRY!"
  gaster "I DON'T THINK I SAID THAT"
  papyrus "YOU ARE SAYING YOU DON'T KNOW"
  papyrus "SO?"
  papyrus "WE SHOULD TRY!"
  papyrus "BECAUSE WE DON'T KNOW!"
  gaster "..."
  gaster "I..."
  gaster "I GUESS YOU CAN SAY THAT"
  papyrus "YAAYYYYY"
  if program2ndChance < 3:
      $ program2ndChance = program2ndChance + 1
  $ tryWithAlphys = True
return

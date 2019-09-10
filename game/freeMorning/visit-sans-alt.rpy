label freeSansAlt:
  show papyrusImg coolDude thinking
  papyrus "I HAVE TO TRY GET HIM TO HELP US"
  show papyrusImg coolDude grandiose
  papyrus "I KNOW THIS IS USELESS, BUT I PROMISE THIS TO GASTER!"
  gaster "YES, YOU PROMISED THIS TO ME"
  show papyrusImg coolDude angry
  papyrus "SHUT UP!"
  papyrus "I'M TRYING TO MENTALIZE WHAT I HAVE TO DO!"
  if penAtAlphys:
      show papyrusImg coolDude realizing
      papyrus "WAIT"
      papyrus "DIDN'T I GIVE THE PENDRIVE TO ALPHYS ALREADY?"
      gaster "THAT'S ACTUALLY TRUE"
      show papyrusImg coolDude delight
      papyrus "THEN I DON'T HAVE TO TALK TO SANS ABOUT THIS!"
      show sansImg hoddie surprised flip at fade:
          xpos 0.5
      sans "are you ok?"
      play music "music/15 sans.mp3" fadein 1
      show papyrusImg coolDude scared
      papyrus "SANS!?"
      show papyrusImg coolDude uhh
      papyrus "SINCE "
      extend "WHEN YOU WERE HERE?"
      sans "..."
      sans "you know i can hear you from the stairs, right?"
      papyrus "..."
      papyrus "..."
      papyrus "..."
      papyrus "I HAVE TO GO TO THE BATHROOM"
      hide papyrusImg
      play sound "music/fx/steps.wav"
      show sansImg hoddie neutral flip
      sans "welp..."
      show sansImg hoddie content flip
      sans "he hopefully is ok..."
      stop music fadeout(1)
      scene black with dissolve
      sans "..."
      sans "why i have this feeling that he isn't?"
      scene forest with dissolve
      play music "music/15 sans.mp3" fadein(1)
      show papyrusImg coolDude explaining flip at fade:
          xpos 0.4
      papyrus "WHY AM I RUNNING AWAY FROM SANS THIS HAS NO SENSE!"
      show gaster trapped explain at fade:
          xpos 0.0
      gaster "DON'T WORRY, YOU AREN'T THE ONLY ONE WHO HAS RAN AWAY FROM HIM"
      show papyrusImg coolDude thinking flip
      papyrus "WHAT."
      papyrus "HAVE YOU?"
      gaster "OF COURSE"
      gaster "SEVERAL TIMES"
      gaster "I HAVE ALSO RAN AWAY FROM YOU, "
      extend "FIRE ELEMENTALS, "
      extend "MY CREATOR..."
      papyrus "I UNDERSTAND THE LAST TWO, BUT WHY SANS?"
      show gaster trapped dissapointed 
      gaster "WELL..."
      gaster "I DID A MISTAKE "
      extend "DURING "
      extend "THE PROCESS OF "
      extend "YOUR SPELL"
      gaster "AND INSTEAD OF YOU I END UP WITH A BUNCH OF GOAT LOOKING SKULLS?"
      papyrus "DID YOU CREATE THE BLASTERS BY MISTAKE WHILE TRYING TO CREATE ME?"
      show gaster trapped explain
      gaster "OH NO"
      gaster "I JUST REPURPOSED THE GOAT LOOKING SKULLS AS LASERS BEAMS"
      gaster "I HOPE YOU STILL HAVE YOURS"
      papyrus "YEAH, I BARELY USE IT THOUGH"
      gaster "IT MAKE SENSE, YOU ARE STRONG AFTER ALL"
      show papyrusImg coolDude uhh flip
      papyrus "I REALLY LIKED TO TALK WITH YOU"
      papyrus "ABOUT HOW WE RAN AWAY FROM OUR PROBLEMS"
      show gaster trapped proud
      gaster "BELIEVE ME MY DEAR PAPYRUS"
      gaster "YOU ARE NOT GOING TO MAKE AN HABIT OUT OF THIS"
      papyrus "BUT I HAVE TO GO"
      show gaster trapped neutral
      gaster "GOOD LUCK MY DEAR BOY"
      stop music fadeout(1.0)
      return
  else:
      call papyrusAskSans from _call_papyrusAskSans
return

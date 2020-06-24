label afterAfternoon:
  scene forest with dissolve
  play music "music/48 Alphys.mp3" fadein 1
  pause(1)
  if weddingFrom == 'frisk':
    show papyrusImg position zorder 1 at fade:
      xpos 0.4
  else:
    show papyrusImg position zorder 1 at fade:
      xpos 0.3
  call papyrusImgSurprisedFlip
  papyrus "WHAT WAS THAT?"
  show gaster trapped oh at fade:
    xpos -0.1
  gaster "WHAT WAS WHAT?"
  call papyrusImgUhhFlip
  papyrus "THEY WERE TALKING ABOUT... WEDDINGS?"
  gaster "UH? WHAT'S THAT?"
  call papyrusImgExplainingFlip
  papyrus "WEDDING"
  papyrus "A CEREMONY IN WHICH HUMANS GET MARRIED"
  gaster "THEY HAVE A CEREMONY FOR THAT?"
  call papyrusImgDelightFlip
  papyrus "YEAH"
  papyrus "I HAVE NEVER FOUND THE USEFULNESS BEHIND THAT BUT IT SEEMS SOMETHING FUN TO DO IF YOU CAN"
  show gaster trapped dissapointed
  gaster "IT SOUND LIKE THE WORST IDEA EVER"
  gaster "ESTABLISHING FAMILY UNITS IS HARD IN GENERAL, BUT THE HUMANS HAVE TO MADE IT HARDER"
  call papyrusImgNeutralFlip
  papyrus "YES, I HAVE SOME HUMAN FRIENDS IN THEIR INTERNET NOT LIKING THE IDEA EITHER"
  show gaster trapped angry
  gaster "DO YOU HAVE WHAT WITH HUMANS IN THEIR INTERNET?"
  call papyrusImgAngryFlip
  papyrus "BUT THEY SHOULD NOT KNOW ABOUT THE WEDDING!"
  show gaster trapped oh
  gaster "WHICH WEDDING?"
  papyrus "UNDYNE AND ALPHYS'! SHOULD BE A SECRET AND A SURPRISE!"
  gaster "TO WHOM?"
  papyrus "TO EVERYBODY! EVEN ME!"
  gaster "THEN HOW TO DO YOU KNOW?"
  call papyrusImgNeutralFlip
  papyrus "I PEAKED OVER UNDYNE DOING HER INVESTIGATION ABOUT WEDDINGS IN HER COMPUTER AND I ASKED HER"
  show gaster trapped dissapointed
  gaster "THAT ANSWER THAT QUESTION"
  call papyrusImgAngry
  papyrus "BUT WHY EVERYBODY ELSE KNOWS???"
  show gaster trapped maybe
  gaster "MAYBE BECAUSE YOU ARE YELLING ABOUT IT IN THE MIDDLE OF THE FOREST TO NOTHING?"
  call papyrusImgAngryFlip
  papyrus "IT'S THE FIRST TIME IN THIS LOOP I YELL YOU ABOUT IT!"
  papyrus "THAT DOESN'T COUNT!"
  show gaster trapped sorry
  gaster "PAPYRUS, MY BOY"
  gaster "SOMETHING SIMILAR MUST HAVE HAPPENED FOR YOUR FRIEND TO TELL THEM"
  gaster "I SUGGEST YOU STAY AWAY FROM THIS WHILE WE'RE WORKING ON SOLVING MY... "
  call papyrusImgWorriedFlip
  extend "PROBLEM"
  papyrus "YEAH..."
  papyrus "MAYBE"
  papyrus "TOMORROW MUST EVERYTHING COME BACK TO RELATIVE NORMALCY"
  papyrus "I GUESS"
  show gaster trapped dissapointed
  gaster "YOU GUESS?"
  papyrus "ALWAYS WHEN SOMEBODY SEND ME TO SLEEP, USUALLY EVERYTHING GET EXACTLY LIKE I SAID"
  gaster "..."
  show gaster trapped sad
  gaster "GO SLEEP"
  gaster "THIS IS NOT THAT IMPORTANT"
  call papyrusImgAngryFlip
  show gaster trapped oh
  papyrus "WHAT?!"
  hide papyrusImg
  play sound "music/fx/steps.wav"
  pause(1)
  papyrus "SUIT YOURSELF"
  stop music fadeout 2
  pause(3)
  gaster "..."
  pause(2)
  gaster "ARE WE GOING TO TALK?"
  papyrus "OH!"
return 

label afterMorning:
  $ resetFromQuestionMenu = True
  scene forest with dissolve
  play music "music/48 Alphys.mp3" fadein 1
  pause(1)
  show gaster trapped oh at fade:
    xpos -0.1
  gaster "PAPYRUS?"
  if weddingFrom == 'frisk':
    show papyrusImg position zorder 1 at fade:
      xpos 0.4
  else:
    show papyrusImg position zorder 1 at fade:
      xpos 0.3
  call papyrusImgSurprisedFlip
  papyrus "WHAT IS HAPPENING?!!"
  gaster "OH"
  show gaster trapped dissapointed
  gaster "I STILL DON'T GET IT"
  call papyrusImgExplainingFlip
  papyrus "IT'S THE WEDDING!"
  show gaster trapped oh
  gaster "WHAT'S THAT?"
  papyrus "THE HUMAN CEREMONY FOR GETTING MARRIED"
  gaster "WHY ARE YOU TALKING ABOUT THAT?"
  call papyrusImgAngryFlip
  papyrus "BECAUSE EVERYBODY SEEMS TO KNOW ABOUT THAT!"
  gaster "ABOUT WHAT?"
  papyrus "ABOUT THE WEDDING!"
  gaster "WHAT'S THAT?"
  papyrus "..."
  call papyrusImgAnnoyedFlip
  papyrus "I'M NOT GOING TO REPEAT MYSELF"
  show gaster trapped dissapointed
  gaster "I STILL DON'T SEE THE PROBLEM"
  gaster "YOUR FRIENDS ARE ALREADY LIVING TOGETHER, THEN THEY ARE MARRIED"
  gaster "I DON'T SEE THE RELEVANCE FOR THAT HUMAN THING"
  call papyrusImgAngryFlip
  papyrus "I'M NOT TALKING ABOUT THE RELEVANCE OF THE CEREMONY"
  papyrus "I'M TALKING ABOUT THE RELEVANCE OF EVERYBODY KNOWING ABOUT THAT WHEN IT SHOULD BE A SECRET!"
  show gaster trapped maybe
  gaster "WELL, I DON'T THINK YOUR FRIEND UNDYNE IS ABLE TO DO ANYTHING QUIETLY"
  papyrus "..."
  call papyrusImgWorriedFlip
  papyrus "YES..."
  call papyrusImgDelightFlip
  papyrus "BUT THAT'S PART OF WHY SHE'S AWESOME"
  show gaster trapped explain
  gaster "IF YOU HAVE SOME PROBLEMS WE COULD JUST RESTART THE WHOLE 3 DAYS"
  gaster "AFTER ALL, ALL THIS WEDDING STUFF HAS NOTHING OF VALUE FOR OUR MISSION"
  show gaster trapped neutral
  gaster "WE MIGHT RESTART THE LOOP ANYWAY"
  stop music fadeout 2
  pause(3)
  play music "music/46 Spear of Justice.mp3"
  call papyrusImgAngryFlip
  papyrus "WHAT ARE YOU TALKING ABOUT? WE NEED TO SOLVE THIS!"
  show gaster trapped angry
  gaster "THERE'S NOTHING TO SOLVE AND NOTHING THAT DESERVE ACTUAL INTERVENTION"
  hide papyrusImg
  play sound "music/fx/steps.wav"
  pause(1)
  show gaster trapped oh
  papyrus "I'M GOING!"
  stop music fadeout 4
  pause(3)
  gaster "..."
  pause(2)
  show gaster trapped dissapointed
  gaster "THIS IS A GOOD MOMENT TO REMIND MYSELF THAT YOU REALLY DON'T CHOOSE THE PERSONALITIES OF THE SKELETONS YOU CREATE"
  
return 

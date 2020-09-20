label monstersForest1:
  show papyrusImg uhh
  papyrus "I FOUND THE WEIRDEST, STIFFIEST MONSTERS IN THE FOREST WHEN WE WERE SEARCHING FOR BAD HUMANS"
  show papyrusImg confused
  papyrus "TURN OUT THEY WERE KIDNAPPING KIDS AS WELL!"
  show gaster trapped sad flip
  gaster "THEY MUST BE WEKUFES"
  show papyrusImg uhh
  papyrus "DO THEY LOOK LIKE REALLY STIFF MONSTERS?"
  show gaster trapped neutral flip
  gaster "THEY LOOK LIKE REALLY STIFF... THINGS"
  papyrus "HUH?"
  show gaster trapped dissapointed flip
  gaster "I'M DEEPLY SORRY, BUT I DON'T KNOW THAT MUCH ABOUT THEM"
  papyrus "I'M QUITE CONFUSED"
  show papyrusImg annoyed
  show gaster trapped oh flip
  papyrus "THE KID THEY WERE KIDNAPPING AND WE SAVED WAS, LIKE, 3 YEARS OLDER THAN FRISK"
  papyrus "AND FRISK IS REALLY STRONG!"
  papyrus "IF THOSE THINGS WERE MONSTERS AND ANY OF THE KIDS THEY KIDNAPPED REALIZED THAT"
  papyrus "BY THIS POINT ALL OF THEM WOULD BE DUST"
  gaster "MAYBE THEY ARE REALLY GOOD AT SCARING KIDS"
  gaster "OR..."
  show gaster trapped neutral flip
  gaster "THEY ARE NOT MONSTERS"
  show papyrusImg uhh
  papyrus "THEN ARE THEY A TYPE OF HUMAN?"
  gaster "..."
  show gaster trapped dissapointed flip
  gaster "I... DON'T... KNOW..."
  gaster "I DON'T KNOW THAT MUCH ABOUT HUMANS"
  show gaster trapped neutral flip
  gaster "MY FIRST ANSWER WOULD BE NO"
  gaster "BUT I MIGHT MISSING SOME MORE DETAILED INFORMATION"
  gaster "WE WILL NEED TO ASK AN EXPERT, BUT WHO AND HOW?"
  show papyrusImg delight
  papyrus "MAYBE I CAN JUST GO AND ASK THEM"
  gaster "..."
  show papyrusImg annoyed
  papyrus "WHAT?"
  show gaster trapped maybe flip
  gaster "I'M TRYING TO THINK WHY THAT IS A BAD IDEA"
  show papyrusImg delight
  papyrus "COME ON, IF SOMETHING WEIRD HAPPENS TO ME YOU CAN JUST RESET, RIGHT?"
  show gaster trapped sorry flip
  gaster "IT HURTS A LOT ANYWAY PAPYRUS, DO NOT FORCE ME TO DO THAT"
  show papyrusImg confused
  papyrus "BUT, WHAT ELSE I CAN DO"
  show papyrusImg neutral
  papyrus "GO FORWARD AND JUST ASK THEM IT CAN BE A GOOD IDEA AFTER ALL"
  papyrus "IF THEY ARE MONSTERS I CAN DEFEND MYSELF"
  gaster "AND IF THEY ARE HUMANS YOU WOULD BE DEAD"
  show papyrusImg delight
  papyrus "BUT YOU WILL RESET AND PROBLEM SOLVED"
  gaster "..."
  show gaster trapped oh flip
  gaster "YOU DON'T CARE ABOUT DYING"
  gaster "YOU WERE PLANNING SINCE THE BEGINNING TO GUILD TRIP THE HUMAN INTO RESETTING DURING THAT PLAYTHROUGH"
  show papyrusImg uhh
  papyrus "OH, SO THAT'S WHY YOU HATE FRISK"
  show papyrusImg neutral
  papyrus "GOOD I DON'T REMEMBER THAT"
  show gaster trapped dissapointed flip
  gaster "FINE, I'M GOING TO RESET IF SOMETHING GOES WRONG..."
  show papyrusImg delight
  papyrus "THANKS"
  if wekufeMeeting == 0:
    $ wekufeMeeting = 1

#  papyrus "I CAN ASK FRISK..."
#  gaster "YOU MIGHT, BUT BEEN A HUMAN DOESN'T MEAN YOU HAVE A DETAILED INFORMATION ABOUT THE HUMANS EXISTENCE"
#  gaster "AT LEAST NOT FROM A MONSTERS' PERSPECTIVE"
#  gaster "HUMANS BARELY HAVE MAGIC, SO THEY DON'T DO CLASSIFICATIONS OR STUDIES BASED ON THAT, WHICH FOR US IS ESENCIAL"
#  papyrus "WAIT"
#  papyrus "I KNOW 2 MONSTERS WHO KNOW EVERYTHING YOU NEED TO KNOW ABOUT HUMANS"
#  gaster "OH, YOU MEAN THE ROYAL SCIENTIST AND..."
#  gaster "NO, NO, NOOOOOOO"
#  papyrus "YES!"
#  papyrus "METTATON!"
  
return

label wekufeTheory:
  papyrus "I WONDER IF THEY WERE SAYING THE TRUTH"
  papyrus "HUMANS ARE REALLY STRONG AFTER ALL"
  gaster "IT'S NOT MY AREA"
  gaster "BUT IT SEEMS OUR FRIEND THERE WERE ESTABLISHING THE THEORY THAT HUMANS HAVE VERY STRONG PARTS BUT VERY WEAK WHOLE"
  if wekufeMeeting == 2:
    $ wekufeMeeting = 3
return
  
label mettatonSempai:
  papyrus "DO YOU THINK HE WOULD TALK TO ME?"
  gaster "WHO?"
  gaster "OH"
  gaster "HE'S JUST A GHOST, DON'T WORRY ABOUT IT"
  papyrus "HE'S NOT JUST A GHOST!"
  papyrus "HE'S AN IDOL FOR ALL MONSTERS!"
  gaster "I... "
  extend "CAN ADMIT HE HAS SCREEN PRESENCE"
  papyrus "IT'S MORE THAN SCREEN PRESENCE!"
  papyrus "HE HAS CHARISMA!"
  papyrus "HE HAS BEAUTIFUL EYES!"
  gaster "I CAN CONCEDE THAT AS WELL"
  gaster "BUT I DON'T SEE HOW HE'S ANY EXPERT ON HUMAN MATTERS!"
  papyrus "OH..."
  papyrus "ALPHYS AND HIM KNEW EACHOTHER FROM A HUMAN APPRECIATION CLUB"
  gaster "A HUMAN."
  gaster "APPRECIATION..."
  gaster "WAIT..."
  gaster "THAT'S WHY I DON'T LIKE HIM"
  gaster "HE'S NOT DOING ANYTHING NEW!"
  gaster "HE'S IMITATING HUMANS!"
  papyrus "WHAT?! NO..."
  papyrus "AND EVEN IF HE DOES, THERE'S NOT A SINGLE HUMAN ENTERTAINER AS COMPLETE AS HE IS!"
  gaster "HOW DO YOU KNOW THAT?"
  papyrus "I HAVE BEEN WATCHING MY FAIR SHARE OF HUMAN TV"
  papyrus "BUT THE ONLY OTHER THING I REALLY LIKE IS THAT SHOW OF THE HUMANS HELPING OTHER HUMANS GET DRESSED MORE FASHIONABLE"
  papyrus "I DON'T REMEMBER HOW IS CALLED BUT I NEED THOSE CLOTHES"
  gaster "STOP WATCHING PROPAGANDA"
  return

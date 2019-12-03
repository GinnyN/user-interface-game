label alphysAlt: 

  show papyrusImg coolDude realizing
  papyrus "OK"
  papyrus "I HOPE SHE'S NOT DOING SOMETHING IMPORTANT"
  papyrus "LET'S DO THIS"
  hide papyrusImg
  papyrus "{cps=*0.5}DR AAALLLLLLLLLLLLLLLLLLLLL{/cps}"
  scene black with dissolve
  extend "{cps=*0.5}PHHHYYYYYYYYYYYYYYYYYYYYYYYY{/cps}"
  scene undyneAlphysHouse inside with dissolve
  extend "{cps=*0.5}YYYYYSSSSSSSSSSSSSSSSSSSSSSS{/cps}"
  show papyrusImg coolDude me flip at fade:
      xpos 0.4
  show alphysImg casual noWords flip at fade:
      xpos -0.1
      ypos -0.2
  alphys "Ah!"
  show alphysImg casual nostalgic
  show papyrusImg coolDude delight flip
  play music "music/48 Alphys.mp3" fadein 1 fadeout 1
  alphys "Papyrus..."
  alphys "I'm sorry I'm such a mess..."
  alphys "It just..."
  show papyrusImg coolDude scared flip
  papyrus "WHAT HAPPENED?"
  show papyrusImg coolDude uhh flip
  alphys "I was watching the last episode of the new season of Mew Mew Kissy Cutie..."
  alphys "And..."
  papyrus "AND?"
  show alphysImg casual noWords
  alphys "IT BECAME GOOD"
  show papyrusImg coolDude scared flip
  papyrus "OH GOD!"
  show papyrusImg coolDude uhh flip
  alphys "IT WAS A REASON FOR EVERYTHING BETWEEN THE TWO SEASONS!"
  alphys "I CANNOT BELIEVE IT PAPYRUS!!!"
  papyrus "OK, SO YOU ARE BUSY NOW"
  show alphysImg casual nostalgic
  alphys "Ah...."
  hide papyrusImg
  papyrus "I'M GOING TO COME BACK IN AROUND 25 MINUTES TO TALK TO YOU"
  alphys "I already finished the episode..."
  alphys "So..."
  alphys "I think you can talk to me anything you need to talk to me???"
  papyrus "OH"
  show papyrusImg coolDude delight flip at fade:
      xpos 0.4
  papyrus "NEATO!"
  show papyrusImg coolDude uhh flip
  papyrus "DR ALPHYS"
  papyrus "IN THIS PENDRIVE THERE'S A BLUEPRINT FOR A MACHINE WHICH CAN ABSORB DETERMINATION"
  papyrus "IT'S NOT THE DT EXTRACTOR"
  show alphysImg casual mild confused
  alphys "Where..."
  show alphysImg casual nostalgic
  alphys "Where did you find this?"
  papyrus "I HAVE A FRIEND WHICH IS TRAPPED..."
  papyrus "..."
  alphys "Beyond the Darkness?"
  papyrus "YES YES, EXACTLY!"
  papyrus "AND NOW HE NEEDS HELP TO GET OUT"
  papyrus "I"
  extend "... I"
  extend "... I"
  extend "... I"
  extend "... I"
  papyrus "I NEED TO KNOW IF YOU CAN HELP US"
  alphys "This are just the blueprint?"
  papyrus "IT HAS MORE FILES, BUT I DO NOT UNDERSTAND VERY WELL WHAT THOSE FILES DO"
  alphys "I ca..."
  show alphysImg casual nostalgic flip
  alphys "..."
  show alphysImg casual dismissive
  alphys "It's going to be easy"
  show papyrusImg coolDude surprised happy flip
  papyrus "REALLY?"
  show alphysImg casual nostalgic
  alphys "Y... Yes.."
  papyrus "THANKS YOU DR ALPHYS!!"
  alphys "I'm..."
  alphys "I'm going to need some space..."
  show papyrusImg coolDude enough flip
  papyrus "TELL NO MORE"
  show papyrusImg coolDude delight flip
  papyrus "THANK YOU VERY MUCH!"
  hide papyrusImg
  alphys "..."
  stop music fadeout(3)
  pause(2)
  show alphysImg casual tired
  alphys "I'm sorry Papyrus"
  $ penAtAlphys = True
  if day > 2:
      $ alphysFailState = True
return

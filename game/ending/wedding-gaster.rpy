label weddingGaster:
  stop music fadeout(1)
  play music "music/81 An Ending.mp3" fadein(5)
  scene black with dissolve
  pause(2)
  frisk "..."
  frisk "Open the door up!"
  sans "..."
  scene skelebrosHouse inside floor2nd with dissolve
  show sansImg hoddie worried zorder 4 at fade with dissolve:
      xpos 0.0
  show friskImg worried flip zorder 5 at fade with dissolve:
      xpos 0.2
      ypos 0.15
  frisk "Sans!"
  show sansImg hoddie worried flip
  sans "frisk..."
  show sansImg hoddie worried
  sans "i already told toriel, i'm not going to the wedding"
  frisk "No, Sans..."
  sans "i'm going to be more of an asshole than i'm already are, i don't wanna ruin it"
  show friskImg explaining flip
  frisk "No Sans, it's not about that"
  show friskImg unsure flip
  frisk "Alphys wants to talk with you"
  frisk "About the ring"
  show sansImg hoddie surprised
  sans "which ring?"
  show alphysImg casual neutral flip zorder 3 at fade:
    xpos 0.45
    ypos -0.2
  alphys "The ring Undyne gave me for the wedding"
  show alphysImg casual explaining flip
  alphys "I asked her from where she got it"
  show alphysImg casual neutral flip
  alphys "And she said she didn't remember"
  alphys "I told that to Frisk and..."
  show friskImg happy flip
  frisk "It was Papyrus!"
  show sansImg hoddie angry
  sans "of course it was papyrus"
  sans "he probably half heard undyne about it and used his savings in human money to get it"
  show alphysImg casual angry flip
  alphys "You have savings in human money"
  sans "that doesn't matter..."
  frisk "There's still some Papyrus around!"
  frisk "I remember him, you remember him, the ring it here!"
  show sansImg hoddie neutral
  sans "that's good news"
  sans "because his room is completely empty"
  show friskImg unsure flip
  show alphysImg casual confused mild flip
  alphys "How that happened?"
  sans "for a moment i thought it was just the ripple effect from him somehow dissapearing from existence"
  sans "but if the ring is there..."
  sans "..."
  hide sansImg
  play sound "music/fx/steps.wav"
  scene black with dissolve
  pause(1)
  scene gasterWedding papyrusRoom with dissolve:
    xpos 0.0
    linear 10 xpos -0.2
  pause(3)
  scene skelebrosHouse inside floor2nd with dissolve
  play sound "music/fx/steps.wav"
  show sansImg hoddie worried zorder 4 at fade with dissolve:
    xpos 0.0
  show friskImg unsure flip zorder 5 at fade with dissolve:
    xpos 0.2
    ypos 0.15
  show alphysImg casual neutral flip zorder 3 at fade:
    xpos 0.45
    ypos -0.2
  frisk "???"
  sans "it's a letter"
  sans "i guess from the people who somehow stole everything from his room"
  show alphysImg casual dismissive flip
  alphys "Why do you assume that?"
  sans "this is not papyrus' handwritting"
  "..."
  text "MY DEAR SANS"
  sans "..."
  show sansImg hoddie surprised
  sans "gaster?"
  show alphysImg casual confused mild flip
  alphys "Is it from Dr. Gaster?"
  show friskImg surprised
  show alphysImg casual neutral flip
  alphys "He took the stuff that was supposed to be there?"
  show friskImg unsure
  frisk "How do you..."
  sans "..."
  show sansImg hoddie neutral
  sans "i guess i can tell you two"
  show friskImg happy flip
  show alphysImg casual confused mild flip
  frisk "Seriously?!"
  alphys "About what?"
  sans "but you have to promise me you are going to believe me"
  frisk "Of course!"
  show alphysImg casual tired flip
  alphys "..."
  show alphysImg casual angry flip
  alphys "Fine..."
  sans "well..."
  scene black with dissolve
  nvl clear
  narrator "THAT'S ALL I CAN SHOW YOU"
  narrator "REALLY! THERE'S NO MORE I CAN SHOW YOU"
  narrator "I HAD SOME DETERMINATION LEFT, BUT I JUST USED UP ALMOST EVERYTHING"
  narrator "..."
  narrator "I'M SORRY ABOUT THIS"
  narrator "BUT I DON'T KNOW HOW TO CONTINUE DIFFERENTLY!"
  narrator "I KNOW THEY WILL BE ALRIGHT"
  narrator "I'M JUST..."
  narrator "..."
  narrator "EVERYTHING IS GOING TO BE OK!"
  narrator "JUST HANG IN THERE!"
  narrator "I'LL BE... TOO..."
  nvl clear
  ""
  stop music fadeout(1)
  pause(1.5)
  # $ renpy.set_return_stack([])
  $ renpy.quit()
return
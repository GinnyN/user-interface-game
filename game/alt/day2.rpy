label altDay2:
  scene black with dissolve
  stop music
  pause(2)
  scene skelebroHouse outside with dissolve
  show papyrusImg coolDude happy zorder 0 at fade:
    xpos 0
  papyrus "I FEEL GREAT"
  papyrus "I DID MY RUN"
  papyrus "HIDE FROM UNDYNE WITH THE KIDS"
  papyrus "I NOW I HAVE FREE THE REST OF THE MORNING!"
  show papyrusImg coolDude thinking
  papyrus "WHAT SHOULD I DO?"
  call displayMenuFreeMorning from _call_displayMenuFreeMorning_2
  scene black with dissolve
  stop music
  pause(2)
  scene skelebroHouse outside with dissolve
  show papyrusImg coolDude surprised zorder 0 at fade:
    xpos 0
  gaster "DON'T YOU FEEL THIS STRUCTURE IS KIND OF ARTIFICIAL?"
  show papyrusImg coolDude offended
  papyrus "THIS IS HOW I STRUCTURE MY DAY USSUALLY, JUST STAY THERE"
  show papyrusImg coolDude thinking
  papyrus "WELL, WHAT SHALL I DO THIS AFTERNOON?"
  gaster "SEE? SEE?"
  show papyrusImg coolDude explaining
  papyrus "THIS IS HOW I DO IT, I NEED STRUCTURE!"
  gaster "..."
  show papyrusImg coolDude offended
  papyrus "I CANNOT BELIEVE I'M EXPLAINING THIS TO *YOU*"
  call displayMenuFreeAfternoon from _call_displayMenuFreeAfternoon_1
  call questionsEnd from _call_questionsEnd_3

label altDay3:
  scene black with dissolve
  stop music
  pause(2)
  scene skelebroHouse outside with dissolve
  show papyrusImg coolDude happy zorder 0 at fade:
    xpos 0
  papyrus "GREAT!"
  papyrus "I DID MY MORNING RUN"
  papyrus "I GIVE SOME PETS IN THE FOREST"
  papyrus "NOW..."
  show papyrusImg coolDude thinking
  papyrus "WHAT I SHOULD DO THIS MORNING?"
  call displayMenuFreeMorning from _call_displayMenuFreeMorning_3
  scene black with dissolve
  stop music
  pause(2)
  scene skelebroHouse outside with dissolve
  papyrus "DO YOU DO SOMETHING IN THE MORNINGS SINCE YOU ONLY TALK TO ME IN THE AFTERNOONS?"
  gaster "THAT'S NOT TRUE AND YOU KNOW THAT"
  papyrus "I'M PRETTY SURE YOU ARE NEVER THERE WHEN I DO MY MORNING ROUTINE"
  gaster "YOU DO STUFF BEFORE 10 A.M.?"
  papyrus "..."
  papyrus "OK, LET SEE WHAT CAN I DO THIS AFTERNOON"
  call displayMenuFreeAfternoon from _call_displayMenuFreeAfternoon_2
  call questionsEnd from _call_questionsEnd_4

  jump endingResolve
return

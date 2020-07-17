label weddingFinal:
  scene black with dissolve
  play music "music/33 Quiet Water.mp3" fadein 1 fadeout 1 
  pause(1)
  scene undyneAlphysHouse inside with dissolve
  if weddingFrom == 'frisk':
    show papyrusImg position zorder 1 at fade:
      xpos 0.4
  else:
    show papyrusImg position zorder 1 at fade:
      xpos 0.3
  call papyrusImgWorriedFlip
  papyrus "DR ALPHYS! DR ALPHYS!"
  show mettaton position zorder 2 at fade:
    ypos 0.2
  call mettatonSurprised
  metatton "Oh!"
  metatton "Papyrus, what are you doing here?"
  call papyrusImgSurprisedFlip
  papyrus "METTATON!!!"
  call papyrusImgSurprised
  papyrus "OH."
  extend " MY."
  extend " GOD."
  call papyrusImgDelight
  papyrus "HE KNOWS MY NAME!"
  call papyrusImgSerious
  papyrus "IT'S NOT TIME FOR FANBOYISM PAPYRUS, GET SERIOUS"
  call papyrusImgWorriedFlip
  papyrus "HAVE... YOU... .................... SEEN......"
  call mettatonQuestion
  metatton "Alphys?" 
  call mettatonThinking
  metatton "We have something to discuss before I start my tour"
  metatton "But she isn't here!"
  call mettatonCalamity
  metatton "OH! The Calamity"
  papyrus "SO... YOU HAVE NO IDEA?"
  call mettatonComplicit
  metatton "I have a theory where she might be"
  call papyrusImgAngryFlip
  papyrus "THEN LET'S GO!"
  hide papyrusImg
  play sound "music/fx/steps.wav"
  pause(1)
  call mettatonQuestion
  metatton "Did Frisk told me something about what to do on this cases?"
  play sound "music/fx/steps.wav"
  pause(1)
  if weddingFrom == 'frisk':
    show papyrusImg position zorder 1 at fade:
      xpos 0.4
  else:
    show papyrusImg position zorder 1 at fade:
      xpos 0.3
  call papyrusImgWorriedFlip
  papyrus "WHERE DO YOU THINK SHE IS?"
  call mettatonDelight
  metatton "Come with me"
  hide mettaton
  play sound "music/fx/steps.wav"
  pause(1)
  metatton "It's where Alphys always plans to have her wedding"
  call papyrusImgSurprised
  papyrus "HER WEDDING WHAT?"
  hide papyrusImg
  papyrus "NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO NO"
  scene black with dissolve
  stop music fadeout 1
  pause(1)
  scene elevator outside with dissolve:
    ypos -0.2
  play music "music/15 sans.mp3" fadein 1
  pause(1)
  show sansImg hoddie neutral flip at fade:
    xpos 0.6
    ypos 0.05
  sans "oh, that's a surprise right there"
  if weddingFrom == 'frisk':
    show papyrusImg position zorder 1 at fade:
      xpos 0.0
  else:
    show papyrusImg position zorder 1 at fade:
      xpos 0.1
  call papyrusImgAngry
  papyrus "SANS!!"
  papyrus "WHAT ARE YOU DOING HERE?!"
  show sansImg hoddie done flip
  sans "..."
  sans "this is where i work?"
  call papyrusImgSurprised
  papyrus "!!"
  call papyrusImgDesperate
  papyrus "I'M SORRY!"
  papyrus "I'M... JUST..."
  call papyrusImgWorried
  papyrus "SO NERVIOUS FOR SOME REASON"
  show sansImg hoddie neutral flip
  papyrus "I'M NOT THINKING STRAIGHT"
  gaster "THAT'S WHY I'M TELLING YOU NOT TO CONTINUE WITH THIS FOOLISHNESS"
  call papyrusImgAnnoyed
  papyrus "YOU SHUT UP!"
  hide papyrusImg
  play sound "music/fx/steps.wav"
  show sansImg hoddie neutral
  pause(1)
  show mettaton position zorder 2 at fade:
    ypos 0.2
  call mettatonQuestion
  metatton "I do not believe Frisk told me about that"
  show sansImg hoddie neutral flip
  sans "oh, that?"
  sans "that's quite weird"
  call mettatonDelight
  metatton "Ohhhhhhh..."
  call mettatonComplicit
  metatton "I need to spend more time with him"
  show sansImg hoddie neutral
  sans "i can arrange that"
  gaster "YOU WILL NOT ARRANGE ANYTHING..."
  gaster "..."
  gaster "RIGHT YOU CANNOT HEAR ME"
  scene black with dissolve
  stop music fadeout 1
  pause(2)
  play music "music/33 Quiet Water.mp3" fadein 1 fadeout 1 
  pause(1)
  if weddingFrom == 'frisk':
    scene alphysWatching battleArmor with dissolve:
      xpos -0.2
      linear 10 xpos 0.0
  else:
    scene alphysWatching coolDude with dissolve:
      xpos -0.2
      linear 10 xpos 0.0
  pause(5)
  scene elevator oceanview with dissolve:
    xpos -0.1
  pause(1)
  if weddingFrom == 'frisk':
    show papyrusImg position zorder 1 at fade:
      xpos 0.0
  else:
    show papyrusImg position zorder 1 at fade:
      xpos 0.0
  call papyrusImgCurious
  papyrus "WHOOOOOIEEEEEEE"
  papyrus "THE VIEW FROM HERE IS REALLY NICE!"
  show alphysImg casual nostalgic zorder 3 at fade:
    xpos 0.15
    ypos -0.2
  alphys "You can see the whole sea from here!"
  call papyrusImgUhh
  papyrus "..."
  show alphysImg casual neutral
  alphys "I still remember the first time we saw it..."
  alphys "I never thought that the water could be this blue and extend for so long"
  papyrus "..."
  show alphysImg casual nostalgic
  alphys "And... I will have my wedding here! I..."
  call papyrusImgSurprised
  papyrus "DO YOU KNOW ABOUT THE WEDDING RING?!"
  stop music
  pause(1)
  show alphysImg casual confused flip
  alphys "Wedding Ring?"
  call papyrusImgUhh
  papyrus "AHH..."
  alphys "!!!"
  show alphysImg casual confused mild flip
  alphys "Undyne brought me a wedding ring?"
  papyrus "NOOOOO......"
  call papyrusImgSurprised
  show alphysImg casual realizing
  play music "music/48 Alphys.mp3" fadein 1
  alphys "Undyne brought me a wedding ring!"
  scene elevator outside with dissolve:
    ypos -0.2
  pause(1)
  if weddingFrom == 'frisk':
    show papyrusImg position zorder 1 at fade:
      xpos 0.5
  else:
    show papyrusImg position zorder 1 at fade:
      xpos 0.4
  call papyrusImgWhy
  pause(4)
  show gaster trapped dissapointed at fade:
    xpos -0.1
  gaster "SHE DIDN'T KNEW"
  papyrus "..."
  gaster "YOU BLEW IT"
  papyrus "I BLEW IT!"
  gaster "YES, YOU DID THAT"
  call papyrusImgUhhFlip
  papyrus "AND NOW WHAT WE WILL DO!?"
  hide gaster
  show sansImg hoddie sideglance zorder 6 at fade:
    xpos 0.4
    ypos 0.05
  sans "uh..."
  show mettaton position zorder 2 at fade:
    ypos 0.2
  call mettatonDelight
  show sansImg hoddie neutral flip
  metatton "Call the only monster who can fix this of course!"
  papyrus "UH?"
  play sound "music/fx/telephone_ring.wav"
  "Phone" "ring! ring!"
  pause(5)
  play sound "music/fx/thump.wav"
  scene elevator outside with vpunch:
    ypos -0.2
  show undyneImg bored at fade:
    ypos -0.2
    xpos 0.0
  undyne "What just happened?"
  if weddingFrom == 'frisk':
    show papyrusImg position zorder 1 at fade:
      xpos 0.4
  else:
    show papyrusImg position zorder 1 at fade:
      xpos 0.3
  call papyrusImgDesperateFlip
  papyrus "I'M SORRY, I'M SOOOORRYYYY"
  hide papyrusImg
  show mettaton position zorder 2 at fade:
    ypos 0.2
    xpos 0.2
  call mettatonQuestionFlip
  metatton "How to say this..."
  metatton "Papyrus just... well..."
  call mettatonDelightFlip
  metatton "'Spoiled' Alphys with the surprise of the wedding"
  show undyneImg frustrated
  undyne "I still don't understand the order of all the things!"
  undyne "..."
  show undyneImg surprised
  undyne "Oh..."
  hide mettaton
  show undyneImg laugh
  undyne "You mean Papyrus just slipped about the ring"
  if weddingFrom == 'frisk':
    show papyrusImg position zorder 1 at fade:
      xpos 0.4
  else:
    show papyrusImg position zorder 1 at fade:
      xpos 0.3
  call papyrusImgDesperateFlip
  undyne "Papyrus! Don't do this to me!"
  papyrus "I'M SOOOOO SOOOOOOORRRRRRRRYYYYYYYY"
  show undyneImg happy
  undyne "Ok, fine"
  hide undyneImg
  undyne "I get it, I get it"
  call papyrusImgUhh
  papyrus "???"
  scene black with dissolve
  stop music fadeout 1
  pause(2)
  play music "music/34 Memory.mp3" fadein 1 fadeout 1 
  pause(2)
  scene elevator oceanview with dissolve:
    xpos -0.1
  show undyneImg worried zorder 2 at fade:
    ypos -0.2
    xpos -0.1
  show alphysImg casual nostalgic zorder 3 at fade:
    xpos 0.4
    ypos -0.2
  pause(2)
  undyne "Uh..."
  undyne "Alphys..."
  show alphysImg casual nostalgic flip
  alphys "Undyne?"
  undyne "Well..."
  undyne "I..."
  undyne "I...."
  show undyneImg bored
  undyne "...."
  show undyneImg angry flip
  undyne "WHAT DO YOU DO FIRST AGAIN?!"
  metatton "You knell in front of her a.."
  show undyneImg surprised flip
  undyne "Oh!"
  show undyneImg laugh
  undyne "Now I remember it!"
  show undyneImg neutral at fade:
    ypos 0.0
    xpos -0.1
  undyne "Will you"
  show undyneImg bored
  undyne "..."
  show undyneImg worried
  undyne "do this human marriage ceremony with me?"
  alphys "..."
  alphys "..."
  alphys "..."
  alphys "..."
  metatton "Now you say yes!"
  show alphysImg casual happy flip
  show undyneImg happy
  alphys "Yes! Yes! Of course!"
  scene black with dissolve
  stop music fadeout 4
  pause(5)
  scene elevator outside with dissolve:
    ypos -0.2
  if weddingFrom == 'frisk':
    show papyrusImg position zorder 1 at fade:
      xpos 0.4
  else:
    show papyrusImg position zorder 1 at fade:
      xpos 0.3
  pause(1)
  call papyrusImgDelight
  show sansImg hoddie neutral zorder 6 at fade:
    xpos 0.4
    ypos 0.05
  papyrus "AREN'T THEY ADORABLE?"
  sans "yes, yes they are"
  show mettaton position zorder 2 at fade:
    ypos 0.2
  call mettatonPresenting
  metatton "And we have to organize a wedding!"
  show lights at sparkles zorder 4
  play music "music/49 It's Showtime!.mp3"
  call mettatonDelight
  metatton "Isn't that exciting!?"
  call papyrusImgUhh
  papyrus "METTATON?"
  show sansImg hoddie neutral flip
  sans "right, right"
  sans "you must know a lot about weddings"
  call mettatonSurprised
  metatton "Of course!"
  metatton "Who do you think am I?"
  call papyrusImgSurprisedFlip
  papyrus "METTATON?"
  metatton "Exactly!"
  call mettatonDelight
  metatton "And here the 2 best men are going to help make it glorious!"
  papyrus "WHO?!"
  call mettatonSurprised
  metatton "You are Undyne's best friend!"
  papyrus "AM I?"
  call mettatonPresenting
  metatton "Exactly my dear!"
  metatton "I got your contact, I got my contact in your phone, and as soon I'm back from my 3 weeks Mini tour..."
  papyrus "AAAAAAAAHHHHHHHHHHHHHHHHHHH"
  hide papyrusImg
  play sound "music/fx/steps.wav"
  pause(1)
  stop music
  play sound "music/fx/glassbreak.wav"
  call mettatonSurprisedFlip
  pause(1)
  metatton "He jumped thru a window"
  sans "yes"
  call mettatonComplicit
  metatton "Outside with no windows"
  sans "yes"
  call mettatonCalamityFlip
  metatton "Oh my!"
  show sansImg hoddie content flip
  sans "i know he's too cool for words"
  scene forest with dissolve
  play music "music/33 Quiet Water.mp3" fadein 1
  pause(1)
  show gaster trapped dissapointed at fade:
    xpos -0.1
  gaster "ENOUGH FOOLISHNESS I SUPPOSE"
  if weddingFrom == 'frisk':
    show papyrusImg position zorder 1 at fade:
      xpos 0.4
  else:
    show papyrusImg position zorder 1 at fade:
      xpos 0.3
  call papyrusImgAnnoyedFlip
  papyrus "ARE YOU SAYING IF I HAD STOOD QUIET, NOTHING WOULD HAVE HAPPENED?"
  gaster "YES, I'M SAYING THAT"
  gaster "..."
  show gaster trapped maybe
  gaster "LOOK, I'M NOT GOOD AT TRYING, I DON'T KNOW WHEN TO TRY"
  call papyrusImgUhhFlip
  papyrus "BUT"
  papyrus "YOU * HAVE * TO TRY!"
  show gaster trapped oh
  gaster "BUT BY TRYING YOU MAKE IT WORSE"
  call papyrusImgExplainingFlip
  papyrus "I NEED TO LEARN WHEN, NOT!"
  extend" TO TRY!"
  show gaster trapped sad
  gaster "YOU NEED TO LEARN WHEN TO TRY"
  papyrus "WHEN, NOT!"
  extend " TO TRY!"
  pause(4)
  show gaster trapped dissapointed
  gaster "I THINK YOU CAN GO TO SLEEP NOW"
  stop music fadeout 1
  $ weddingEnding = True
return

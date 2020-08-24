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
  call papyrusImgWorriedFlip from _call_papyrusImgWorriedFlip_2
  papyrus "DR ALPHYS! DR ALPHYS!"
  show mettaton position zorder 2 at fade:
    ypos 0.2
  call mettatonSurprised from _call_mettatonSurprised
  metatton "Oh!"
  metatton "Papyrus, what are you doing here?"
  call papyrusImgSurprisedFlip from _call_papyrusImgSurprisedFlip_2
  papyrus "METTATON!!!"
  call papyrusImgSurprised from _call_papyrusImgSurprised_1
  papyrus "OH."
  extend " MY."
  extend " GOD."
  call papyrusImgDelight from _call_papyrusImgDelight_2
  papyrus "HE KNOWS MY NAME!"
  call papyrusImgSerious from _call_papyrusImgSerious
  papyrus "IT'S NOT TIME FOR FANBOYISM PAPYRUS, GET SERIOUS"
  call papyrusImgWorriedFlip from _call_papyrusImgWorriedFlip_3
  papyrus "HAVE... YOU... .................... SEEN......"
  call mettatonQuestion from _call_mettatonQuestion
  metatton "Alphys?" 
  call mettatonThinking from _call_mettatonThinking_1
  metatton "We have something to discuss before I start my tour"
  metatton "But she isn't here!"
  call mettatonCalamity from _call_mettatonCalamity
  metatton "OH! The Calamity"
  papyrus "SO... YOU HAVE NO IDEA?"
  call mettatonComplicit from _call_mettatonComplicit
  metatton "I have a theory where she might be"
  call papyrusImgAngryFlip from _call_papyrusImgAngryFlip_6
  papyrus "THEN LET'S GO!"
  hide papyrusImg
  play sound "music/fx/steps.wav"
  pause(1)
  call mettatonQuestion from _call_mettatonQuestion_1
  metatton "Did Frisk told me something about what to do on this cases?"
  play sound "music/fx/steps.wav"
  pause(1)
  if weddingFrom == 'frisk':
    show papyrusImg position zorder 1 at fade:
      xpos 0.4
  else:
    show papyrusImg position zorder 1 at fade:
      xpos 0.3
  call papyrusImgWorriedFlip from _call_papyrusImgWorriedFlip_4
  papyrus "WHERE DO YOU THINK SHE IS?"
  call mettatonDelight from _call_mettatonDelight_1
  metatton "Come with me"
  hide mettaton
  play sound "music/fx/steps.wav"
  pause(1)
  metatton "It's where Alphys always plans to have her wedding"
  call papyrusImgSurprised from _call_papyrusImgSurprised_2
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
  call papyrusImgAngry from _call_papyrusImgAngry_1
  papyrus "SANS!!"
  papyrus "WHAT ARE YOU DOING HERE?!"
  show sansImg hoddie done flip
  sans "..."
  sans "this is where i work?"
  call papyrusImgSurprised from _call_papyrusImgSurprised_3
  papyrus "!!"
  call papyrusImgDesperate from _call_papyrusImgDesperate
  papyrus "I'M SORRY!"
  papyrus "I'M... JUST..."
  call papyrusImgWorried from _call_papyrusImgWorried_1
  papyrus "SO NERVIOUS FOR SOME REASON"
  show sansImg hoddie neutral flip
  papyrus "I'M NOT THINKING STRAIGHT"
  gaster "THAT'S WHY I'M TELLING YOU NOT TO CONTINUE WITH THIS FOOLISHNESS"
  call papyrusImgAnnoyed from _call_papyrusImgAnnoyed_1
  papyrus "YOU SHUT UP!"
  hide papyrusImg
  play sound "music/fx/steps.wav"
  show sansImg hoddie neutral
  pause(1)
  show mettaton position zorder 2 at fade:
    ypos 0.2
  call mettatonQuestion from _call_mettatonQuestion_2
  metatton "I do not believe Frisk told me about that"
  show sansImg hoddie neutral flip
  sans "oh, that?"
  sans "that's quite weird"
  call mettatonDelight from _call_mettatonDelight_2
  metatton "Ohhhhhhh..."
  call mettatonComplicit from _call_mettatonComplicit_1
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
  call papyrusImgCurious from _call_papyrusImgCurious
  papyrus "WHOOOOOIEEEEEEE"
  papyrus "THE VIEW FROM HERE IS REALLY NICE!"
  show alphysImg casual nostalgic zorder 3 at fade:
    xpos 0.15
    ypos -0.2
  alphys "You can see the whole sea from here!"
  call papyrusImgUhh from _call_papyrusImgUhh_1
  papyrus "..."
  show alphysImg casual neutral
  alphys "I still remember the first time we saw it..."
  alphys "I never thought that the water could be this blue and extend for so long"
  papyrus "..."
  show alphysImg casual nostalgic
  alphys "And... I will have my wedding here! I..."
  call papyrusImgSurprised from _call_papyrusImgSurprised_4
  papyrus "DO YOU KNOW ABOUT THE WEDDING RING?!"
  stop music
  pause(1)
  show alphysImg casual confused flip
  alphys "Wedding Ring?"
  call papyrusImgUhh from _call_papyrusImgUhh_2
  papyrus "AHH..."
  alphys "!!!"
  show alphysImg casual confused mild flip
  alphys "Undyne brought me a wedding ring?"
  papyrus "NOOOOO......"
  call papyrusImgSurprised from _call_papyrusImgSurprised_5
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
  call papyrusImgWhy from _call_papyrusImgWhy
  pause(4)
  show gaster trapped dissapointed at fade:
    xpos -0.1
  gaster "SHE DIDN'T KNEW"
  papyrus "..."
  gaster "YOU BLEW IT"
  papyrus "I BLEW IT!"
  gaster "YES, YOU DID THAT"
  call papyrusImgUhhFlip from _call_papyrusImgUhhFlip_1
  papyrus "AND NOW WHAT WE WILL DO!?"
  hide gaster
  show sansImg hoddie sideglance zorder 6 at fade:
    xpos 0.4
    ypos 0.05
  sans "uh..."
  show mettaton position zorder 2 at fade:
    ypos 0.2
  call mettatonDelight from _call_mettatonDelight_3
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
  call papyrusImgDesperateFlip from _call_papyrusImgDesperateFlip
  papyrus "I'M SORRY, I'M SOOOORRYYYY"
  hide papyrusImg
  show mettaton position zorder 2 at fade:
    ypos 0.2
    xpos 0.2
  call mettatonQuestionFlip from _call_mettatonQuestionFlip
  metatton "How to say this..."
  metatton "Papyrus just... well..."
  call mettatonDelightFlip from _call_mettatonDelightFlip_1
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
  call papyrusImgDesperateFlip from _call_papyrusImgDesperateFlip_1
  undyne "Papyrus! Don't do this to me!"
  papyrus "I'M SOOOOO SOOOOOOORRRRRRRRYYYYYYYY"
  show undyneImg happy
  undyne "Ok, fine"
  hide undyneImg
  undyne "I get it, I get it"
  call papyrusImgUhh from _call_papyrusImgUhh_3
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
  call papyrusImgDelight from _call_papyrusImgDelight_3
  show sansImg hoddie neutral zorder 6 at fade:
    xpos 0.4
    ypos 0.05
  papyrus "AREN'T THEY ADORABLE?"
  sans "yes, yes they are"
  show mettaton position zorder 2 at fade:
    ypos 0.2
  call mettatonPresenting from _call_mettatonPresenting_5
  metatton "And we have to organize a wedding!"
  show lights at sparkles zorder 4
  play music "music/49 It's Showtime!.mp3"
  call mettatonDelight from _call_mettatonDelight_4
  metatton "Isn't that exciting!?"
  call papyrusImgUhh from _call_papyrusImgUhh_4
  papyrus "METTATON?"
  show sansImg hoddie neutral flip
  sans "right, right"
  sans "you must know a lot about weddings"
  call mettatonSurprised from _call_mettatonSurprised_1
  metatton "Of course!"
  metatton "Who do you think am I?"
  call papyrusImgSurprisedFlip from _call_papyrusImgSurprisedFlip_3
  papyrus "METTATON?"
  metatton "Exactly!"
  call mettatonDelight from _call_mettatonDelight_5
  metatton "And here the 2 best men are going to help make it glorious!"
  papyrus "WHO?!"
  call mettatonSurprised from _call_mettatonSurprised_2
  metatton "You are Undyne's best friend!"
  papyrus "AM I?"
  call mettatonPresenting from _call_mettatonPresenting_6
  metatton "Exactly my dear!"
  metatton "I got your contact, I got my contact in your phone, and as soon I'm back from my 3 weeks Mini tour..."
  papyrus "AAAAAAAAHHHHHHHHHHHHHHHHHHH"
  $ mettatonNumber = True
  hide papyrusImg
  play sound "music/fx/steps.wav"
  pause(1)
  stop music
  play sound "music/fx/glassbreak.wav"
  call mettatonSurprisedFlip from _call_mettatonSurprisedFlip_2
  pause(1)
  metatton "He jumped thru a window"
  sans "yes"
  call mettatonComplicit from _call_mettatonComplicit_2
  metatton "Outside with no windows"
  sans "yes"
  call mettatonCalamityFlip from _call_mettatonCalamityFlip
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
  call papyrusImgAnnoyedFlip from _call_papyrusImgAnnoyedFlip_1
  papyrus "ARE YOU SAYING IF I HAD STOOD QUIET, NOTHING WOULD HAVE HAPPENED?"
  gaster "YES, I'M SAYING THAT"
  gaster "..."
  show gaster trapped maybe
  gaster "LOOK, I'M NOT GOOD AT TRYING, I DON'T KNOW WHEN TO TRY"
  call papyrusImgUhhFlip from _call_papyrusImgUhhFlip_2
  papyrus "BUT"
  papyrus "YOU * HAVE * TO TRY!"
  show gaster trapped oh
  gaster "BUT BY TRYING YOU MAKE IT WORSE"
  call papyrusImgExplainingFlip from _call_papyrusImgExplainingFlip_2
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

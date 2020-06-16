label weddingTorielSans:
    if weddingFrom == 'sans':
        show papyrusImg coolDude thinking
        papyrus "I DON'T KNOW HOW BUT MY RESPONSIBLE BROTHER INSTINCT IS TELLING ME SANS IS NOT AT HIS POST"
        papyrus "I BETTER GO FIGURE OUT WHAT'S GOING ON"
        hide papyrusImg
        play sound "music/fx/steps.wav"
        pause(1)
        pause(2)
        play sound "music/fx/steps.wav"
        pause(1)
        show papyrusImg coolDude thinking flip zorder 0 at fade:
            xpos 0.4
        papyrus "BUT HE MAYBE HAS SOMETHING ELSE TO DO AND IT'S NOT LIKE HE HAS TO BE ALWAYS THERE..."
        papyrus "..."
        papyrus "BUT THIS ITCH..."
        papyrus "..."
        papyrus "I'D GO ANYWAY"
        hide papyrusImg
        gaster "BE NICE WITH YOUR BROTHER!"
        papyrus "I KNOW I KNOW"
    else:
        show papyrusImg coolDude thinking
        papyrus "MAYBE NOW I CAN ASK TORIEL A GOOD QUESTION"
        show papyrusImg coolDude careful
        papyrus "SINCE GASTER IS NOT GOING TO HEAR!"
        gaster "..."
        show papyrusImg coolDude uhh
        papyrus "WELL, SHE SHOULDN'T REMEMBER ANYTHING..."
        show papyrusImg coolDude enough
        papyrus "BUT I'M STILL NOT THAT CONVINCED"
        hide papyrusImg
        play sound "music/fx/steps.wav"
        pause(1)
        papyrus "MAYBE I CAN HELP HER JOG HER MEMORY!"
        gaster "..."
        gaster "HE TRULY BELIEVES I'M NOT THERE IF I'M NOT TALKING TO HIM"
        gaster "IT'S UNSETTLING" 
        extend " IN A WAY"
    play music "music/54 Hotel.mp3"
    scene muffetCafe with dissolve
    pause(1)
    show torielImg teacher neutral zorder 2 at fade:
        xpos 0.25
        ypos 0.2
    toriel "And..." 
    toriel "that happened"
    show sansImg hoddie worried flip at fade:
        xpos 0.6
        ypos 0.05
    sans "ok..."
    sans "and you need help in that because"
    show torielImg teacher worried
    toriel "I'm not very good at writing speeches"
    show sansImg hoddie neutral flip
    sans "i'm not going to even ask"
    show sansImg hoddie worried
    sans "so... ah..."
    show sansImg hoddie worried flip
    sans "it's there something... do you want to do..."
    show torielImg teacher unsure
    toriel "I don't know"
    toriel "I just prepared a list with..."
    show torielImg teacher worried
    toriel "suggestions..."
    show sansImg hoddie surprised flip
    sans "..."
    show sansImg hoddie neutral flip
    sans "we're totally doing this"
    show torielImg teacher neutral
    toriel "I'm glad"
    toriel "Now"
    if weddingFrom == 'sans':
        show papyrusImg coolDude offended zorder 0 at fade:
            xpos -0.2
        papyrus "I KNEW YOU WERE SLA..."
        papyrus "..."
        show papyrusImg coolDude scared
        papyrus "TORIEL?"
    else:
        show papyrusImg coolDude me zorder 0 at fade:
            xpos -0.2
        papyrus "TORIEL!"
        papyrus "AT THE SCHOOL THEY SAID YOU..."
        show papyrusImg coolDude scared
        papyrus "SANS?"
    show torielImg teacher neutral flip:
        xpos 0
    papyrus "I WASN'T INFORMED OF THIS"
    papyrus "..."
    show papyrusImg coolDude hangOn
    show sansImg hoddie done flip
    papyrus "I'M NOT SAYING THAT YOU HAVE TO TELL ME WHEN YOU HAVE A DATE"
    sans "..."
    sans "this is not a date"
    show papyrusImg coolDude angry
    papyrus "THIS IS THE TEXTBOOK DEFINITION OF A DATE, YOU CANNOT FOOL ME!"
    show papyrusImg coolDude annoyed
    papyrus "I READ THE MANUAL 10 TIMES BEFORE MY DATE WITH FRISK"
    show torielImg teacher unsure flip
    toriel "There's a manual?"
    toriel "..."
    show torielImg teacher neutral flip
    toriel "No, no, Sans is going to help me with some... writing I have to do"
    show papyrusImg coolDude thinking
    papyrus "IS THERE PUNS INVOLVED?"
    papyrus "..."
    sans "..."
    show papyrusImg coolDude annoyed
    papyrus "OF COURSE THERE PUNS INVOLVED"
    show sansImg hoddie content flip
    sans "oh papyrus, cod you know us?"
    show papyrusImg coolDude thinking
    papyrus "COD?"
    show torielImg teacher happy zorder 2 at fade:
        xpos 0.25
    toriel "That was *eely* bad"
    show sansImg hoddie sideglance
    sans "salmon had to say it"
    show papyrusImg coolDude careful
    papyrus "WHY THOSE ARE FISH PUNS?"
    show sansImg hoddie surprised flip
    sans "oh"
    show sansImg hoddie content flip
    sans "well, we fermi use some science puns as well"
    show torielImg teacher unsure
    toriel "You right!"
    show torielImg teacher happy
    toriel "I *newton* prepare for that!"
    papyrus "WHY THOSE ARE SCIENCE AND FISH PUNS?"
    show torielImg teacher unsure flip:
        xpos 0
    toriel "Uh?"
    show torielImg teacher worried flip
    toriel "You didn't knew?"
    show sansImg hoddie neutral flip
    sans "i'm pretty sure undyne already told him"
    show papyrusImg coolDude thinking
    papyrus "ABOUT WHAT?"
    show torielImg teacher neutral flip
    toriel "About the wedding"
    papyrus "WHICH WEDDING?"
    show torielImg teacher worried zorder 2 at fade:
        xpos 0.25
    toriel "He doesn't know about the wedding"
    show sansImg hoddie content flip
    sans "i knew about her intentions because of him, i'm sure he knows"
    show papyrusImg coolDude careful
    papyrus "WHAT ARE YOU TALKING ABOUT?"
    show torielImg teacher neutral flip:
        xpos 0
    toriel "Asgore called me because he has been  reading about humans' weddings and he told me he needed help with the official part of it"
    toriel "Because someone has to 'deliver the bride' it seems"
    papyrus "..."
    show papyrusImg coolDude thinking
    papyrus "WHA..."
    show papyrusImg coolDude scared
    papyrus "WHAT?!"
    toriel "For Undyne and Alphys' wedding of course"
    stop music
    papyrus "AH"
    papyrus "AHHH"
    papyrus "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
    hide papyrusImg
    play sound "music/fx/steps.wav"
    pause(1)
    play sound "music/fx/glassbreak.wav"
    show torielImg teacher surprised flip
    show sansImg hoddie neutral flip
    pause(1)
    toriel "He jumped tru the window"
    sans "he always does that"
    show torielImg teacher unsure flip
    toriel "Oh!"
    show torielImg teacher neutral zorder 2 at fade:
        xpos 0.25
    toriel "He has already mastered the art of the stylish exit"
    sans "yes"
    sans "he just has to do it not only when he's nervious"
    show torielImg teacher neutral flip:
        xpos 0
    toriel "He's cooler than you described"
    show sansImg hoddie content flip
    sans "i know words aren't enough"
return
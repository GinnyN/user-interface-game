label weddingFriskAsgore:
    if weddingFrom == 'frisk':
        show papyrusImg coolDude delight
        papyrus "I'M GOING TO VISIT FRISK!"
        papyrus "THE HUMAN HAD A DIFFICULT WEEK NOT MATTER HOW MUCH I TRIED NOT TO"
        gaster "LIKE I SAID, I CANNOT MANAGE TO WHERE I CAN JUMP BACK IN TIME"
        show papyrusImg coolDude neutral
        papyrus "I KNOW, I KNOW, RELAX"
        show papyrusImg coolDude checkThis
        papyrus "I JUST NEED TO UP MY GAME AS A SUPORTIVE FRIEND!"
        hide papyrusImg
        play sound "music/fx/steps.wav"
        pause(1)
        papyrus "HERE WE GOOOO"
        gaster "..."
        gaster "WHAT KIND OF GAME IS THAT?!"
    else: 
        show papyrusImg coolDude thinking
        papyrus "MAYBE I COULD ASK SOMETHING TO THE KING"
        gaster "REALLY?"
        gaster "LIKE WHAT?"
        show papyrusImg coolDude delight
        papyrus "WHAT DO YOU THINK?"
        gaster "I WAS ASSUMING YOU WERE TALKING ABOUT THAT"
        gaster "STILL, I DON'T THINK THIS IS GOING TO BE PRODUCTIVE"
        show papyrusImg coolDude enough
        papyrus "I KNOW YOU DON'T HAVE A HIGH OPINION OF THE KING"
        gaster "HE HAD STOPPED SOME OF MY EXPERIMENTS FOR MORAL CONCERNS MULTIPLE TIMES"
        gaster "WHAT DO YOU THINK I WOULD THINK ABOUT IT?"
        show papyrusImg coolDude thinking
        papyrus "MORAL CONCERNS?"
        gaster "..."
        show papyrusImg coolDude thinking
        gaster "I WOULD NOT TELL YOU WHERE THE KING IS"
        show papyrusImg coolDude happy
        papyrus "I'LL ASK MY INFORMANT THEN"
        hide papyrusImg
        papyrus "AND THE KING DOES NOT REMEMEBER ANYTHING SO WHY ARE YOU SCARED?"
        gaster "I'M NOT SCARED!"
    scene black with dissolve
    play music "music/05 Ruins.mp3" fadein 1 fadeout 1
    pause(1)
    scene toriel house with dissolve
    pause(0.5)
    show asgoreImg shirt serious flip zorder 1 at fade:
        xpos 0.3
        ypos -0.15
    asgore "You... you..."
    asgore "Has never gone to one of those?"
    show friskImg explaining zorder 3 at fade:
        xpos 0.0
        ypos 0.13
    frisk "No..."
    frisk "I'm too young for that..."
    show asgoreImg shirt embarrased flip
    asgore "I was hoping you could clarify me some... "
    extend "misconceptions I must have"
    show friskImg unsure
    frisk "I can help you with the internet"
    asgore "Oh..."
    show asgoreImg shirt happy flip
    asgore "That's actually a good idea"
    if weddingFrom == 'frisk':
        show papyrusImg me zorder 0 at fade:
            xpos -0.2
        papyrus "I HAVE ARRIVED!"
        show papyrusImg proud
        show friskImg happy flip at fade:
            xpos 0.1
        papyrus "IT'S ME!"
        papyrus "THE GREAT..."
        papyrus "!!"
        show papyrusImg surprised
        papyrus "YOUR MAJESTY!"
        papyrus "WHAT ARE YOU DOING HERE?!"
    else: 
        show papyrusImg coolDude me zorder 0 at fade:
            xpos -0.2
        papyrus "HEY!"
        papyrus "FRISK!"
        show papyrusImg coolDude delight
        show friskImg happy flip at fade:
            xpos 0.1
        papyrus "I'M SORRY IF I'M ASKING YOU..."
        show papyrusImg coolDude neutral
        papyrus "OH, YOUR MAJESTY"
    show asgoreImg shirt explaining flip
    asgore "Oh, howdy!"
    asgore "I'm here with Frisk because"
    asgore "I need to figure out some things and... well, I thought they could help me"
    call papyrusImgDelight
    papyrus "OHHHHHH"
    papyrus "WHAT'S THAT?"
    papyrus "MAYBE I CAN HELP FRISK HELP YOU ABOUT THAT PROBLEM"
    show asgoreImg shirt embarrased flip
    asgore "You sure?"
    call papyrusImgAnnoyed
    papyrus "YOUR MAJESTY PLEASE..."
    call papyrusImgDelight
    papyrus "MORAL SUPPORT IS ALSO HELP"
    show asgoreImg shirt happy flip
    asgore "Oh, you right!"
    asgore "Ok..."
    show asgoreImg shirt serious flip
    asgore "Ehem..."
    asgore "Do you know what 'deliver the bride' is?"
    papyrus "..."
    papyrus "............"
    call papyrusImgUhh
    show friskImg worried flip
    papyrus "YES?"
    asgore "You do?"
    show asgoreImg shirt happy flip
    asgore "That's great"
    asgore "Did you heard Frisk? He knows what that is!"
    show friskImg unsure flip
    frisk "I imagined that"
    show friskImg happy flip
    frisk "How many books do you have about it?"
    papyrus "AH..."
    papyrus "I FOUND SOME BOOKS ON THE HUMAN INTERNET ABOUT IT..."
    papyrus "I MADE A FRIEND ON A BOOKS STORE WHO SENT ME THE BOOKS FOR GOLD..."
    papyrus "I HAVE LIKE 10 COPIES IF SOMEONE NEED THEM..."
    show asgoreImg shirt explaining flip
    asgore "I'm going to need a copy"
    papyrus "..."
    asgore "Papyrus?"
    call papyrusImgWorried
    papyrus "I'M SORRY YOUR MAJESTY BUT..."
    papyrus "WHY DO YOU NEED TO KNOW ABOUT WEDDINGS?"
    show asgoreImg shirt embarrased flip
    asgore "Didn't Undyne told you?"
    show friskImg worried flip
    frisk "..."
    show asgoreImg shirt explaining flip
    asgore "It's for her wedding with Alphys!"
    call papyrusImgSurprised
    stop music
    papyrus "!"
    frisk "?"
    papyrus "AAAAAAAAAHHHHHHHHHHHHHHHHHHHHHH"
    hide papyrusImg
    play sound "music/fx/steps.wav"
    pause(1)
    play sound "music/fx/glassbreak.wav"
    show friskImg surprised flip
    show asgoreImg shirt happy flip
    pause(1)
    asgore "He... just... jumped out of the window?"
    show friskImg happy
    frisk "Yes, he does that sometimes..."
    asgore "He has already learnt the stylish exit"
    asgore "That's really impressive"
return

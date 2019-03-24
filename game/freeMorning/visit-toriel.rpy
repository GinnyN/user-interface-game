label torielSchool:
    play music "music/12 Home.mp3" fadein 1
    scene school outside with dissolve:
        ypos -0.3
    show torielImg teacher neutral flip zorder 2 at fade:
        xpos 0.4
    toriel "Papyrus!"
    show papyrusImg coolDude happy zorder 0 at fade:
        xpos 0
    papyrus "I CAME TO SEE IF YOU NEED HELP ON SOMETHING!"
    show torielImg teacher unsure flip
    toriel "I don't know if I have something for you today Papyrus"
    show torielImg teacher neutral
    toriel "The kids are running around the forest now"
    show torielImg teacher neutral flip
    toriel "Maybe you can help us with the parts of the laboratory"
    show papyrusImg coolDude thinking
    papyrus "FROM THE LAB?"
    papyrus "MAYBE YOU SHOULD CALL SANS INSTEAD"
    show papyrusImg coolDude happy
    papyrus "HE LOVES SCIENCE AFTER ALL!"
    show torielImg teacher happy flip
    toriel "It's just moving things around"
    show torielImg teacher neutral flip
    toriel "Alphys is sorting the aparatus right now"
    toriel "She needs some muscle"
    toriel "And Undyne is with the kids right now"
    show papyrusImg coolDude explaining
    papyrus "BUT I DON'T HAVE A MUSCLE"
    show torielImg teacher unsure flip
    toriel "..."
    toriel "Oh!"
    show torielImg teacher neutral flip
    toriel "Don't worry, your bones are going to be a perfect replacement"
    show papyrusImg coolDude surprised happy
    papyrus "REALLY?!"
    papyrus "THEN THE GREAT PAPYRUS IS GOING TO HELP"
    hide papyrusImg
    papyrus "DOOOOCCCCTOOOOOORRRRR ALLLLLLLPHHYYYYYYSSSSSS!!!!!!"
    show torielImg teacher worried flip
    toriel "I'll better go to check as well"
    hide torielImg

##School Basement
    scene school basement with dissolve
    show alphysImg casual confused mild flip zorder 3 at fade:
        xpos 0
        ypos -0.2
    alphys "Yet another of this papers"
    show alphysImg casual tired flip
    alphys "I know that giant goat head is a determination extractor"
    alphys "But why it was built in the first place..."
    show alphysImg casual confused mild flip
    alphys "Why I never made that question before?"
    show alphysImg casual realizing flip:
        xpos -0.2
    papyrus "DOCTOR ALPHYS!"
    show alphysImg casual nostalgic
    show papyrusImg coolDude delight flip zorder 0 at fade:
        xpos 0.1
    alphys "Papyrus!"
    alphys "We already did our training this week!"
    papyrus "TORIEL TOLD ME YOU NEED HELP WITH MOVING AROUND SOME MACHINES"
    show alphysImg casual confused mild
    alphys "Oh"
    show alphysImg casual confused mild flip
    alphys "That"
    show alphysImg casual confused mild
    alphys "THAT"
    show alphysImg casual confused mild flip
    alphys "Ok..."
    show alphysImg casual nostalgic
    show torielImg teacher neutral flip zorder 2 at fade:
        xpos 0.4
    toriel "What do you have there Alphys?"
    show alphysImg casual confused flip
    alphys "This?"
    show alphysImg casual dismissive
    alphys "It's nothing"
    alphys "It just some files with weird symbols"
    show papyrusImg coolDude thinking flip
    papyrus "WEIRD? DOESN'T LOOK WEIRD TO ME?"
    show alphysImg casual confused
    show torielImg teacher unsure flip
    alphys "What are you talking about, Papyrus?"
    papyrus "I... CAN... READ IT....???"
    alphys "What?"
    "Text" "{font=fonts/NewAster.ttf} TODAY I WAS SUPPOSED TO MAKE AN ANNOUNCEMENT TO THE KING. {/font}"
    "Text" "{font=fonts/NewAster.ttf} BUT MY ASSISTANT DECIDED IT WAS NOT ENOUGH EXCITEMENT. {/font}"
    papyrus "I WONDER ABOUT THEIR 'KIND' OF EXCITEMENT"
    alphys "You can read that?!"
    show papyrusImg coolDude explaining flip
    papyrus "IT'S JUST AN ACCENT"
    show torielImg teacher worried flip
    toriel "Like yours and Sans'?"
    show papyrusImg coolDude thinking 
    papyrus "I GUESS?"
    show alphysImg casual noWords
    alphys "I just this week I found tons and tons of papers with those symbols, everywhere!"
    show papyrusImg coolDude thinking flip
    alphys "And it's weird, because it's the first time I pay attention to them somehow"
    show torielImg teacher explaining flip
    toriel "Maybe you just forgot!"
    show alphysImg casual tired
    alphys "That's kind of the only solution I have..."
    alphys "But how I'm going to forget piles of papers with..."
    alphys "symbols..."
    show papyrusImg coolDude explaining flip
    papyrus "LETTERS ARE SYMBOLS"
    alphys "You know what I'm talking about"
    show papyrusImg coolDude thinking flip
    papyrus "I'M NOT??"
    show torielImg teacher neutral flip
    toriel "It's ok Alphys, you can sort this next week"
    toriel "Then we'll ask Papyrus and maybe Sans to help you out with those papers"
    show alphysImg casual tired
    alphys "I guess you right"
    show papyrusImg coolDude thinking
    hide torielImg
    hide alphysImg
    papyrus "MMMMMM..."
    "Text" "{font=fonts/NewAster.ttf} I DECIDED HE MIGHT FEEL ALONE. {/font}"
    "Text" "{font=fonts/NewAster.ttf} MAYBE, HE NEEDS COMPANY.{/font}"
    "Text" "{font=fonts/NewAster.ttf} I MIGHT MAKE HIM A BROTHER.{/font}"
    papyrus "?!"
    "Text" "{font=fonts/NewAster.ttf} I'LL ANALYSE THAT BETTER IN THE MORNING.{/font}"
    show papyrusImg coolDude enough
    papyrus "I THINK I JUST READ QUITE ENOUGH"
    if resets > 0 and not papersPapyrusCreation:
        show papyrusImg coolDude thinking
        papyrus "..."
        "Text" "{font=fonts/NewAster.ttf} I SPOKE TO SANS ABOUT THAT IDEA THIS MORNING.{/font}"
        show papyrusImg coolDude angry
        stop music
        papyrus "I KNEW IT"
        "Text" "{font=fonts/NewAster.ttf} HE SEEMS STOKED. I CAN HARDLY BLAME HIM.{/font}"
        "Text" "{font=fonts/NewAster.ttf} I DO NOT HAVE A BROTHER MYSELF, BUT I IMAGINE BEEN ALWAYS WITH AN OLD SKELETON LIKE ME SHOULD NOT BE SOMETHING A YOUNG SKELETON LIKE HIM MUST FIND EXCITING.{/font}" 
        "Text" "{font=fonts/NewAster.ttf} I ALSO ASKED IF HE HAD A GOOD NAME FOR HIM.{/font}"
        "Text" "{font=fonts/NewAster.ttf} HE TOOK ABOUT 2 SECONDS TO FLOOD ME WITH SUGGESTIONS.{/font}"
        "Text" "{font=fonts/NewAster.ttf} BUT I THINK WE GOT A GREAT ONE.{/font}"
        show papyrusImg coolDude thinking
        papyrus "..."
        papyrus "I NEED TO TALK ABOUT THIS WITH SANS"
        show papyrusImg coolDude explaining
        papyrus "BUT WHEN?"
        $ papersPapyrusCreation = True
    
return
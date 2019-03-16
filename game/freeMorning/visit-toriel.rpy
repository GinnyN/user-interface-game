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

    alphys "Yet another of this papers"
    alphys "I know that giant goat head is a determination extractor"
    alphys "But why it was built in the first place..."
    alphys "Why I never made that question before?"
    papyrus "DOCTOR ALPHYS!"
    alphys "Papyrus!"
    alphys "We already did our training this week!"
    papyrus "TORIEL TOLD ME YOU NEED HELP WITH MOVING AROUND SOME MACHINES"
    alphys "Oh"
    alphys "That"
    alphys "THAT"
    alphys "Ok..."
    toriel "What do you have there Alphys?"
    alphys "This?"
    alphys "It's nothing"
    alphys "It just some files with weird symbols"
    papyrus "WEIRD? DOESN'T LOOK WEIRD TO ME?"
    alphys "What are you talking about, Papyrus?"
    "Papyrus reads from the notes"
    papyrus "{font=fonts/NewAster.ttf} today i was supposed to make an annoucement to the king. {/font}"
    papyrus "{font=fonts/NewAster.ttf} but my assistant decided it was prank day or something. {/font}"
    papyrus "SOUNDS LIKE SANS TO ME, NYEHEHEH"
    alphys "You can read that?!"
    papyrus "IT'S JUST AN ACCENT"
    toriel "Like yours and Sans'?"
    papyrus "I GUESS?"
    alphys "I just this week I found tons and tons of papers with those symbols, everywhere!"
    alphys "And it's weird, because it's the first time I pay attention to them somehow"
    toriel "Maybe you just forgot!"
    alphys "That's kind of the only solution I have..."
    alphys "But how I'm going to forget piles of papers with..."
    alphys "symbols..."
    papyrus "LETTERS ARE SYMBOLS"
    alphys "You know what I'm talking about"
    papyrus "I'M NOT??"
    toriel "It's ok Alphys, you can sort this next week"
    toriel "Then we'll ask Papyrus and maybe Sans to help you out with those papers"
    alphys "I guess you right"
    "Toriel and Alphys leaves"
    papyrus "MMMMMM..."
    "Papyrus read the note again"
    papyrus "{font=fonts/NewAster.ttf} i decided that maybe he feels alone. {/font}"
    papyrus "{font=fonts/NewAster.ttf} maybe, he needs some company.{/font}"
    papyrus "{font=fonts/NewAster.ttf} i shall make him a brother, maybe.{/font}"
    papyrus "?!"
    papyrus "{font=fonts/NewAster.ttf} i'll analyse that in the morning.{/font}"
    papyrus "I THINK I JUST READ QUITE ENOUGH"

    if resets > 2 and not papersPapyrusCreation:
        papyrus "..."
        papyrus "{font=fonts/NewAster.ttf} i spoke to Sans about that idea this morning.{/font}"
        papyrus "I KNEW IT"
        papyrus "{font=fonts/NewAster.ttf} he seems stoked. i can hardly blame him.{/font}"
        papyrus "{font=fonts/NewAster.ttf} i never had a brother myself, and staying always with an old skeleton like me is not something a young lad must look forward everyday.{/font}" 
        papyrus "{font=fonts/NewAster.ttf} i also asked if he had a good name for him.{/font}"
        papyrus "{font=fonts/NewAster.ttf} he asks me why. i forgot i never told him.{/font}"
        papyrus "{font=fonts/NewAster.ttf} but after explain to him, i think he got a great name.{/font}"
        papyrus "..."
        papyrus "I NEED TO TALK ABOUT THIS WITH SANS"
        papyrus "BUT WHEN?"
        $ papersPapyrusCreation = True
    
return
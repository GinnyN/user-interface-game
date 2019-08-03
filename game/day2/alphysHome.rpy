label alphysHome:    
    scene undyneAlphysHouse inside with dissolve
    play music "music/33 Quiet Water.mp3" fadein 1 fadeout 1 
    show papyrusImg neutral zorder 0 at fade:
        xpos -0.2
    show alphysImg casual tired zorder 3 at fade:
        xpos 0.2
        ypos -0.2
    alphys "Thanks Papyrus"
    papyrus "IT'S OK, MY PLEASURE"
    alphys "I'm such a mess..."
    alphys "Undyne must be so embarrased..."
    show papyrusImg delight
    papyrus "SHE ACTUALLY LOVES WHEN YOU DO THIS"
    show papyrusImg neutral
    papyrus "BUT I THOUGHT YOU ALREADY KNEW THAT"
    show alphysImg casual tired flip
    alphys "Yes..."
    alphys "I just cannot believe it myself"
    papyrus "WE CAN ADD THAT 'UNDYNE LOVES ME FOR HOW I'M' TO OUR TRAINING EVERY WEDNESDAY AND FRIDAY"
    alphys "No, we'll not going to do that"
    papyrus "EVERYBODY BELIEVE YOU ARE AMAZING DR. ALPHYS"
    papyrus "IF YOU NEED SOMEONE TO REMIND YOU, APART OF UNDYNE, JUST GIVE A CALL"
    show alphysImg casual nostalgic flip
    alphys "Aw... Papyrus..."
    show alphysImg casual tired flip
    alphys "..."
    show alphysImg casual nostalgic flip
    alphys "Undyne is right, you are way too nice..."
    show papyrusImg uhh
    papyrus "?"
    papyrus "I JUST DO WHAT I THINK IS THE CORRECT THING TO DO"
    papyrus "THAT'S NOT BEEN NICE"
    show papyrusImg neutral
    papyrus "IT'S BEEN CONSEQUENT"
    alphys "Well..."
    show alphysImg casual tired flip
    alphys "..."
    alphys "..."
    show alphysImg casual nostalgic flip
    alphys "If you say so"
    if pen and tryWithAlphys and not program:
        $ penAtAlphys = True
        show papyrusImg neutral flip
        pause(1.0)
        show papyrusImg sorry
        papyrus "DR. ALPHYS, I KNOW YOU ARE BUSY"
        papyrus "BUT I HAVE A PROBLEM ONLY YOU CAN SOLVE"
        alphys "Me?"
        alphys "Me?"
        alphys "What do you mean?"
        show papyrusImg worried
        papyrus "I HAVE HERE THE BLUEPRINTS OF A DETERMINATION ABSORBING MACHINE"
        show alphysImg casual confused flip
        alphys "How you..."
        papyrus "I CANNOT TELL YOU THAT"
        papyrus "JUST..."
        papyrus "TRUST ME"
        show alphysImg casual nostalgic flip
        alphys "Ok..."
        papyrus "SOMEONE IS TRAPPED BEYOND..."
        papyrus "..."
        show alphysImg casual nostalgic
        alphys "Beyond..."
        show alphysImg casual nostalgic flip
        extend "the darkness?"
        show papyrusImg delight
        papyrus "YES!"
        show papyrusImg explainingPointing
        papyrus "IT BECAME ONE WITH EVERYTHING ONCE"
        papyrus "BUT WITH THIS MACHINE IS GETTING THEIR ORIGINAL FORM BACK"
        papyrus "BUT THE PROCESS IS NOT COMPLETE"
        show papyrusImg worried
        papyrus "CAN YOU SEE IF THERE'S A WAY TO COMPLETE THE PROCESS?"
        alphys "With just the bluprints?"
        papyrus "I DON'T HAVE MORE WITH ME, I'M..."
        alphys "..."
        show alphysImg casual nostalgic
        alphys "..."
        show alphysImg casual explaining flip
        alphys "It's going to be a piece of cake"
        show papyrusImg delight
        papyrus "THANKS!"
        show papyrusImg worried
        papyrus "JUST KEEP THE THING A SECRET, PLEASE"
        show alphysImg casual nostalgic flip
        alphys "Will do."

    show papyrusImg me
    papyrus "GOOD NIGHT DR ALPHYS"
    hide papyrusImg
    papyrus "DREAM OF TINY UNDYNES BEEN AWESOME"
    show alphysImg casual laugh
    alphys "PAPYRUS!"

    if pen and tryWithAlphys and not program:
        show alphysImg casual neutral
        pause(1)
        show alphysImg casual tired
        alphys "I'm sorry Papyrus"
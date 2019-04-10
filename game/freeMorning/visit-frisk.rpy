label visitFrisk:
    scene freeMorning frisk resetZero scene1 with dissolve:
        ypos -0.8
    pause(0.5)
    scene freeMorning frisk resetZero scene2 with dissolve:
        ypos -0.8
    pause(0.5)
    scene freeMorning frisk resetZero scene3 with dissolve:
        ypos -0.8
        linear 3 ypos 0.0
    papyrus "LOOK WHO'S THERE!"
    papyrus "IT'S THE GREAT PAPYRUS WHO'S VISITING YOU!"
    show friskImg happy zorder 3 at fade:
        xpos 0.0
        ypos 0.13
    frisk "smiles"
    show friskImg unsure
    frisk "i wanted to talk with you"
    show papyrusImg uhh flip:
        xpos 0.4
    papyrus "ABOUT WHAT?"
    frisk "it's a hunch i have"
    show papyrusImg serious flip
    papyrus "OH, THEN MUST BE IMPORTANT!"
    show friskImg explaining
    frisk "have you feel something is deciding for you things?"
    if resets < 1:
        show papyrusImg uhh flip
        papyrus "NO, NOT REALLY"
        show friskImg unsure
        frisk "..."
        show papyrusImg proud flip
        papyrus "DON'T FEEL BAD!"
        show papyrusImg delight flip
        papyrus "LET'S GO TO THE SPIDER BAKERY TO GET SOME POWER BRACELETS!"
        show friskImg happy
        frisk ".."
        show papyrusImg surprised flip
        papyrus "YES, RIGHT, I FORGOT"
        show papyrusImg proud flip
        papyrus "I'LL BRING THEM TO YOU THEN!"
        hide papyrusImg
        play sound "music/fx/steps.wav"
        frisk ".."
        show papyrusImg me flip:
            xpos 0.4
        papyrus "BACK!"
        show papyrusImg proud flip
        papyrus "TAKE SOME GREAT BRECELETS!"
        show friskImg explaining
        frisk "..."
        show papyrusImg surprised flip
        papyrus "THOSE CAME BACK?"
        show friskImg happy
        frisk "..."
        show papyrusImg surprised happy flip
        papyrus "THAT'RE REALLY COOL BRACELETS!"
        papyrus "..."
        frisk "..."
        hide papyrusImg
        hide friskImg
        papyrus "ISN'T IT WEIRD?"
        frisk "?!"
        papyrus "WE'RE ALL OUT"
        papyrus "I KNEW PEOPLE WHO LOST HOPE"
        papyrus "AND PEOPLE WHO DIED STILL HOPING"
        papyrus "BUT SOMEHOW, WE'RE OUT"
        papyrus "THANKS TO YOU"
        frisk "*pats Papyrus*"
        papyrus "I ONLY KNEW IF I HAD 1%% OF POWER ON GET IN US OUT, I WILL USE IT"
        papyrus "BUT I STILL DON'T KNOW IF I HAD SOMETHING TO DO ON THIS"
        frisk "??"
        papyrus "YEAH"
        papyrus "IT'S A WEIRD THING TO ASK"
        papyrus "SOMETIMES I FEEL POWERLESS OVER THINGS"
        papyrus "BUT AFTER THAT I FORGET ABOUT IT"
        papyrus "I DO WHAT I CAN, WITH THE AMOUNT OF POWER I HAVE"
        papyrus "I GUESS THAT'S THE IMPORTANT PART"
        frisk "..."
        frisk "sometimes, I feel i have none"
        papyrus "YES, ME TOO"
        papyrus "BUT NOT ALL THE TIME"
        frisk "now"
        papyrus "OH FRISK!"
        papyrus "YOU ARE MY FAVORITE HUMAN, ALWAYS REMEMBER THAT!"
        papyrus "AND CHOOSED THAT WITH MY OWN WILL!"
        "HUGS"
        
    return

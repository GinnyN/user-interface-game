label visitFrisk:
    scene freeMorning frisk resetZero scene1 with dissolve:
        ypos -0.8
    pause(0.5)
    play sound "music/fx/explosion.wav"
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
    play music "music/12 Home.mp3" fadein 1
    frisk "..."
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
    if resets < 4:
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
        hide papyrusImg
        hide friskImg
        papyrus "..."
        frisk "..."
        scene freeMorning frisk resetZero background with dissolve:
            ypos 0.0
            xpos -0.2
            linear 30 ypos -0.4 xpos 0.0
        show freeMorningF frisk resetZero foreground zorder 3 at fade:
            ypos 0.0
            xpos 0.0
            linear 30 ypos -0.1
        papyrus "ISN'T IT WEIRD?"
        frisk "?!"
        papyrus "WE'RE ALL OUT"
        papyrus "I KNEW PEOPLE WHO LOST HOPE"
        papyrus "AND PEOPLE WHO DIED STILL HOPING"
        papyrus "BUT SOMEHOW, WE'RE OUT"
        papyrus "THANKS TO YOU"
        frisk "pat* *pat"
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
        stop music
    else:
        papyrus "KIND.... OF...."
        papyrus "WHY ARE YOU ASKING ME THAT?"
        frisk "I..."
        frisk "..."
        frisk "A hunch maybe?"
        frisk "Flowey seems to know a lot about that..."
        papyrus "FLOWEY?"
        papyrus "DID YOU MEET HIM?"
        frisk "Do you..."
        frisk "Right, you don't..."
        papyrus "I MEAN, HE TOLD ME ABOUT A HUMAN HE WAS TALKING WITH..."
        papyrus "BUT I NEVER ASSUMED IT WAS YOU..."
        frisk "Why?"
        papyrus "HE DESCRIBED THEM DIFFERENTLY"
        frisk "..."
        papyrus "WHEN I MET YOU I TOLD HIM HE WAS WRONG, BUT ONCE HE TOLD ME THAT WASN'T WHAT HE WAS TALKING ABOUT"
        papyrus "I JUST ASSUMED HE WAS TALKING ABOUT ANOTHER HUMAN, BUT IN OUR SEARCHS FOR MONSTERS WHO MAYBE DIDN'T KNEW ABOUT THE BARRIER BREAKING WE CANNOT FIND THEM"
        papyrus "SO, I FIGURED, IT MIGHT BE SOMEONE ELSE"
        papyrus "LIKE, WHOEVER IS HELPING YOU TRAVELING IN TIME"
        frisk "You knew that?"
        papyrus "SANS KNEW"
        papyrus "AND DESPITE WHAT EVERYBODY BELIEVES, HE'S NOT THAT GOOD AT KEEPING SECRETS"
        papyrus "AND..."
        papyrus "WELL, THE FIRST TIME I SAW YOU I FELT IT WASN'T THE FIRST TIME"
        papyrus "AND I FELT SO HAPPY TO SEE YOU"
        papyrus "FOR SOME REASON"
        frisk "I cannot 'travel in time' now"
        papyrus "YOU CAN'T?"
        frisk "And who ever was doing that, I haven't heard them or feeling them in years"
        papyrus "WHAT DO YOU THINK IS GOING TO HAPPEN WHEN THEY COME BACK?"
        frisk "I hope they won't"
        frisk "They wasn't very nice"
        papyrus "AWWW..."
        papyrus "BUT I WANT TO KNOW MY FRIEND BETTER..."
        frisk "Friend?"
        papyrus "I MADE 2 FRIENDS AT ONCE, ISN'T THAT NEATO??"
        frisk "Papyrus..."
        papyrus "COME HERE!"
        papyrus "WE SKELETONS GIVE THE BEST HUGS!"
        frisk "Yes... yes you do..."
    return

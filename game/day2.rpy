label day2:
    #$ if day2:
    #    jump alternative

label schoolPapyrusRun:
    scene skelebroHouse outside with dissolve
    pause 0.5
    show studentImg dog gossiping flip zorder 3 at fade:
        xalign 0.7 yalign 1.0
    show kidImg listening zorder 0 at fade:
        xalign 0.3 yalign 1.0
    "Student" "* Did you heard that?"
    "Student" "* The teacher said we'll not meet with Papyrus today!"
    show studentImg dog sorry flip zorder 4 at fade
    show kidImg angry at fade
    monsterKid "No sense!"
    monsterKid "Papyrus never miss his morning run!"
    monsterKid "He's as cool as that!"
    show studentImg dog happy at fade
    show kidImg happy at fade
    show papyrusImg coolDude cocky flip zorder 2 at fade:
        xalign 0.9 yalign 1.0
    play music "music/16 Nyeh Heh Heh!.mp3" fadein(1)
    papyrus "HI KIDS!"
    papyrus "THE GREAT PAPYRUS HAS ARRIVED!"
    monsterKid "Papyrus!"
    papyrus "DON'T STOP MOVING!"
    papyrus "YOU DON'T WANNA ANGER YOUR TEACHER!"
    show undyneImg gym sarcastic at fade:
        xalign 0.2 yalign 1.0
    undyne "And what's Toriel told you!?"
    show papyrusImg coolDude surprised flip at fade
    show studentImg dog surprised flip at fade:
        xalign 0.8 yalign 1.0
    show kidImg scared flip at fade:
        xalign 0.6 yalign 1.0
    "* UNDYNE!"
    show studentImg dog scared flip
    show kidImg hiding flip
    show papyrusImg coolDude annoyed flip at fade
    show undyneImg gym bored at fade
    undyne "Move along kids, I need to talk with 'The Great Papyrus'"
    hide studentImg
    hide kidImg
    papyrus "I'M DOING WHAT TORIEL TOLD ME"
    undyne "You are keeping your rutine Papyrus"
    undyne "You need to rest!"
    show papyrusImg coolDude explaining flip at fade
    papyrus "BUT KEEPING WITH MY RUTINE IS RELAXING TO ME!"
    show undyneImg gym yelling at fade
    undyne "That's the opposite of a vacation Papyrus"
    show papyrusImg coolDude screaming flip at fade
    papyrus "BUT I DON'T TAKE VACATIONS!"
    show undyneImg gym frustrated at fade
    undyne "BUT NOW YOU SHOULD! AND IT'S TORIEL'S ADVICE!"
    show papyrusImg coolDude explaining flip at fade
    papyrus "BUT.."
    papyrus "I LIKE TO BE WITH THE KIDS"
    undyne "And I..."
    show undyneImg gym shy at fade
    undyne "..."
    show papyrusImg coolDude annoyed flip at fade
    papyrus "WHAT?!"
    stop music
    undyne "I don't want you to be with them"
    undyne "Not during this week at least"
    show papyrusImg coolDude speakless flip at fade
    papyrus "UNDYNE..."
    show undyneImg gym frustrated at fade
    undyne "Now, go to marathon Metaton's... "
    show undyneImg gym shy at fade
    extend "whatever is called now"
    show undyneImg gym frustrated at fade

    undyne "NOW GO!"
    hide undyneImg
    papyrus "..."
    hide papyrusImg

label grillsby:
    scene black with dissolve
    play sound "music/fx/steps.wav"
    pause(1.0)
    play music "music/15 sans.mp3" fadein 1
    pause(1.0)
    scene grillsbys inside with dissolve
    show grillsby neutral zorder 1 at fade:
        xalign 0.1 yalign 1.1 
    grillsby "..."
    show papyrusImg coolDude sorry flip zorder 0 at fade:
        xalign 1.0 yalign 1.2
    papyrus "YES, IT'S ME"
    grillsby "..."
    papyrus "NO IT'S NOT A MISTAKE"
    show papyrusImg coolDude sorry flip zorder 0 at fade:
        xpos 0.9 ypos 1.5
    papyrus "I FEEL AWFUL NOW"
    papyrus "UNDYNE THINKS I'M DANGEROUS"
    show papyrusImg coolDude grandiose flip at fade
    papyrus "AND SHOULDN'T BE! BECAUSE I'M THE GREAT PAPYRUS"
    show papyrusImg coolDude sorry flip at fade
    papyrus "Not anymore it seems..."
    grillsby "..."
    papyrus "GIVE ME THE KETCHUP BOTTLE"
    grillsby "?!"
    papyrus "JUST GIVE ME THE KETCHUP BOTTLE"
    grillsby "..."
    hide grillsby
    hide papyrusImg
    show grillsby neutral flip zorder 3 at fade:
        xpos 0.1 ypos 0.2
    show dogamy neutral flip zorder 2 at fade:
        xpos 0.3 ypos 0.25
    show dogaressa neutral flip zorder 1 at fade:
        xpos 0.5 ypos 0.25
    dogamy "What's happening?"
    grillsby "..."
    show dogamy surprised flip at fade
    show dogaressa surprised flip at fade
    dogamy "You say it's Papyrus?!"
    show dogamy worried at fade
    show dogaressa worried flip at fade
    dogaressa "He doesn't smell like him... weird..."
    grillsby "..."
    show dogamy surprised flip at fade
    show dogaressa surprised flip at fade
    dogamy "He's drinking the ketchup bottle?!"
    dogaressa "He can also do that?!"
    hide dogamy
    hide dogaressa
    hide grillsby
    stop music
    pause(0.1)
    scene grillsbys inside with vpunch
    play sound "music/fx/thump.wav"
    pause(1)
    show sansImg hoddie content flip at fade:
        xpos 0.6 ypos 0.205
    if torielKnows:
        sans "but how toriel did.."
    else:
        sans "time to..."
    show sansImg hoddie surprised flip at fade
    sans "papyrus?!"
    hide sansImg
    show grillsby neutral flip zorder 3 at fade:
        xpos 0.1 ypos 0.2
    show dogamy surprised  flip zorder 2 at fade:
        xpos 0.3 ypos 0.25
    show dogaressa worried flip zorder 1 at fade:
        xpos 0.5 ypos 0.25
    dogamy "The world is backwards today!"
    dogaressa "I think I'll need some ketchup myself"

label school:
    play music "music/12 Home.mp3" fadein 1
    scene school outside with dissolve:
        ypos -0.2
        linear 5 ypos -0.5
    pause(1.5)
    scene school gym with dissolve:
        xpos 0
        linear 5 xpos -0.1
    pause(0.8)
    show undyneImg gym happy at fade:
        xpos 0
    undyne "Today was a long one, those kids!"
    show undyneImg gym mildSurprise
    show sansImg hoddie angry flip at fade:
        xpos 0.6
    sans "i should say the same"
    show undyneImg gym yelling
    undyne "SANS?!"
    undyne "shouldn't you be at the elevator to High Snowdin?"
    sans "no... i was taking my break"
    show undyneImg gym bored
    undyne "Break... heh"
    sans "and i found my brother at grillsby"
    show undyneImg gym mildSurprise
    sans "drunk"
    undyne "that isn't a Papyrus thing"
    sans "exactly"
    show undyneImg gym frustrated
    undyne "Ok, ok, he feels bad for what happened yesterday, I get it, tough cookie"
    undyne "But what I have to do with anything now"
    show undyneImg gym mildSurprise
    sans "he was in the floor, sobbing, asking you for forgiveness"
    show undyneImg gym shy
    undyne "Oh"
    sans ".."
    undyne "I told him I didn't want him near to the kids today"
    show sansImg hoddie annoyed flip
    sans ".."
    undyne "He's just unstable after what happened yesterday and..."
    undyne "And even I have problems keeping cool with those kids"
    sans "that's explain it"
    show sansImg hoddie angry flip
    sans "but papyrus loves kids, you know that"
    undyne "I know, but..."
    sans "you don't feel ok with it"
    undyne "Despite I think those humans have it coming"
    show sansImg hoddie unsure flip
    sans "we need to find a way to solve this..."
    show undyneImg gym frustrated
    undyne "Before Papyrus does something REALLY crazy"
    undyne "like he's prone to do"
    play music "music/24 Bonetrousle.mp3" fadeout 1
    show undyneImg gym mildSurprise
    show sansImg hoddie surprised flip
    toriel "WHAT ARE YOU DOING!?"
    show sansImg hoddie surprised
    sans "toriel!"

#Outside School 
    "Sans and Undyne goes where Toriel and Frisk are looking up to Papyrus, jumping over the ceilings"
    undyne "I'll catch him up..."
    sans "let's me try that"
    undyne "?!"
    frisk "Sign of Ok"
    "Sans use a shortcut to appear in front of Papyrus"
    papyrus "SANS?"
    papyrus "IT'S THERE A SHORTCUT TO HERE?!"
    sans "what are you doing papyrus?"

label loop1:
    menu:
        "This is for keep my greatness!":
            jump honor
        "Stay away Sans! This is my problem!":
            jump stuborn
        "Sans! I have a Plan!":
            jump plan

label honor:
    papyrus "THIS IS FOR MY OWN GREATNESS SANS!"
    sans "you don't have anything to prove to undyne, really"
    papyrus "WHO SAID ANYTHING ABOUT HER?!"
    papyrus "THIS IS FOR ME!"
    papyrus "I NEED TO GO BACK TO BE AS GREAT AS I CAN BE!"
    sans "papyrus, please.."
    jump loop1

label stuborn:
    papyrus "DON'T GET IN THE WAY SANS!"
    papyrus "THIS IS *MY* PROBLEM!"
    sans "i understand the feeling"
    sans "but toriel told you, it's not anymore"
    papyrus "BUT IT'S STILL MY FAULT"
    papyrus "*I* HAVE TO SOLVE IT!"
    sans ".."
    jump loop1

label plan:
    papyrus "I HAVE A PLAN SANS!"
    sans "what kind of plan now..."
    papyrus "I'LL CAPTURE THE REST OF THOSE TERRIBLE HUMANS"
    papyrus "AND I'LL DELIVER THEM TO THE HUMANS' AUTHORITIES!"
    papyrus "I'LL BE A HERO"
    papyrus "AND THE GOOD HUMANS WILL CONSIDER US ALLIES INSTEAD OF ENEMIES!"
    sans "......"
    papyrus "SANS?"
    sans "that's actually a good idea"
    papyrus "OF COURSE IT IS"
    sans "but.."
    sans "but maybe it needs a bit more of.."
    sans "diplomacy"
    papyrus "???"
    sans "let's talk with toriel"

#label planning:
    toriel "It doesn't sound half bad"
    papyrus "OF COURSE IT'S NOT BAD, IT'S MY IDEA"
    toriel "But Sans it's right, we need to have some diplomacy added to the idea"
    papyrus "I DON'T DO WORDS. I DO ACTION"
    toriel "We know that my friend, I was thinking on doing it myself"
    papyrus "REALLY?"
    toriel "Of course"
    toriel "But I will need help"
    asgore "I'm sorry saying this but"
    papyrus "YOUR MAJESTY!"
    asgore "I would prefer help with capturing those people"
    asgore "Also, I have never been good with diplomacy"
    toriel "I sadly agree"
    undyne "Hey, and why don't you go with Sans"
    sans "hey"
    alphys "I think is appropiate"
    sans "don't"
    papyrus "THAT'S A GOOD IDEA"
    sans "do i not have a say on this?"
    papyrus "NO"
    toriel "Come on Papyrus, don't be like that with your brother"
    frisk "Signs of 'Sans did stand up at Metatton's Hotel'"
    papyrus "EXACTLY"
    toriel "Then is settled"
    sans "i really didn't have any say on this"
    toriel "I cannot go alone and you are the only one who can help me Sans"
    sans ".."
    sans "ok"
    toriel "Well then"
    toriel "Sans and I will go to talk with the humans authorities"
    asgore "We will ask for an audience in my behalf"
    toriel "We're going to ask for cooperation in the investigation of this human trafficking thing"
    toriel "They are doing it near to our lands for some reason and they kidnapped Frisk"
    toriel "So is our problem too"
    papyrus "AND WHAT'S GOING TO HAPPEN IF WE FIND THEM FIRST"
    undyne "That's a good question"
    undyne "I'll not sat here waiting for you to tell me to crush those bastards"
    sans "we will improvise"
    toriel "Well yes"
    toriel "We did improv once"
    asgore "I'm sorry Sans but..."
    asgore "Do you have something else to wear apart of that hoddie?"
    asgore "Something a bit more..."
    asgore "formal?"
    papyrus "NO, HE DOESN'T"
    sans "papyrus"
    alphys "Well... Metatton can help with that"
    sans "today is the backwards world"

label metattonsFashion:
    metatton "Welcome! Gentlemen and Gentlebeauties"
    metatton "To today's Metatton's Fashion Emergency!"
    sans "just do this thing quickly"
    metatton "My oh My, our subject today has a temper"
    papyrus "BUT HE DOESN'T HAVE AN OPTION"
    metatton "Those are my favorite subjects!"
    metatton "Let's see for what you have to dress for!"
    toriel "Ah... ap..."
    toriel "We just need a formal suit for an official meeting"
    metatton "But with GLAMOUR and PIZZAZ"
    toriel "ehh.. No"
    toriel "Just formal"
    metatton "..."
    metatton "I still can do something with that"
    metatton "Well Darlings, let's present the first of all options!"
    $ alphysHot = 0
    $ undyneThere = True

label loopSuit:
    menu:
        "Bonestrousle":
            jump bonestrousleSuit
        "Megalovania":
            jump megalovaniaSuit
        "Spears of Justice":
            jump spearsSuit

label bonestrousleSuit:
    metatton "This is a great design by our greatest designer"
    metatton "Combines a stylish white suit and a soft orange shirt with a wonderful red scarf"
    metatton "Wonderful for feel confident in anything you do"
    metatton "Even if you are terrible at it!"
    sans ".."
    sans "it doesn't feel half bad"
    metatton "Let's see what the public is thinking!"
    $ suit = 1
    jump publicAsk

label megalovaniaSuit:
    metatton "This is a wonderful design by our greatest designer"
    metatton "It has an elegant blue suit with a silked black shirt"
    metatton "Excelent for keep your promises"
    metatton "Until the very last moment!"
    sans ".."
    sans "why does it have this thing on the shirt?"
    sans "otherwise..."
    metatton "Let's see what the public is atching to say!"
    $ suit = 2
    jump publicAsk

label spearsSuit:
    metatton "This is a incredible design by our greatest designer"
    metatton "It has a wonderful green combination of suit and shirt"
    metatton "So you feel strong"
    metatton "And make everybody dreams true!"
    sans "what's this thing?!"
    metatton "Let's see what the public want to tell us!"
    $ suit = 3
    jump publicAsk

label publicAsk:
    menu:
        "Ask Asgore":
            if suit == 1:
                asgore "It look very well on him"
                asgore "That shirt has a nice color"
                asgore "Goes very well with his bones' color"
            elif suit == 2:
                asgore "The dark color suits him"
                asgore "And that shirt..."
                asgore "Goes very well with his eyes"
            elif suit == 3:
                asgore "The Green combination is very pleasant"
                asgore "That shirt combines very well"
                asgore "It has a good fit"
            $ alphysHot = 0
        "Ask Papyrus":
            if suit == 1:
                papyrus "METATTON IS SOOOO BISHONEN AND SEXY I'LL DIE!!"
                papyrus "I MEAN"
                papyrus "YOU LOOK GREAT SANS!"
                toriel "Yes Papyrus"
                toriel "Keep Supporting him"
                sans "somebody forgot i'm here against my will"
                papyrus "BUT I'M STILL SUPPORTING YOU!"
            elif suit == 2:
                papyrus "OHHH I CAN'T BELIEVE I'M SO CLOSE TO MY SEXY RECTANGLE IN HIS OWN SHOW!!!"
                papyrus "OH!"
                papyrus "IT REALLY SUITS YOU SANS!"
                sans "papyrus don't"
                papyrus "WHAT?!"
                papyrus "I REALLY MEAN IT!"
            elif suit == 3:
                papyrus "I'M SO CLOSE I CAN SEE HIS BISHONEN EYES..."
                papyrus "OH ME!"
                papyrus "IT HAS A GOOD FIT ON YOU SANS!"
                toriel "I must agree"
                papyrus "KEEP SUPPORTING SANS!"
                sans "why?"
                sans "why?!"
            $ alphysHot = 0
        "Ask Toriel":
            if suit == 1:
                toriel "I think he looks very s..."
                toriel "mmm"
                toriel "Confident in it"
                papyrus "TORIEL APROVES SANS!"
            elif suit == 2:
                toriel "I think he looks very s..."
                toriel "mmm"
                toriel "Dreamy in it"
                toriel "!?"
                frisk "smiles"
                asgore "frowns"
                papyrus "TORIEL *DEFINITELY* APROVES SANS!"
            elif suit == 3:
                toriel "I think he looks very p..."
                toriel "mmm"
                toriel "comfortable in it"
                papyrus "I DON'T KNOW WHAT SHE REALLY WAS GOING TO SAY BUT SHE APPROVES!"
            $ alphysHot = 0
        "Ask Undyne":
            if suit == 1:
                undyne "I don't know anything about 'style'"
                undyne "But I heard that white make you look fat!"
                undyne "And you are already fat!"
                undyne "Imagine yourself even fatter!"
            elif suit == 2:
                undyne "That opening is for your 'hair chest'"
                undyne "Just imagine everybody thinking what are you thinking wearing something for that!"
                undyne "Yes! It's funny!"
            elif suit == 3:
                undyne "That tie is from those weird monster horse riding movies!"
                undyne "You need to make the accent~!"
                undyne "HIIII YAAAAAAA!"
            $ alphysHot = 0
        "Ask Alphys":
            if alphysHot == 0:
                alphys "(Why am I feeling so turn on right now?)"
                $ alphysHot = alphysHot + 1
            elif alphysHot == 1:
                alphys "(He's just a gross fat skeleton)"
                alphys "(Who's also very smart)"
                $ alphysHot = alphysHot + 1
            else:
                alphys "(OH NO, I forgot I always get turn on by people on suits)"
                alphys "(Everybody look always so great on suits)"
                metatton "Mmm..."
                metatton "Darlings, I am noticing a disturbance in the force..."
                undyne "Oh wait"
                undyne "I know!"
                undyne "Hey! Metatton! Can we?!"
                metatton "Oh, Please! Be my guest!"
                undyne "Let's go Papyrus"
                papyrus "TO WHAT?!"
                jump alphysTeasing
        "Ask Frisk":
            if suit == 1:
                frisk "Questioning Expression"
                toriel "Do you think?"
                toriel "mmm...."
            elif suit == 2:
                frisk "Aproving Expression"
                papyrus "ONE VOTE FOR THE BLUE ONE!"
            elif suit == 3:
                frisk "Desaproving expression"
                undyne "Come on Frisk!"
                undyne "Help me out on this!"
            $ alphysHot = 0

    metatton "Are we ready to make a decision?"

    menu:
        "Yes":
            metatton "Let's see which one is the winner!"
            jump suitDecision
        "No":
            metatton "Let's see other suits then!"
            jump loopSuit

label alphysTeasing:
    "Papyrus and Undyne appear dressed with suits too"
    papyrus "THIS IS A GOOD SUIT INDEED"
    undyne "What do you think Alphys?"
    alphys "..."
    alphys "..."
    alphys "..."
    alphys "..."
    toriel "I'll take Frisk out of here"
    undyne "I just love when Alphys get so passionate about something..."
    "Alphys pass out"
    undyne "ALPHYS"
    metatton "Oh no"
    metatton "Her levels of "
    extend "'passion' were too high!"

    menu:
        "Undyne takes her back home":
            jump undyneLab
        "Papyrus takes her back home":
            jump papyrusLab

label undyneLab:
    undyne "I'll better take her back home!"
    metatton "Take the suit as well"
    undyne "?!"
    metatton "But don't tell her it was my idea"
    "Undyne gives a knowing look. Then retires."
    metatton "Well, we better jump to the decision then!"
    $ undyneThere = False

label suitDecision:
    menu:
        "Bonestrousle":
            $ sansSuit = 1
        "Megalovania":
            $ sansSuit = 2
        "Spears of Justice":
            $ sansSuit = 3

    metatton "Excelent choice!"
    metatton "You look marvelous!"
    papyrus "THIS WAS AMAZING!"
    if undyneThere:
        undyne "And wholefully innecesary"
        papyrus "BUT SANS LOOK VERY COOL!"
    else:
        sans "And kind of tacky"
        papyrus "BUT YOU LOOK VERY COOL SANS!"
    toriel "And you have a new suit which we needed"
    sans "the things i do for my brother"
    papyrus "AHHH..."
    papyrus "YOU ARE ADORABLE"
    sans "don't tell me that"
    asgore "Ahhh..."
    asgore "Brotherly love"
    metatton "I think I need to go and hug Nastablook right now"

    "Asgore talks with Papyrus and Undyne (If she's there)"

    asgore "Tomorrow we will start searching in the woods"
    asgore "Hopefully we're going to end this problem this week"
    if undyneThere:
        "* YES SIR!"
    else:
        papyrus "YES SIR!"
        asgore "Papyrus, please tell Undyne about this tomorrow, ok?"
        papyrus "YES SIR"

    jump day3

label papyrusLab:
    $ sansSuit = 2
    papyrus "I'LL TAKE HER BACK HOME"
    undyne "Papyrus please"
    papyrus "SHE MUST BE OVERWHELMED WITH SO MUCH COOLNESS IN SUITS"
    papyrus "AND, EVEN IF I'M THE COOLEST, SHE DOESN'T HAVE A CRUSH ON ME"
    undyne "Ngaaa..."
    undyne "Ok"

label alphysHome:
    "Papyrus get Alphys home"
    alphys "Thanks Papyrus"
    papyrus "IT'S OK, MY PLEASURE"
    alphys "I'm such a mess..."
    alphys "Undyne must be so embarrased..."
    papyrus "SHE ACTUALLY LOVES WHEN YOU DO THIS"
    papyrus "BUT I THOUGHT YOU ALREADY KNEW THAT"
    alphys "Yes..."
    alphys "I just cannot believe it myself"
    papyrus "WE CAN ADD THAT 'UNDYNE LOVES ME FOR HOW I'M' TO OUR TRAINING EVERY WEDNESDAY AND FRIDAY"
    alphys "No, we'll not going to do that"
    papyrus "EVERYBODY BELIEVE YOU ARE AMAZING DR. ALPHYS"
    papyrus "IF YOU NEED SOMEONE TO REMIND YOU, APART OF UNDYNE, JUST GIVE A CALL"
    alphys "Aw... Papyrus..."
    alphys "..."
    alphys "Undyne is right, you are way too nice..."
    papyrus "?"
    papyrus "I JUST DO WHAT I THINK IS THE CORRECT THING TO DO"
    papyrus "THAT'S NOT BEEN NICE"
    papyrus "IT'S BEEN CONSEQUENT"
    alphys "Well..."
    alphys "..."
    alphys "..."
    extend " If you say so"
    if pen and not program and not penAtSans:
        papyrus "DR. ALPHYS, I KNOW YOU ARE BUSY"
        papyrus "BUT I HAVE A PROBLEM ONLY YOU CAN SOLVE"
        alphys "What do you mean?"
        papyrus "I HAVE HERE THE BLUEPRINTS OF A DETERMINATION ABSORBING MACHINE"
        alphys "How you..."
        papyrus "I CANNOT TELL YOU THAT"
        papyrus "JUST..."
        papyrus "TRUST ME"
        alphys "Ok..."
        papyrus "SOMEONE IS TRAPPED THERE"
        papyrus "IT BECAME PURE DETERMINATION ONCE"
        papyrus "BUT WITH THIS MACHINE IS GETTING THEIR ORIGINAL FORM BACK"
        papyrus "BUT THE PROCESS IS NOT COMPLETE"
        papyrus "CAN YOU SEE IF THERE'S A WAY TO COMPLETE THE PROCESS?"
        alphys "With just the bluprints?"
        papyrus "I DON'T HAVE MORE WITH ME, I'M..."
        alphys "It's going to be a piece of cake"
        papyrus "THANKS!"
        papyrus "JUST KEEP THE THING A SECRET, PLEASE"
        alphys "Will do."

    papyrus "GOOD NIGHT DR ALPHYS"
    papyrus "DREAM OF TINY UNDYNES BEEN AWESOME"
    alphys "PAPYRUS!"

    if pen and not program and not penAtSans:
        alphys "I'm sorry Papyrus"

    jump day3

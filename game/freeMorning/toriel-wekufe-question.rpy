label torielWekufeQuestion:
    show papyrusImg coolDude realizing
    papyrus "OK"
    papyrus "I NEED TO DO THIS..."
    papyrus "BUT I DON'T WANNA"
    show sansImg hoddie neutral flip at fade:
        xpos 0.5
    sans "do you not want to do what?"
    show papyrusImg coolDude scared
    papyrus "ARGH!"
    hide papyrusImg
    papyrus "{fast}GOODBYESANSINEEDTOSPEAKWITHTORIEL                                                                                                                                                          {nw}"
    play music "music/05 Ruins.mp3" fadein 1 fadeout 1
    play sound "music/fx/thump.wav"
    scene toriel house with hpunch
    pause(0.5)
    show torielImg teacher neutral zorder 2 at fade:
        xpos 0.0
    toriel "I hope everything is ok at the school"
    toriel "I had to leave early but..."
    show torielImg teacher surprised
    papyrus "TORIEL!"
    show papyrusImg coolDude realizing zorder 1 at fade:
        xpos -0.1
    show torielImg teacher neutral flip zorder 2 at fade:
        xpos 0.4
    toriel "Oh!"
    show torielImg teacher neutral 
    toriel "I'll call you later I have visitors"
    show torielImg teacher neutral flip 
    toriel "Well, what are you two doing around here?"
    show papyrusImg coolDude thinking
    papyrus "TWO?"
    show sansImg hoddie neutral zorder 3 at fade:
        xpos 0.0
    show papyrusImg coolDude realizing
    sans "i don't either"
    show sansImg hoddie neutral flip zorder 3 at fade:
        xpos 0.5
    sans "papyrus? care to explain us?"
    papyrus "........................"
    gaster "YES, THIS IS WAY MORE UNCONFORTABLE THAN USUAL"
    papyrus "........................"
    gaster "MAYBE YOU CAN SPIN THIS SOMEHOW..."
    papyrus "!!!"
    show papyrusImg coolDude thinking
    papyrus "I WAS..."
    papyrus "THINKING..."
    papyrus "ABOUT..."
    papyrus "THE KIDNAPPERS..."
    show torielImg teacher worried flip
    toriel "Oh, Papyrus...."
    toriel "Do not worry about that, we'll take care of everything..."
    show papyrusImg coolDude explaining
    papyrus "I WAS JUST... WELL... THINKING THAT THEY WERE WEIRDLY... REALLY STIFF..."
    if not altRoute:
        papyrus "AND WEIRDLY WEAK?"
        show papyrusImg coolDude checkThis
        papyrus "LIKE, I KNOW I'M GREAT AND ALL BUT..."
        show papyrusImg coolDude thinking
        papyrus "DON'T YOU FIND THAT KIND OF SUSPICIOUS?"
        gaster "OH NO... OH NO..."
        show papyrusImg coolDude offended
        papyrus "YOU SHUT UP"
        $ gasterDreamsShattered = True
    else: 
        papyrus "NOT REALLY EXPRESSIVE AT ALL???"
        show torielImg teacher neutral flip
        toriel "Well... there are humans which are not really expressive..."
        show sansImg hoddie sideglance flip
        sans "also monsters..."
        papyrus "...."
        show papyrusImg coolDude thinking
        papyrus "I DON'T NOW WHY... BUT..."
        papyrus "THEY KINDA FELT DIFFERENT ANYWAY..."
    papyrus "SO..."
    show papyrusImg coolDude uhh
    papyrus "FOR... RESEARCH..."
    papyrus "I WAS WONDERING... IF IT'S THERE MORE BEINGS BEYOND HUMANS AND MONSTERS????"
    show torielImg teacher unsure flip
    toriel "Mmmm"
    show sansImg hoddie neutral flip
    sans "i don't see why not"
    sans "but if they weren't humans according to you"
    sans "why did they look so much like humans?"
    show papyrusImg coolDude thinking
    papyrus "I WAS THINKING..."
    papyrus "IT'S THERE SOMETHING THAT... KINDA GLUES SOUL AND BODY TOGETHER?"
    show torielImg teacher angry flip
    toriel "Spirit"
    show papyrusImg coolDude surprised happy
    show sansImg hoddie surprised zorder 3 at fade:
        xpos 0.0
    "!"
    show torielImg teacher unsure flip
    toriel "I think that the name..."
    papyrus "IS IT THERE SOMETHING LIKE THAT?"
    show torielImg teacher explaining flip
    toriel "Well, I don't think we as monsters have any surviving investigation about it"
    show torielImg teacher unsure flip
    toriel "Specially because, even if it's there something, monster magic have no way to destroy or change that union"
    show torielImg teacher explaining flip
    toriel "The only way we as monsters have to destroy the union between soul and body is by destroying either the soul or the body"
    sans "are you saying there's a kind of being that can destroy the spirit of another being and then basically possess its soul and body?"
    show papyrusImg coolDude delight
    papyrus "YES! EXACTLY"
    "...."
    show torielImg teacher unsure flip
    toriel "Why I feel there some investigation I'm missing?"
    show papyrusImg coolDude careful
    papyrus "..................."
    show sansImg hoddie neutral flip zorder 3 at fade:
        xpos 0.5
    sans "There's some investigation we're missing"
    show torielImg teacher angry flip
    toriel "Papyrus, what do you know?"
    pause(2)
    show papyrusImg coolDude neutral
    papyrus "I WAS READING THE HUMAN INTERNET AND I FOUND SOMETHING SIMILAR AND APARENTLY ARE CALLED WEKUFE"
    show torielImg teacher surprised flip
    toriel "I haven't heard that word in my life"
    show torielImg teacher angry flip
    toriel "And Gerson could barely preserve the most important parts of our history after the war..."
    toriel "If I don't think I had heard the word, most probably there's not surviving records of those beings from the monsters perspective"
    hide torielImg
    toriel "I guess we'll have to check the human internet"
    show papyrusImg coolDude careful
    papyrus "NOW?"
    sans "you asked"
    hide sansImg
    hide papyrusImg
    papyrus "FINE..."
    scene papyrusWekufe frame1 with dissolve
    sans "according to this, they seem to be spirits without souls or body"
    sans "we shouldn't be able to even see them"
    toriel "Unless they possesed a body and a soul"
    sans "well..."
    sans "according to some humans they can possess a kind of soul which are..."
    sans "about to go to a higher plane..."
    papyrus "BEFORE THEY GET BROKEN UP"
    pause(2)
    show torielImg teacher unsure flip zorder 2 at fade:
        xpos 0.4
    show papyrusImg coolDude thinking zorder 1 at fade:
        xpos -0.1
    toriel "I don't get it"
    show torielImg teacher explaining flip
    toriel "It cannot exist a being without a soul or a body, right?"
    show sansImg hoddie worried zorder 3 at fade:
        xpos 0.2
    sans "not in this dimension... i guess"
    show torielImg teacher surprised flip
    toriel "Dimension?"
    papyrus "IS IT THERE SOMETHING ABOUT THE..."
    papyrus "CHINCHE MAPU???"
    show sansImg hoddie worried flip
    sans "miñche mapu..."
    show torielImg teacher unsure flip
    toriel "What's a Mapu?"
    hide sansImg
    sans "those seems to be like... lands?"
    sans "but i think it's more like dimensions..."
    sans "and our dimension is called... nag mapu???"
    "..."
    show sansImg hoddie neutral zorder 3 at fade:
        xpos 0.2
    sans "it's a cosmology we're not familiar with, it's impossible for us to understand it fully just by reading humans' webpages"
    sans "but i think that's the gist of it"
    toriel "So, to recap"
    show torielImg teacher explaining flip
    toriel "We're talking about beings from another dimension without a soul or a body"
    toriel "Which can separate soul and body"
    toriel "possess it" 
    toriel "use it to roam the earth"
    toriel "and Papyrus is suggesting a group of those beings kidnapped Frisk"
    show sansImg hoddie sideglance
    sans "yes, i understand"
    sans "we better go back to our work"
    stop music fadeout 2
    pause(3)
    play music "music/15 sans.mp3" fadeout 1
    show torielImg teacher angry flip
    toriel "Why that makes so much sense?"
    show sansImg hoddie surprised
    show papyrusImg coolDude realizing
    papyrus "UH?"
    hide torielImg
    show sansImg hoddie surprised zorder 3 at fade:
        xpos 0.6
    toriel "We need to go to the forest"
    if not altRoute:
        show sansImg hoddie surprised flip
        toriel "I'll call the humans and move our visit"
        show sansImg hoddie surprised
        toriel "If this is true, we have nothing to talk with them"
    hide sansImg
    toriel "I'm going to find them and they are going to get an earful about kidnapping my child!"
    stop music fadeout(3)
    pause(4)
    hide papyrusImg
    play sound "music/fx/steps.wav"
    scene black with dissolve
    pause(1)
    scene forest with dissolve
    show papyrusImg coolDude realizing at fade:
        xpos 0.4
        ypos 0.0
    show gaster trapped oh at fade:
        xpos -0.1
    gaster "THIS IS BAD"
    gaster "THE WEKUFES SEEM REALLY SCARED OF US MONSTERS FOR SOME REASON"
    gaster "I DO NOT THINK HAVING THE QUEEN OF ALL MONSTERS GOING AFTER THEM IS GOING TO HELP OUR CAUSE"
    gaster "I WOULD SUGGEST RESTART IF YOU LIKE"
    show papyrusImg coolDude angry flip
    papyrus "YOU RIGHT"
    hide papyrusImg
    play music "music/24 Bonetrousle.mp3" fadeout 1
    papyrus "I GOTTA TELL THEM"
    show gaster trapped wait at fade:
    gaster "NO.. I.. I..."
    show gaster trapped sad at fade:
    gaster "OH WELL..."

    scene black with dissolve
    pause(1)
    scene papyrusWekufe frame2 with dissolve:
        ypos 0
        linear 20 ypos -0.6
    pause(1)
   
    if altRoute:
        show goon1 at fade:
            xpos -0.1
            ypos 0.2
        invunche "Hey, Boss..."
        show goon2 flip at fade:
            xpos 0.3
        trauco "What?!"
        show goon1 flip
        show goon2 flip at fade:
            xpos 0.1
        invunche "It seems a... very thin human is running up here..."
        trauco "Wait"
        trauco "That's not one of the monsters?"
        show goon1
        invunche "Which ones?"
        trauco "The ones who saved our last kid this week"
        show goon1 flip
        invunche "Ohhh..."
        show goon2
        trauco "Hey!"
        show goon3 flip at fade:
            xpos 0.5
        voladora "What's up boss?"
        trauco "Go tell them what's going on"
        trauco "We'll try to keep them busy"
        show goon1
        invunche "No, I will not"
        show cuero flip at fade:
            xpos 0.4
        cuero "There's no need"
        hide cuero
        cuero "I will talk with him"
        hide goon2
        show goon3
        trauco "But..."
        hide goon1
        hide goon3
    
    pause(1)
    scene wekufeLab with dissolve
    pause(1)
    show papyrusImg coolDude angry at fade:
        xpos -0.1
    papyrus "I MADE IT IN TIME!"
    gaster "I REALLY DON'T KNOW WHY ARE YOU HERE"
    show coo flip at fade:
        xpos 0.4
    coo "You better have a good explanation of why are you here"
    show papyrusImg coolDude hangOn
    papyrus "GOOD CHUNK OF THE NEW MONSTER KINGDOM MONSTERS IS SEARCHING FOR YOU AT THE FOREST"
    papyrus "I CAME TO TELL YOU NOT GO THERE"
    coo "But, how do you know this place?"
    show papyrusImg coolDude thinking
    papyrus "AHHH...."
    show papyrusImg coolDude uhh
    papyrus "CAN I TALK WITH THE CUERO PERSON PLEASE???"
    coo "No"
    show coo flip at fade:
        xpos 0.5
    show cuero flip at fade:
        xpos 0.3
    cuero "Yes, of course you can"
    papyrus "I CAN HEAR THE ANOMALY"
    papyrus "HIS NAME IS GASTER!"
    stop music 
    play sound "music/fx/thump.wav"
    scene wekufeLab with vpunch
    show sansImg hoddie surprised zorder 3 at fade:
        xpos 0.1
    sans "what?!"
    pause(3)
    cuero "And I see you also have an unwanted companion"
    show papyrusImg coolDude desperate flip at fade:
        xpos 0.4
    papyrus "WHAT ARE YOU..."
    show papyrusImg coolDude realizing flip
    papyrus "OH, RIGHT"
    cuero "So, they follow you around because they don't trust you enough, I see"
    show papyrusImg coolDude angry
    show sansImg hoddie tired
    papyrus "HEY!"
    show papyrusImg coolDude uhh
    papyrus "WE HAVE... FAMILY ISSUES..."
    show papyrusImg coolDude angry
    papyrus "WE'RE... WORKING ON THEM"
    cuero "If this make you feel ok, I can barely recall our last conversation"
    cuero "But you haven't used your magic against us twice"
    show papyrusImg coolDude annoyed
    papyrus "EH..."
    cuero "I hope you can keep your... family from doing that as well"
    show sansImg hoddie worried
    sans "this are the wekufe?"
    sans "from where you know them?"
    show cuero flip zorder 2 at fade:
        xpos 0.3
    show papyrusImg coolDude annoyed zorder 1 at fade:
        xpos 0.1
    cuero "We're collecting determination from human children"
    cuero "That collected determination has caused an anomaly"
    sans "why are you telling us that?"
    cuero "Because that determination seems to be something your family member needs to communicate with someone important"
    show sansImg hoddie surprised
    sans "uh? papyrus?"
    hide cuero
    show papyrusImg coolDude uhh flip at fade:
        xpos 0.3
    papyrus "THAT DETERMINATION IS THE REASON I CAN HEAR AND SEE GASTER FROM WHEREVER HE IS"
    papyrus "I COULD ALSO RELIVE 2 DAYS AND A HALF THANKS TO HIM"
    sans "then why you didn't..."
    sans "..."
    show sansImg hoddie sideglance
    sans "right"
    papyrus "IF IT MAKES YOU FEEL BETTER"
    papyrus "THE THEORY WAS YOU WILL NEVER BELIEVE ME IN LESS THAN 3 DAYS"
    sans "thanks, i guess"
    papyrus "THE..."
    show papyrusImg coolDude explaining flip
    papyrus  "WHOLE POINT OF ALL OF THIS IS..."
    papyrus  "MAYBE..." 
    show papyrusImg coolDude delight flip
    papyrus "WE COULD USE THAT DETERMINATION TO GET GASTER BACK!"
    papyrus "THIS IS PROBABLY THE ONLY OPPORTUNITY WE HAVE WITH THIS MUCH DETERMINATION!"
    gaster "WITHOUT BREAKING SOME LAWS THE QUEEN SURELY PUT ON THE BOOKS"
    show papyrusImg coolDude annoyed flip
    papyrus "YOU SHUT UP"
    show sansImg hoddie worried
    sans "i..."
    sans "i don't know i would like that..."
    show papyrusImg coolDude surprised flip
    papyrus "UH?"
    papyrus "WHAT?"
    sans "i tried to get him back so many times and..."
    sans "i just have to give up..."
    sans "and i was finally feeling confortable moving away..."
    show papyrusImg coolDude neutral flip
    papyrus "I SEE"
    papyrus "I UNDERSTAND"
    papyrus "YOU DON'T HAVE TO DO IT"
    show papyrusImg coolDude delight flip
    papyrus "I'LL DO IT MYSELF"
    show sansImg hoddie surprised
    sans "uh?"
    play music "music/06 Cliffs.mp3" fadein 5
    show papyrusImg coolDude neutral zorder 1 at fade:
        xpos -0.1
    hide sansImg
    papyrus "CUERO, THAT'S THE NAME?"
    show cuero flip zorder 2 at fade:
        xpos 0.4
    cuero "If you want it to be"
    papyrus "I'M GUESSING THIS WHOLE ANOMALY IS MESSING WITH YOUR EXPERIMENTS WITH DETERMINATION"
    cuero "You guessed correctly"
    cuero "The first thing I remember have tried was the only thing which has work so far"
    cuero "Which was to reverse the flow of the determination"
    if program:
        cuero "I'm guessing that program you have been using does the same thing"
    cuero "I don't know why exactly, but the 4th dimension of the Nag Mapu went out of shape"
    gaster "THAT WAS THE 1ST RESET"
    gaster "THE MOMENT I ACTUALLY FIGURE OUT IT WASN'T THE SAME SITUATION AS BEFORE"
    cuero "I assume your friend connected with the determination on the tanks"
    cuero "Because it was the only way to keep the equilibrium"
    if program:
        cuero "Using the same method again, must cause another monster to connect with the determination of the tanks"
        cuero "Since that determination is too much for the monster in question"
        cuero "Goes where the other monster is"
        cuero "But an imbalance occours"
        cuero "And the other monster is sent where the new monster was"
    show papyrusImg coolDude thinking
    papyrus "THAT THE ONLY THING YOU SAY IT WORKS"
    cuero "I have tried diferent ways to change how the determination flows"
    cuero "If your friend haven't felt them, then they were unsuccesful"
    gaster "THAT'S CORRECT. I NEVER FELT ANYTHING"
    show papyrusImg coolDude explaining
    papyrus "ARE YOU SAYING THERE'S NO WAY TO TAKE HIM OUT?"
    if program:
        papyrus "WITHOUT... YOU KNOW..."
    cuero "Not by my efforts, no"
    show papyrusImg coolDude uhh
    papyrus "I... HAVE BAD NEWS..."
    cuero "I suspected that"
    show papyrusImg coolDude scared
    papyrus "???"
    cuero "You are a being from the Nag Mapu and your soul is trying to handle the weirdness of everything"
    show papyrusImg coolDude realizing
    papyrus "..."
    show papyrusImg coolDude explaining
    papyrus "I'M AWARE I'M TRAVELING IN TIME"
    papyrus "BUT I FORGET ALMOST EVERYTHING"
    papyrus "I CANNOT LEARN NEW THINGS"
    papyrus "IT TAKES TONS OF EFFORT TO REMEMBER I HAVE TO DO SOMETHING DIFFERENT"
    show papyrusImg coolDude realizing
    papyrus "AND MOST OF THE TIME I'M NOT THE ONE WHO DECIDES THAT"
    show sansImg hoddie surprised zorder 3 at fade:
        xpos 0.0
    sans "are you..."
    papyrus "YES..."
    show sansImg hoddie worried
    sans "mmm..."
    gaster "THAT'S PRECIOUS"
    gaster "IT MEANS YOUR FRIEND DOESN'T REMEMBER WHAT THEY DID... THAT TIME"
    gaster "BECAUSE US, AS BEINGS FROM THIS DIMENSION"
    gaster "CANNOT REALLY HANDLE TIME TRAVEL"
    hide papyrusImg
    show sansImg hoddie neutral zorder 3 at fade:
        xpos 0.1
    sans "why are you trying to help him?"
    cuero "It just not convenient for us wekufes to have monsters on our bad side, that's all"
    sans "yes, i will believe that"
    cuero "Also, I guess, it is because you might have some knowledge which can help us with our next experiment"
    cuero "But, mostly, because I really want to get over with this loop"
    sans "i see"
    sans "unlike us you are perfectly aware this is a repeat from days before"
    cuero "And anyway cannot avoid doing almost the same thing over and over again"
    cuero "My spirit might be from the Miñche Mapu"
    cuero "But the body and soul I'm using is from here"
    show papyrusImg coolDude neutral zorder 1 at fade:
        xpos -0.1
    papyrus "YOU WANT TO ESCAPE THE LOOP AND GET MONSTERS' SCIENCE KNOWLEDGE"
    cuero "That's correct"
    if not program:
        show papyrusImg coolDude explaining zorder 1 at fade:
            xpos -0.1
        papyrus "WHAT WOULD HAPPEN IF YOU TRY TO REVERSE THE FLOW OF DETERMINATION AGAIN?"
        cuero "Something with your friend I'm guessing"
        cuero "It seems you are also linked by that determination"
        cuero "So, something will happen to you as well"
        show sansImg hoddie worried flip
        sans "papyrus?"
        sans "what are you..."
    else:
        pause(3)
    hide sansImg
    show papyrusImg coolDude thinking
    pause(3)
    papyrus "..."
    show papyrusImg coolDude neutral
    papyrus "I CAN FOR SURE, ONLY GIVE YOU ONE THING OF WHAT ARE YOU ASKING"
    show papyrusImg coolDude explaining
    papyrus "THE OTHER, WELL"
    show papyrusImg coolDude neutral
    papyrus "OTHER PEOPLE CAN GET ACCESS TO IT"
    papyrus "IT WOULD DEPEND OF THEM TO GIVE YOU ACCESS OR NOT"
    papyrus "THAT THE ONLY THING I CAN PROMISE YOU"
    cuero "In exchange to get you out"
    stop music
    papyrus "IN EXCHANGE TO GET ME OUT"
    scene white with dissolve
    pause(1)
    play sound "music/fx/iau.wav"
    pause(3)
    scene black with dissolve
    play music "music/81 An Ending.mp3" fadein(5)
    pause(1)
    scene toriel house with dissolve
    pause(1)
    show gaster free worried at fade:
        xpos -0.1
    show torielImg teacher worried flip zorder 2 at fade:
        xpos 0.3
    gaster "AND THAT WAS WHAT ROUGHLY HAPPENED"
    toriel "Those... beings have... trapped your youngest son...."
    toriel "And they made a spell so we'll not remember him..."
    show gaster free doubt 
    gaster "ACTUALLY, THE MEMORY LOSS HAS NOTHING TO DO WITH THEM"
    gaster "AND THEY DIDN'T CAPTURE HIM, IT'S SOMETHING PAPYRUS HIMSELF DECIDED"
    show gaster free happy
    gaster "I DON'T THINK ANYONE IS ABLE TO CAPTURE HIM"
    show gaster free doubt
    gaster "BUT AT THE SAME TIME HE MUST BE UNABLE TO CAPTURE ANYONE AS WELL..."
    show torielImg teacher neutral flip
    toriel "He sounds like your son alright"
    show torielImg teacher explaining flip
    toriel "Still, it's feels weird I'm not able to remember him..."
    show torielImg teacher worried flip
    toriel "Frisk told me he was their friend..."
    show gaster free compassionate
    gaster "YES, IT'S SAD..."
    gaster "..."
    show gaster free worried
    gaster "I DON'T KNOW WHAT WE'RE GOING TO DO"
    show gaster free happy
    gaster "WE'RE GOING TO GET HIM OUT..."
    show gaster free worried
    gaster "I DON'T THINK THE WEKUFES WILL DO WHAT THEY SAID"
    show torielImg teacher unsure flip
    toriel "Do you think?"
    gaster "I..."
    show gaster free compassionate
    gaster "I BELIEVE THIS WAS JUST PAPYRUS FINDING AN EXCUSE TO LET ME GO"
    show torielImg teacher worried flip
    toriel "You don't want that"
    show gaster free angry
    gaster "OF COURSE NOT..."
    show gaster free worried
    gaster "THIS IS MY FAULT..."
    gaster "IF I WEREN'T TRAPPED, HE WOULD NOT BE TRAPPED RIGHT NOW"
    gaster "I...."
    gaster "I...."
    show torielImg teacher neutral flip
    toriel "You might need help for that..."
    toriel "Where's Sans?"
    show gaster free happy
    gaster "AT HOME"
    show gaster free doubt
    gaster "LOOKING AT THE CEILING..."
    show gaster free doubt flip
    hide torielImg
    toriel "Then lets go"
    hide gaster
    toriel "I think Frisk is already there..."
    scene black with dissolve
    nvl clear
    pause(3)
    "WELL, YEAH, THEY ARE RIGHT"
    "HOPEFULLY EVERYTHING IS GOING TO BE BETTER"
    "..."
    ".."
    "."
    "HOPEFULLY "
    nvl clear
    ""
    stop music fadeout(1)
    pause(1.5)
    # $ renpy.set_return_stack([])
    $ renpy.retain_after_load()
    $ persistent.endingPapyrus = False
    $ persistent.endingGaster = True
    $ renpy.quit()
return
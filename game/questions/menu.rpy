label questionsEnd:
    stop music fadeout 1
    scene black with dissolve
    pause(1.0)
    play music "music/another him.MP3" fadein 1
    scene mistColor with dissolve
    show mist at fade
    pause(1.0)
    show papyrusImg neutral at fade:
        xpos -0.1
    show gaster trapped neutral flip at fade:
        xpos 0.4
    gaster "THEN, MY DEAR PAPYRUS, THERE'S SOMETHING YOU WANT TO TALK WITH ME?"
    call questionsMenu from _call_questionsMenu
    return

label questionsMenu:
    menu:
        "This is a time loop, right?":
            call decisions from _call_decisions
        "What do I do with this Storage Unit?":
            call pendriveTree from _call_pendriveTree
        #"Those Weird Monsters I found":
        #    call monstersForest from _call_monstersForest
        "Political Geography":
            call politicalGeographyTree from _call_politicalGeographyTree
        #"I know something I really didn't knew I knew" if papyrusKnowsProgramming:
        #    call programmingTree
        "Papers with Weird Symbols only I can read" if papersPapyrusCreation and politicalGeography > 2:
            call sansPapyrusPast from _call_sansPapyrusPast
        #"Demography" if politicalGeography > 0:
        #    call demographics
        "Wait, King Fluffybuns?" if politicalGeography > 0:
            call gasterGerson from _call_gasterGerson
        "Skeleton During the Great War" if gasterPast > 0:
            call gasterPastTree from _call_gasterPastTree
        "Something is wrong with the program" if not firstTry:
            call programAgainTree
        "4th Wall Breaking Stuff":
            call fourthWallTree from _call_fourthWallTree
        "Nothing Else":
            show papyrusImg uhh
            papyrus "NOTHING I CAN THINK OF RIGHT NOW"
            show gaster trapped sorry flip 
            gaster "VERY WELL"
            show gaster trapped neutral flip 
            gaster "GOOD NIGHT MY DEAR PAPYRUS"
            stop music
            return
        "Reset" if resetFromQuestionMenu:
            show papyrusImg annoyed
            show gaster trapped neutral flip
            gaster "ARE YOU SURE YOU WANT TO RESET?"
            menu: 
                "Yes":
                    gaster "WELL THEN"
                    jump day1
                "No":
                    gaster "VERY WELL"
                    gaster "BE CAREFUL WITH CLICKING NEXT TIME"
    call questionsMenu from _call_questionsMenu_1
    return

label programAgainTree:
    menu:
        "Something is wrong with the program":
            call fileAlphysTryAgain
        "But why I cannot do it!?" if program2ndChance > 0:
            call papyrusWantsToTry
        "Change of Plans!" if program2ndChance > 1:
            call changeOfPlans
        "Back":
            return
    return

label sansPapyrusPast:
    menu:
        "Papers with Weird Symbols only I can read" if papersPapyrusCreation and politicalGeography > 2:
            call foundSomePapers from _call_foundSomePapers
        "Why did you created us?" if sansPapyrusPast > 0:
            call sansWantsABrother from _call_sansWantsABrother
        "Skeleton Disco Wave" if sansPapyrusPast == 2:
            call skeletonWave from _call_skeletonWave
        "Return":
            return
    return 


label pendriveTree:
    menu:
        "What do I do with this Storage Unit?":
            call pendriveBrainStorm from _call_pendriveBrainStorm
        "What about your brother?" if pendriveTree > 0:
            call pendriveSans from _call_pendriveSans
        "Can you tell me what the problem with your brother?" if pendriveTreeSans > 0:
            call pendriveSansTwo from _call_pendriveSansTwo
        "What about the Royal Scientist?" if pendriveTree > 0:
            call pendriveAlphys from _call_pendriveAlphys
        "Are you ok?" if pendriveTreeAlphys > 0:
            call pendriveAreYouOk from _call_pendriveAreYouOk
        "What is Alphys doing now anyways?" if pendriveTreeAlphys > 1:
            call pendriveAlphysThree from _call_pendriveAlphysThree
        "Did Alphys said she needs more time?" if alphysFailStateBoleean and pendriveTreeAlphys > 2:
            call pendriveAlphysFailState from _call_pendriveAlphysFailState
        "Return":
            return
    return

label programmingTree:
    menu:   
        "I know something I really didn't knew I knew" if papyrusKnowsProgramming:
            call programmingTheory from _call_programmingTheory
        "Maybe I can do something with this programming thing" if programmingWoes2 > 0:
            call programmingMagicTheory from _call_programmingMagicTheory
        "Then, how do Sans do it?" if programmingWoes2 > 1:
            call theoryBehind from _call_theoryBehind
        "Return":
            return
    return

label politicalGeographyTree:
    menu:
        "Political Geography": 
            call politicalGeography from _call_politicalGeography
        "Political Geography 2" if politicalGeography > 0:
            call politicalGeography2 from _call_politicalGeography2
        "Higher Snowdin" if politicalGeography > 1:
            call geoSnowdin from _call_geoSnowdin
        "Lower Snowdin" if politicalGeography > 2:
            call elevatorSnowdin from _call_elevatorSnowdin
        "A Mystery" if politicalGeography > 2:
            call aMystery from _call_aMystery
        "Return":
            return
    return

label gasterPastTree:
    menu:
        "Skeleton During the Great War" if gasterPast > 0:
            call gasterWar from _call_gasterWar
        "Skeleton Duties" if gasterPast > 0:
            call gasterDuties from _call_gasterDuties
        "The Talk" if gasterPast > 1:
            call gasterCreation from _call_gasterCreation
        "Adridged History of the Skeleton Kind" if gasterPast > 2:
            call skeletonKind from _call_skeletonKind
        "Skeleton Creation" if gasterPast > 3:
            call superSoldiers from _call_superSoldiers
        "I WAS NEVER A CHILD?!" if gasterPast > 4:
            call noChildhood from _call_noChildhood
        "Blank Science Encyclopedia" if gasterPast > 5 and gasterScienceEncyclopedia:
            call blankScience
        "Return":
            return
    return
        
label fourthWallTree:
    menu:
        "4th Wall Breaking Stuff":
            call wallBreakingStuff from _call_wallBreakingStuff
        "More 4th Wall Breaking Stuff" if wallBreakingStuff > 0:
            call moreWallBreakingStuff from _call_moreWallBreakingStuff
        #"4th Wall Breaking Stuff 2" if programmingWoes2 > 0:
        #    call wallBreakingStuff2 from _call_wallBreakingStuff2
        "Return":
            return
    return 



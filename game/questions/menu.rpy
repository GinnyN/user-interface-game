label questionsEnd:
    gaster "THEN, MY DEAR PAPYRUS, THERE'S SOMETHING YOU WANT TO TALK WITH ME?"
    jump questionsMenu
    return

label questionsRepeat:
    gaster "WELL THEN"
    gaster "SOMETHING ELSE ARE YOU CURIOUS ABOUT?"
    jump questionsMenu
    return

label questionsMenu:
    menu:
        "This is a time loop, right?":
            call decisions from _call_decisions
        "Those Weird Monsters I found":
            call monstersForest from _call_monstersForest
        "I know something I really didn't knew I knew" if papyrusKnowsProgramming:
            call programmingTheory from _call_programmingTheory
        "Maybe I can do something with this programming thing" if programmingWoes2 > 0:
            call programmingMagicTheory from _call_programmingMagicTheory
        "Political Geography":
            call politicalGeographyTree
        "Papers with Weird Symbols only I can read" if papersPapyrusCreation and politicalGeography > 2:
            call foundSomePapers from _call_foundSomePapers
        #"Demography" if politicalGeography > 0:
        #    call demographics
        "Wait, King Fluffybuns?" if politicalGeography > 0:
            call gasterGerson from _call_gasterGerson
        "Skeleton During the Great War" if gasterPast > 0:
            call gasterPastTree
        "4th Wall Breaking Stuff":
            call fourthWallTree
        "Nothing Else":
            papyrus "NOTHING I CAN THINK OF RIGHT NOW"
            gaster "VERY WELL"
            return
    jump questionsRepeat
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
            call questionsMenu
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
        "Return":
            call questionsMenu
    return
        
label fourthWallTree:
    menu:
        "4th Wall Breaking Stuff":
            call wallBreakingStuff from _call_wallBreakingStuff
        "More 4th Wall Breaking Stuff" if wallBreakingStuff > 0:
            call moreWallBreakingStuff from _call_moreWallBreakingStuff
        "4th Wall Breaking Stuff 2" if programmingWoes2 > 0:
            call wallBreakingStuff2 from _call_wallBreakingStuff2
        "Return":
            call questionsMenu
    return 



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
            call decisions
        "Those Weird Monsters I found":
            call monstersForest
        "I know something I really didn't knew I knew" if papyrusKnowsProgramming:
            call programmingTheory
        "Political Geography": 
            call politicalGeography
        "Political Geography 2" if politicalGeography > 0:
            call politicalGeography2
        "Higher Snowdin" if politicalGeography > 1:
            call geoSnowdin
        "Lower Snowdin" if politicalGeography > 2:
            call elevatorSnowdin
        "Papers with Weird Symbols only I can read" if papersPapyrusCreation and politicalGeography > 2:
            call foundSomePapers
        "A Mystery" if politicalGeography > 2:
            call aMystery
        #"Demography" if politicalGeography > 0:
        #    call demographics
        "Wait, King Fluffybuns?" if politicalGeography > 0:
            call gasterGerson
        "Skeleton During the Great War" if gasterPast > 0:
            call gasterWar
        "Skeleton Duties" if gasterPast > 0:
            call gasterDuties
        "The Talk" if gasterPast > 1:
            call gasterCreation
        "Adridged History of the Skeleton Kind" if gasterPast > 2:
            call skeletonKind
        "Skeleton Creation" if gasterPast > 3:
            call superSoldiers
        "4th Wall Breaking Stuff":
            call wallBreakingStuff
        "More 4th Wall Breaking Stuff" if wallBreakingStuff > 0:
            call moreWallBreakingStuff
        "4th Wall Breaking Stuff 2" if programmingWoes2 > 0:
            call wallBreakingStuff2
        "Nothing Else":
            papyrus "NOTHING I CAN THINK OF RIGHT NOW"
            gaster "VERY WELL"
            return
    jump questionsRepeat
    return

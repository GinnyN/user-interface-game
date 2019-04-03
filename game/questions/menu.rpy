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
        "Political Geography": 
            call politicalGeography
        "Political Geography 2" if politicalGeography > 0:
            call politicalGeography2
        "Higher Snowdin" if politicalGeography > 1:
            call geoSnowdin
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
        "4th Wall Breaking Stuff":
            call wallBreakingStuff
        "More 4th Wall Breaking Stuff" if wallBreakingStuff > 0:
            call moreWallBreakingStuff
    jump questionsRepeat
    return

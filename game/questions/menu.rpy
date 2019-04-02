label questionsEnd:
    gaster "THEN, MY DEAR PAPYRUS, THERE'S SOMETHING YOU WANT TO TALK WITH ME?"
    label questionsMenu
    return

label questionsRepeat:
    gaster "WELL THEN"
    gaster "SOMETHING ELSE ARE YOU CURIOUS ABOUT?"
    label questionsMenu
    return

label questionsMenu:
    menu:
        "Political Geography": 
            call politicalGeography
        "Political Geography 2" if politicalGeography > 0:
            call politicalGeography2
        "Demography" if politicalGeography > 0:
            call demographics
        "Wait, King Fluffybuns?" if politicalGeography > 0:
            call gasterGerson
        "Skeleton Duties" if gasterPast > 0:
            call gasterDuties
        "4th Wall Breaking Stuff":
            call wallBreakingStuff
        "More 4th Wall Breaking Stuff" if wallBreakingStuff > 0:
            call moreWallBreakingStuff
    label questionsRepeat
    return

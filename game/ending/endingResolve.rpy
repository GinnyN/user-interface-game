label endingResolve:
    if penAtAlphys:
        jump getPenFromAlphys
    elif firstTry:
        $ renpy.retain_after_load()
        jump endingsFirstTry
    else:
        gaster "THIS IS THE LAST DAY WE HAVE BEFORE GOING BACK"
        gaster "DO YOU WANT TO TRY USING THE PROGRAM ANYWAY?"
        papyrus "WELL..."
        menu: 
            "Yes, I want to try":
                papyrus "LET'S TRY THIS TIME"
                papyrus "I REALLY DON'T KNOW IF THIS GOING TO WORK, BUT I WANNA SEE"
                gaster "VERY WELL"
                $ renpy.retain_after_load()
                jump endingCase
            "No, let's go back":
                papyrus "I'M NOT SURE"
                papyrus "I GUESS THE SAFEST BET WOULD BE RESET"
                gaster "YES, I DO AGREE"
                jump day1

label endingCase:
    label endingWithSans:
    gaster "I CANNOT FIND WEKUFES ANYWHERE"
    gaster "WE CAN WORK NOW"
    papyrus "GOOD"
    papyrus "I'LL JUST FIRE UP THE PROGRAM AND..."
    gaster "PAPYRUS, MY BOY?"
    papyrus "WE..."
    papyrus "THIS IS NOT GOING TO BE ANY DIFFERENT, RIGHT?"
    gaster "NO..."
    gaster "AS FAR AS WE KNOW..."
    papyrus "SO, WE'RE..."
    gaster "..."
    papyrus "WE ARE"
    gaster "I DON'T KNOW..."
    gaster "I DON'T WANT TO KEEP LIVING LIKE THIS..."
    gaster "BUT I DON'T WANT TO LOSE YOU EITHER..."
    papyrus "DO WE HAVE A 3RD OPTION?"
    gaster "..."
    gaster "I..."
    gaster "..."
    papyrus "WE DON'T"
    gaster "NO..."
    gaster "NO!"
    gaster "WE HAVE TO KEEP INSISTING!"
    gaster "THAT'S HOW THE MONSTERS GOT OUT THE UNDERGROUND!"
    papyrus "NO"
    papyrus "IT WAS FRISK"
    papyrus "WE BELIEVED IN THEM!"
    papyrus "I..."
    papyrus "I BELIEVED IN THEM"
    papyrus "SO I..."
    papyrus "I WILL..."
    menu: 
        "I WILL BELIEVE IN YOU!":
            $ persistent.endingGaster = True
        "I WILL BELIEVE IN MYSELF!":
            $ persistent.endingPapyrus = True  
    $ renpy.save_persistent()
    papyrus "I HOPE YOU CAN FORGIVE ME"
    gaster "I'M NOT SURE I WILL"
    gaster "BUT I'LL SEE YOU AGAIN"
    "* Fade to white *"       

    if endingGaster:   
        if endingSans:
            jump neutralEndingGaster
        else:
            jump wekufeEndingGaster
    else:
        if altRoute:
            "Papyrus Neutral Ending"
        else: 
            jump prisonPapyrusEnding
return
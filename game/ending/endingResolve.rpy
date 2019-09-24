label endingResolve:
    if penAtAlphys:
        jump getPenFromAlphys
    elif firstTry:
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
                jump endingCase
            "No, let's go back":
                papyrus "I'M NOT SURE"
                papyrus "I GUESS THE SAFEST BET WOULD BE RESET"
                gaster "YES, I DO AGREE"
                jump day1

label endingCase:
    if endingSans:
        "Ending in which Sans appears"
    else:
        "Ending in which Sans does not Appear"
return
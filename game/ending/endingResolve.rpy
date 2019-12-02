label endingResolve:
    if penAtAlphys:
        jump getPenFromAlphys
    elif firstTry:
        $ renpy.retain_after_load()
        jump endingsFirstTry
    else:
        scene black with dissolve
        pause(1.0)
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
    stop music fadeout(1.0)
    pause(1.0)
    play music "music/47 Ooo.mp3" fadein 1
    scene wekufeLab with dissolve
    pause(1.0)
    show gaster trapped sad at fade with dissolve:
        xpos -0.1
    gaster "I CANNOT FIND WEKUFES ANYWHERE"
    gaster "WE CAN WORK NOW"
    show papyrusImg annoyed at fade with dissolve:
        xpos 0.4
    papyrus "GOOD"
    papyrus "I'LL JUST FIRE UP THE PROGRAM AND..."
    pause(1)
    show gaster trapped oh
    gaster "PAPYRUS, MY BOY?"
    papyrus "WE..."
    show papyrusImg annoyed flip
    papyrus "THIS IS NOT GOING TO BE ANY DIFFERENT, RIGHT?"
    show gaster trapped sorry
    gaster "NO..."
    gaster "AS FAR AS WE KNOW..."
    papyrus "SO, WE'RE..."
    gaster "..."
    play music "music/94 Respite.mp3" fadein(1)
    show gaster trapped oh
    papyrus "WE ARE"
    gaster "I DON'T KNOW..."
    show gaster trapped sorry
    gaster "I DON'T WANT TO KEEP LIVING LIKE THIS..."
    gaster "BUT I DON'T WANT TO LOSE YOU EITHER..."
    papyrus "DO WE HAVE A 3RD OPTION?"
    gaster "..."
    gaster "I..."
    gaster "..."
    papyrus "WE DON'T"
    gaster "NO..."
    show gaster trapped descisive
    gaster "NO!"
    gaster "WE HAVE TO KEEP INSISTING!"
    gaster "THAT'S HOW THE MONSTERS GOT OUT THE UNDERGROUND!"
    show gaster trapped oh
    papyrus "NO"
    show gaster trapped sorry
    papyrus "IT WAS FRISK"
    show papyrusImg angry flip
    papyrus "WE BELIEVED IN THEM!"
    papyrus "I..."
    show papyrusImg serious flip
    papyrus "I BELIEVED IN THEM"
    papyrus "SO I..."
    papyrus "I WILL..."
    menu: 
        "I WILL BELIEVE IN YOU!":
            $ persistent.endingGaster = True
        "I WILL BELIEVE IN MYSELF!":
            $ persistent.endingPapyrus = True  
    $ renpy.save_persistent()
    show papyrusImg sorry flip
    papyrus "I HOPE YOU CAN FORGIVE ME"
    show gaster trapped happy
    gaster "I'M NOT SURE I WILL"
    gaster "BUT I'LL SEE YOU AGAIN"
    stop music fadeout 3
    scene white with dissolve
    play sound "music/fx/iau.wav"
    pause(2)     

    if persistent.endingGaster:   
        if endingSans:
            jump neutralEndingGaster
        else:
            jump wekufeEndingGaster
    else:
        if altRoute:
            jump neutralEndingPapyrus
        else: 
            jump prisonPapyrusEnding
return
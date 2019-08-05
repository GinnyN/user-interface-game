label day3:
    $ day = 3
    call freeMorning from _call_freeMorning

    call forest

    menu:
        "Help them out":
            call helpthemout
        "Let's them go alone":
            call leaveThemAlone
    call backNewerHome
    
label endOfDay3:
    if resets > 0:
        call questionsEnd from _call_questionsEnd_1
    jump day4
return



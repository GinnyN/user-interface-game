label day3:
    $ day = 3
    call freeMorning from _call_freeMorning

    call forest from _call_forest

    menu:
        "Help them out":
            call helpthemout from _call_helpthemout
        "Let's them go alone":
            call leaveThemAlone from _call_leaveThemAlone
        "Comment about the tanks with determination" if wekufeMeeting > 0:
            call wekufe3rdDayDetermination from _call_wekufe3rdDayDetermination
            jump endOfDay3
            if wekufeMeeting == 1:
                $ wekufeMeeting = 2
    call backNewerHome from _call_backNewerHome
    
label endOfDay3:
    if resets > 0:
        call questionsEnd from _call_questionsEnd_1
    jump day4
return



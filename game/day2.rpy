label day2:
    $ day = 2

    call schoolPapyrusRun from _call_schoolPapyrusRun
    call day2grillsby from _call_day2grillsby
    call sansMeetUndyne from _call_sansMeetUndyne
    call outsideSchool from _call_outsideSchool
#Outside School 


label loop1:
    show papyrusImg angry flip at fade:
        xpos 0.5
    show sansImg hoddie angry at fade:
        xpos 0
        ypos -0.05
    menu:
        "This is for keep my greatness!":
            call honor from _call_honor
            jump loop1
        "Stay away Sans! This is my problem!":
            call stuborn from _call_stuborn
            jump loop1
        "Sans! I have a Plan!":
            jump plan

label plan:
    call iHaveAPlan from _call_iHaveAPlan
    call planning from _call_planning
    call mettatonFashionShow from _call_mettatonFashionShow
    call finishPlan from _call_finishPlan
    jump endOfDay2

label alphysHomeCall:
    call alphysHome from _call_alphysHome
    jump endOfDay2

label endOfDay2:
    if resets > 0:
        call questionsEnd from _call_questionsEnd_2
    jump day3
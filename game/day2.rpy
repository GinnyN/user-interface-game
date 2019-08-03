label day2:
    $ day = 2

    call schoolPapyrusRun
    call day2grillsby
    call sansMeetUndyne
    call outsideSchool
#Outside School 


label loop1:
    show papyrusImg angry flip at fade:
        xpos 0.5
    show sansImg hoddie angry at fade:
        xpos 0
        ypos -0.05
    menu:
        "This is for keep my greatness!":
            call honor
            jump loop1
        "Stay away Sans! This is my problem!":
            call stuborn
            jump loop1
        "Sans! I have a Plan!":
            jump plan

label plan:
    call iHaveAPlan
    call planning
    call mettatonFashionShow
    call finishPlan
    jump endOfDay2

label alphysHomeCall:
    call alphysHome
    jump endOfDay2

label endOfDay2:
    if resets > 0:
        call questionsEnd from _call_questionsEnd_2
    jump day3
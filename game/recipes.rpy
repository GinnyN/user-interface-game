#Preferences

default preferences.text_cps = 50

#RECIPES
screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    #bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

transform fade:
    on show:
        alpha 0
        linear 0.3 alpha 1
    on hide:
        linear 0.3 alpha 0
    on replace:
        linear 0.2 alpha 1
    on replaced:
        linear 0.2 alpha 0

transform sparkles:
    on show: 
        xpos -1.5
        ypos -1.5
        rotate 0
        alpha 1
        linear 2 rotate 145 alpha 0
        #linear 2 alpha 0

transform panningSuit:
    on show:
        xpos -0.5
        linear 1 xpos 0 


#Count Variables
define resets = 0
define papyrusTraining = 0

#Define Mettaton Variable
define mettatonModel = "v1"
define askUndyne = False
define undyneThere = True
define suit = 1

#Flag Variables
define doors = False
define idea = False
define pen = False
define penAtAlphys = False
define tryWithSans = False
define papyrusMourn = False
define tryWithAlphys = False
define alphysFailState = False
define alphysFailStateBoleean = False
define program = False
define papersPapyrusCreation = False
define readStats = False
define firstTry = True
define gasterInformPosition = False
define gasterScienceEncyclopedia = true

#Flag variables which have to be reset
define whoRescueMauricio = False

#Gaster's Dialogue Tree
define gasterPapyrusSansDad = False
define papyrusKnowsProgramming = False
define resetFromQuestionMenu = False

#Free Mornings
define helpedToriel = False
define metAsgore = False
define visitSans = False
define visitUndyne = False
define visitAlphys = False
define visitFrisk = False

label resetVariables:
    $ day = 1
    $ helpedToriel = False
    $ metAsgore = False
    $ visitSans = False
    $ visitUndyne = False
    $ visitAlphys = False
    $ visitFrisk = False
    $ whoRescueMauricio = False
    $ alphysFailState = False
    $ penAtAlphys = False
    return

#Define Day Alternatives
define day = 1

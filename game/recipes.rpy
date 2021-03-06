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
define gasterScienceEncyclopedia = False
define endingSans = False
define altRoute = False
define giveRingToUndyne = False
define mettatonNumber = False
define mettatonFreeMorning = False
define wekufeMeeting = 0
define askTorielWekufe = False

define weddingFrom = ""
define weddingEnding = False

#Flag variables which have to be reset
define whoRescueMauricio = False

#Gaster's Dialogue Tree
define gasterPapyrusSansDad = False
define papyrusKnowsProgramming = False
define resetFromQuestionMenu = False
define gasterDreamShattered = False

#Free Mornings
define helpedToriel = False
define metAsgore = False
define visitSans = False
define visitUndyne = False
define visitAlphys = False
define visitFrisk = False
define metMettaton = False

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
    $ endingSans = False
    $ altRoute = False
    $ giveRingToUndyne = False
    $ weddingFrom = ""
    $ weddingEnding = False
    $ metMettaton = False
    if persistent.wekufeNames:
        call changeWekufe from _call_changeWekufe
    return

#Define Day Alternatives
define day = 1
define endingGaster = False
define endingPapyrus = False

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

#Count Variables
define resets = 0
define papyrusTraining = 0

#Flag Variables
define doors = False
define idea = False
define torielKnows = False
define asgoreKnows = False
define pen = False
define penAtAlphys = False
define penAtSans = False
define program = False
define papersPapyrusCreation = False

#Gaster's Dialogue Tree
define gasterPapyrusSansDad = False

#Free Mornings
define helpedToriel = False
define metAsgore = False
define visitSans = False

#Define Day Alternatives
define day2 = False

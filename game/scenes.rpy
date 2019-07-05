#background
image black = "#000000"
image mistColor = "#3f575f"
image white = "#ffffff"
image lights = im.FactorScale("background/lights.png",3.0)

#Cinematic Scenes
#Day 1
image day1 scene1 = "background/day1/scene1.png"
image day1 scene2 = "background/day1/scene2.png"
image day1 scene3 = "background/day1/scene3.png"
image day1 scene4 = "background/day1/scene4.png"
image day1 scene5 = "background/day1/scene5.png"
image day1 scene6 = "background/day1/scene6.png"
image day1Alt title = "../gui/main_menu.png"
#Day 2
image day2 papyrusJump frame1 = "background/day2/papyrusjump-frame1.png"
image day2 papyrusJump frame2 = "background/day2/papyrusjump-frame2.png"
image day2 papyrusJump frame3 = "background/day2/papyrusjump-frame3.png"
image day2 papyrusJump frame4 = "background/day2/papyrusjump-frame4.png"
image day2 papyrusLanding frame1 = "background/day2/papyruslanding-frame1.png"
image day2 papyrusLanding frame2 = "background/day2/papyruslanding-frame2.png"
image day2 papyrusLanding frame3 = "background/day2/papyruslanding-frame3.png"
image day2 suit blue = "background/day2/blueSuit.png"
image day2 suit red = "background/day2/redSuit.png"
image day2 suit green = "background/day2/greenSuit.png"
image day2 suit undyne ="background/day2/undyneSuit.png"
#Day 3
image day3F intro foreground = "background/day3/intro-foreground.png"
image day3 intro background = "background/day3/intro-background.png"
image day3F fortress foreground = "background/day3/fortress-foreground.png"
image day3 fortress background = "background/day3/fortress-background.png"
image day3 fortress findMauricio frame1 = "background/day3/findMauricio-frame-1.png"
image day3 fortress findMauricio frame2 = "background/day3/findMauricio-frame-2.png"
image day3 fortress persue frame1 ="background/day3/fortress-persue-frame-1.png"
image day3 fortress persue frame2 ="background/day3/fortress-persue-frame-2.png"
image day3 fortress persue frame3 ="background/day3/fortress-persue-frame-3.png"
image day3 forest hanging ="background/day3/forest-hanging.png"
image day3 forest pickup frame1 = "background/day3/forest-pickup-frame-1.png"
image day3 forest pickup frame2 = "background/day3/forest-pickup-frame-2.png"
image day3 forest pickup frame3 = "background/day3/forest-pickup-frame-3.png"
image day3 forest pickup frame4 = "background/day3/forest-pickup-frame-4.png"
image day3 forest pickup frame5 = "background/day3/forest-pickup-frame-5.png"
image day3 forest pickup frame6 = "background/day3/forest-pickup-frame-6.png"
image day3 forest action frame1 = "background/day3/forest-action-frame-1.png"
image day3 forest action frame2 = "background/day3/forest-action-frame-2.png"
image day3 forest action frame3 = "background/day3/forest-action-frame-3.png"
image day3 forest stop frame1 = "background/day3/forest-stop-frame-1.png"
image day3 forest stop frame2 = "background/day3/forest-stop-frame-2.png"
image day3 forest spear frame1 = "background/day3/forest-spear-frame-1.png"
image day3 forest trident frame1 = "background/day3/forest-trident-frame-1.png"
image day3 forest trident frame2 = "background/day3/forest-trident-frame-2.png"
image day3F nightview foreground = "background/day3/nightview-foreground.png"
image day3 nightview background = "background/day3/nightview-background.png"
image day3 kids cave = "background/day3/kids-in-cave.png"
#Day 4
image day4 gaster = "background/day4/gaster.png"
image day4 homeworkAttack = "background/day4/homeworkAttack.png"
image day4 sansFriskWekufeLab = "background/day4/sansFriskWekufeLab.png"
image day4 gasterFree = "background/day4/gasterFree.png"
image day4 papyrusTrapped = "background/day4/papyrusTrapped.png"
#Free morning
image freeMorning sans resetZero panoramica = "background/freeMorning/sans-reset-zero-panoramica.png"
image freeMorning frisk resetZero scene1 = "background/freeMorning/frisk-zero-scene1.png"
image freeMorning frisk resetZero scene2 = "background/freeMorning/frisk-zero-scene2.png"
image freeMorning frisk resetZero scene3 = "background/freeMorning/frisk-zero-scene3.png"
image freeMorningF frisk resetZero foreground = "background/freeMorning/frisk-zero-foreground.png"
image freeMorning frisk resetZero background = "background/freeMorning/frisk-zero-background.png"
#Try with Sans
image tryWithSans jumpOver = "background/tryWithSans/papyrusOverSchool.png"
image tryWithSans sansShattering frame1 = "background/tryWithSans/sansShattering-frame1.png"
image tryWithSans sansShattering frame2 = "background/tryWithSans/sansShattering-frame2.png"
image tryWithSans sansShattering frame3 = "background/tryWithSans/sansShattering-frame3.png"
image tryWithSans lookingTheDistance frame1 = "background/tryWithSans/watchingTheDistance.png"
image tryWithSans lookingTheDistance frame2 = "background/tryWithSans/watchingTheDistance-frame2.png"
image tryWithSans lookingTheDistance frame3 = "background/tryWithSans/watchingTheDistance-frame3.png"

#Places Backgrounds
image newerHome night = "background/newerHome/night.png"
image toriel house = "background/torielHouse.png"
image skelebroHouse outside = "background/lowersnowdin.png"
image grillsbys inside = "background/grillbys.png"
image school outside = "background/school.png"
image school gym = "background/schoolGym.png"
image school basement = "background/schoolBasement.png"
image undyneAlphysHouse inside = "background/undyneAlphysHouse.png"
image muffetBakery inside = "background/muffetBakery.png"
image elevator outside = "background/elevatorOutside.png"
image forest = "background/forest.png"
image fortress inside = "background/fortressInside.png"
image mountAnemi = "background/mountAnemi.png"
image wekufeLab = "background/wekufeLab.png"
image mist:
    contains:
        alpha 0.2
        HBox("background/mist.png")
        linear 5 alpha 1.0
        linear 5 alpha 0.2
        repeat
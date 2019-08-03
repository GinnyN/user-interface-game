label suitDecision:
    stop music
    scene black with dissolve
    metatton "And the winner is..."
    menu:
        "The Red One":
            $ suit = 1
        "The Blue One":
            $ suit = 2
        "The Green One":
            $ suit = 3
    return

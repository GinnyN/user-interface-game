label mettatonFashionShow:
    call presentation from _call_presentation

    label loopSuit:
        menu:
            "The Red One":
                $ suit = 1
                call bonestrousleSuit from _call_bonestrousleSuit
            "The Blue One":
                $ suit = 2
                call megalovaniaSuit from _call_megalovaniaSuit
            "The Green One":
                $ suit = 3
                call spearsSuit from _call_spearsSuit
        
    jump publicAsk

    label suitDecisionCall:
        call suitDecision from _call_suitDecision

    return
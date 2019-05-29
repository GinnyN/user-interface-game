label freeMorning:
    stop music
    scene skelebroHouse outside with dissolve
    show papyrusImg coolDude happy zorder 0 at fade:
        xpos 0
    papyrus "LOOKIE THAT!"
    papyrus "I HAVE FREE THE MORNING!"
    show papyrusImg coolDude thinking
    papyrus "WHAT SHALL I DO?"
    
    call displayMenuFreeMorning

    return

label displayMenuFreeMorning:
    menu:
        "Go help Toriel at the School" if not helpedToriel:
            show papyrusImg coolDude happy 
            papyrus "LET'S SEE IF TORIEL HAVE SOMETHING TO DO!"
            papyrus "THEY ARE STILL MOVING THINGS FROM THE UNDERGROUND AFTER ALL"
            $ helpedToriel = True
            call torielSchool from _call_torielSchool

        "Go grocery shopping" if not metAsgore:
            papyrus "I'LL BETTER GO TO GET SOME GROCERIES"
            papyrus "MAYBE I CAN FIND SOME DISCOUNTS ON THE SPIDER BAKERY"
            papyrus "EVERYTHING IS ALWAYS SO EXPENSIVE"
            $ metAsgore = True
            call groceryShopping from _call_groceryShopping
            
        "Go check Sans" if not visitSans:
            papyrus "MAYBE I SHOULD CHECK WHAT SANS IS DOING"
            $ visitSans = True
            call checkSans from _call_checkSans

        "Go check with Undyne" if not visitUndyne:
            papyrus "I SHOULD CHECK OUT WITH UNDYNE"
            show papyrusImg coolDude delight
            papyrus "I HAVE A SURPRISE FOR HER AND I DON'T WANT TO FORGET!"
            $ visitUndyne = True
            call visitUndyne from _call_visitUndyne
        
        "Go visit Alphys" if not visitAlphys:
            if penAtAlphys:
                papyrus "I LEFT THE IMPORTANT MISSION TO DR ALPHYS LAST NIGHT"
                papyrus "I DON'T KNOW IF I CAN VISIT HER, I MIGHT BOTHER HER"
                gaster "SHE MIGHT HAVE INSPIRATION ON DOING IT AND THEN WORK IN A HURRY FOR 3 HOURS STRAIGHT"
                papyrus "YOU MEAN SHE MIGHT NEED SOME REFRESTMENTS FOR AVOID DEHYDRATION?"
                gaster "I DON'T THINK SO"
                gaster "SHE LOOKED MORE LIKE THE NOCTURNAL TYPE"
                papyrus "YOU RIGHT"
                papyrus "SHE PROBABLY HAD ALREADY DONE ALL THE WORK"
                papyrus "AND SHE'S SLEEPING RIGHT NOW"
                gaster "I'LL RECOMEND VISIT SOMEONE ELSE"
                papyrus "THAT'S A GOOD IDEA"
                call displayMenuFreeMorning
            else:
                papyrus "DR ALPHYS SAID SHE WAS WORKING ON SOMETHING IMPORTANT"
                show papyrusImg coolDude delight
                papyrus "MAYBE IS A NEW KIND OF PUZZLE!"
                show papyrusImg coolDude thinking
                papyrus "OK, MAYBE NOT"
                show papyrusImg coolDude delight
                papyrus "BUT SHOULD BE INTERESTING!"
                $ visitAlphys = True
                call visitAlphys from _call_visitAlphys
        
        "Go check how Frisk is doing" if not visitFrisk:
            papyrus "FRISK IS NOT GOING TO SCHOOL"
            papyrus "POOR HUMAN IS RESTING AFTER EVERYTHING JUST HAPPENED"
            show papyrusImg coolDude delight
            papyrus "MAYBE WE CAN DO THAT TOGETHER!"
            $ visitFrisk = True
            call visitFrisk from _call_visitFrisk

return

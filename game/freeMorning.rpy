label freeMorning:
    stop music
    scene skelebroHouse outside with dissolve
    show papyrusImg coolDude happy zorder 0 at fade:
        xpos 0
    papyrus "LOOKIE THAT!"
    papyrus "I HAVE FREE THE MORNING!"
    show papyrusImg coolDude thinking
    papyrus "WHAT SHALL I DO?"
    
    call displayMenuFreeMorning from _call_displayMenuFreeMorning

    return

label displayMenuFreeMorning:
    menu:
        # Toriel
        "Go help Toriel at the School" if not helpedToriel and not giveRingToUndyne:
            show papyrusImg coolDude happy 
            papyrus "LET'S SEE IF TORIEL HAVE SOMETHING TO DO!"
            papyrus "THEY ARE STILL MOVING THINGS FROM THE UNDERGROUND AFTER ALL"
            $ helpedToriel = True
            call torielSchool from _call_torielSchool
        "Go help Toriel with something she needs" if not helpedToriel and giveRingToUndyne:
            $ helpedToriel = True
            $ visitSans = True
            $ weddingFrom = 'toriel'
            call weddingTorielSans

        # Asgore
        "Go grocery shopping" if not metAsgore and not giveRingToUndyne:
            papyrus "I'LL BETTER GO TO GET SOME GROCERIES"
            papyrus "MAYBE I CAN FIND SOME DISCOUNTS ON THE SPIDER BAKERY"
            papyrus "EVERYTHING IS ALWAYS SO EXPENSIVE"
            $ metAsgore = True
            call groceryShopping from _call_groceryShopping
        "I never know where the King is in the mornings" if not metAsgore and giveRingToUndyne:
            $ metAsgore = True
            $ visitFrisk = True
        
        # Sans
        "Go check Sans" if not visitSans and not giveRingToUndyne:
            papyrus "MAYBE I SHOULD CHECK WHAT SANS IS DOING"
            $ visitSans = True
            call checkSans from _call_checkSans
        "Sans is not at his work post, I know it!" if not visitSans and giveRingToUndyne:
            $ helpedToriel = True
            $ visitSans = True
            $ weddingFrom = 'sans'
            call weddingTorielSans

        "Go check with Undyne" if not visitUndyne:
            papyrus "I SHOULD CHECK OUT WITH UNDYNE"
            show papyrusImg coolDude delight
            papyrus "I HAVE A SURPRISE FOR HER AND I DON'T WANT TO FORGET!"
            $ visitUndyne = True
            $ giveRingToUndyne = True
            call visitUndyne from _call_visitUndyne
        
        "Go visit Dr. Alphys" if not visitAlphys:
            if penAtAlphys:
                show papyrusImg coolDude thinking
                papyrus "I LEFT THE IMPORTANT MISSION TO DR ALPHYS LAST NIGHT"
                papyrus "I DON'T KNOW IF I CAN VISIT HER, I MIGHT BOTHER HER"
                gaster "SHE MIGHT HAVE INSPIRATION ON DOING IT AND THEN WORK IN A HURRY FOR 3 HOURS STRAIGHT"
                papyrus "YOU MEAN SHE MIGHT NEED SOME REFRESTMENTS FOR AVOID DEHYDRATION?"
                gaster "I DON'T THINK SO"
                gaster "SHE LOOKED MORE LIKE THE NOCTURNAL TYPE"
                show papyrusImg coolDude explaining
                papyrus "YOU RIGHT"
                papyrus "SHE PROBABLY HAD ALREADY DONE ALL THE WORK"
                papyrus "AND SHE'S SLEEPING RIGHT NOW"
                gaster "I'LL RECOMMEND VISIT SOMEONE ELSE"
                show papyrusImg coolDude delight
                papyrus "THAT'S A GOOD IDEA"
                call displayMenuFreeMorning from _call_displayMenuFreeMorning_1
            else:
                $ giveRingToUndyne = False
                $ visitAlphys = True
                call visitAlphys from _call_visitAlphys
        
        "Go check how Frisk is doing" if not visitFrisk and not giveRingToUndyne:
            papyrus "FRISK IS NOT GOING TO SCHOOL"
            papyrus "POOR HUMAN IS RESTING AFTER EVERYTHING JUST HAPPENED"
            show papyrusImg coolDude delight
            papyrus "MAYBE WE CAN DO THAT TOGETHER!"
            $ visitFrisk = True
            call visitFrisk from _call_visitFrisk

        "Let's see where Frisk is" if not visitFrisk and giveRingToUndyne:
            $ metAsgore = True
            $ visitFrisk = True

    return
    

label displayMenuFreeAfternoon:
    menu:
        # Toriel
        "I have a question fand Toriel" if not helpedToriel and not giveRingToUndyne:
            call afternoonToriel from _call_afternoonToriel
            $ helpedToriel = True
        "Go help Toriel with something she needs" if not helpedToriel and giveRingToUndyne:
            $ helpedToriel = True
            $ visitSans = True
            $ weddingFrom = 'toriel'
            call weddingTorielSans

        "Maybe Asgore can help me with this" if not metAsgore and not giveRingToUndyne:
            call afternoonAsgore from _call_afternoonAsgore
            $ metAsgore = True
            
        # Sans
        "Maybe Sans needs something" if not visitSans and not giveRingToUndyne:
            call afternoonSans from _call_afternoonSans
            $ visitSans = True
        "Sans is not at his work post, I know it!" if not visitSans and giveRingToUndyne:
            $ helpedToriel = True
            $ visitSans = True
            $ weddingFrom = 'sans'
            call weddingTorielSans

        "Maybe I should check with Undyne" if not visitUndyne and not giveRingToUndyne:
            call afternoonUndyne from _call_afternoonUndyne
            $ visitUndyne = True
        
        "I want to visit Dr. Alphys..." if not visitAlphys:
            if penAtAlphys:
                show papyrusImg coolDude thinking
                papyrus "I LEFT THE IMPORTANT MISSION TO DR ALPHYS LAST NIGHT"
                papyrus "I DON'T KNOW IF I CAN VISIT HER, I MIGHT BOTHER HER"
                gaster "SHE MIGHT HAVE INSPIRATION ON DOING IT AND THEN WORK IN A HURRY FOR 3 HOURS STRAIGHT"
                papyrus "YOU MEAN SHE MIGHT NEED SOME REFRESTMENTS FOR AVOID DEHYDRATION?"
                gaster "I DON'T THINK SO"
                gaster "SHE LOOKED MORE LIKE THE NOCTURNAL TYPE"
                show papyrusImg coolDude explaining
                papyrus "YOU RIGHT"
                papyrus "SHE PROBABLY HAD ALREADY DONE ALL THE WORK"
                papyrus "AND SHE'S SLEEPING RIGHT NOW"
                gaster "I'LL RECOMMEND VISIT SOMEONE ELSE"
                show papyrusImg coolDude delight
                papyrus "THAT'S A GOOD IDEA"
                call displayMenuFreeAfternoon from _call_displayMenuFreeAfternoon
            else:
                $ giveRingToUndyne = False
                call afternoonAlphys from _call_afternoonAlphys
                $ visitAlphys = True
        
        "Let's checkout how Frisk is doing" if not visitFrisk and not giveRingToUndyne:
            papyrus "FRISK IS NOT GOING TO SCHOOL"
            papyrus "POOR HUMAN IS RESTING AFTER EVERYTHING JUST HAPPENED"
            show papyrusImg coolDude delight
            papyrus "MAYBE WE CAN DO THAT TOGETHER!"
            $ visitFrisk = True
            call visitFrisk from _call_visitFrisk_1

    return

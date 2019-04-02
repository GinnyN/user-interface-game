label freeMorning:
    stop music
    scene skelebroHouse outside with dissolve
    show papyrusImg coolDude happy zorder 0 at fade:
        xpos 0
    papyrus "LOOKIE THAT!"
    papyrus "I HAVE FREE THE MORNING!"
    show papyrusImg coolDude thinking
    papyrus "WHAT SHALL I DO?"

    menu:
        "Go help Toriel at the School" if not helpedToriel:
            show papyrusImg coolDude happy 
            papyrus "LET'S SEE IF TORIEL HAVE SOMETHING TO DO!"
            papyrus "THEY ARE STILL MOVING THINGS FROM THE UNDERGROUND AFTER ALL"
            $ helpedToriel = True
            call torielSchool

        "Go grocery shopping" if not metAsgore:
            papyrus "I'LL BETTER GO TO GET SOME GROCERIES"
            papyrus "MAYBE I CAN FIND SOME DISCOUNTS ON THE SPIDER BAKERY"
            papyrus "EVERYTHING IS ALWAYS SO EXPENSIVE"
            $ metAsgore = True
            call groceryShopping
            
        "Go check Sans" if not visitSans:
            papyrus "MAYBE I SHOULD CHECK WHAT SANS IS DOING"
            $ visitSans = True
            call checkSans

        "Go check with Undyne" if not visitUndyne:
            papyrus "I SHOULD CHECK OUT WITH UNDYNE"
            show papyrusImg coolDude delight
            papyrus "I HAVE A SURPRISE FOR HER AND I DON'T WANT TO FORGET!"
            $ visitUndyne = True
            call visitUndyne
        
        "Go visit Alphys at the New Lab" if not visitAlphys:
            papyrus "I HEARD DR ALPHYS IS WORKING ON SOMETHING NEW"
            papyrus "MAYBE IS A NEW KIND OF PUZZLE!"
            papyrus "OK, MAYBE NOT"
            papyrus "BUT SHOULD BE INTERESTING!"
            $ visitAlphys = True
            call visitAlphys
        
        "Go check how Frisk is doing" if not visitFrisk:
            papyrus "FRISK IS NOT GOING TO SCHOOL"
            papyrus "POOR HUMAN IS RESTING AFTER EVERYTHING JUST HAPPENED"
            papyrus "MAYBE WE CAN DO THAT TOGETHER!"
            $ visitFrisk = True
            call visitFrisk

return

label freeMorning:
    stop music
    scene skelebroHouse outside with dissolve
    show papyrusImg coolDude happy zorder 0 at fade:
        xpos 0
    papyrus "LOOKIE THAT!"
    papyrus "I HAVE FREE THE MORNING!"
    show papyrusImg coolDude thinking
    papyrus "WHAT SHALL I DO?"
    
    jump displayMenuFreeMorning

    return

label displayMenuFreeMorning:
    if giveRingToUndyne:
        menu:
            #Toriel
            "Go help Toriel with something she needs" if not helpedToriel:
                $ helpedToriel = True
                $ visitSans = True
                $ weddingFrom = 'toriel'
                call weddingTorielSans
            #Asgore
            "I never know where the King is in the mornings" if not metAsgore:
                $ weddingFrom = 'asgore'
                call weddingFriskAsgore
                $ metAsgore = True
                $ visitFrisk = True
            #Sans
            "Sans is not at his work post, I know it!" if not visitSans:
                $ helpedToriel = True
                $ visitSans = True
                $ weddingFrom = 'sans'
                call weddingTorielSans
            #Alphys
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
                    call displayMenuFreeAfternoon
                else:
                    $ giveRingToUndyne = False
                    call visitAlphys from _call_visitAlphys
                    $ visitAlphys = True
            #Frisk
            "Let's see where Frisk is" if not visitFrisk:
                $ metAsgore = True
                $ visitFrisk = True
                $ weddingFrom = 'frisk'
                call weddingFriskAsgore
            
            #Mettaton
            "Let's call to Mettaton's number" if mettatonFreeMorning and not metMettaton:
                show papyrusImg coolDude delight
                papyrus "LET'S CALL METTATON'S NUMBER!"
                gaster "DON'T DO THAT"
                gaster "THAT'S A BAD IDEA"
                play sound "music/fx/telephone_ring.wav"
                pause(0.5)
                "Phone" "* Ring ring! *"
                show papyrusImg coolDude thinking
                papyrus "MAYBE HE'S BUSY"
                gaster "HOPEFULLY PERMANENTLY"
                "Phone" "* click *"
                phone "You have called to a very personal number, if you have obtained this number ilegally, we will found you and we will destroy you"
                show papyrusImg coolDude uhh
                papyrus "DID I THOUGH?"
                gaster "..."
                gaster "YES"
                show papyrusImg coolDude delight
                papyrus "NO I DIDN'T"
                phone "If you have not, please stay in line"
                "Phone" "* click *"
                show papyrusImg coolDude uhh
                phone "Right now Mettaton cannot talk with you"
                phone "He's getting prepared for his first human tour and of course he's very busy"
                phone "Thanks for calling"
                phone "He will contact you eventually after the tour"
                phone "Except if you are an illegal caller"
                phone "You must be dead by now"
                "Phone" "* click *"
                show papyrusImg coolDude neutral
                papyrus "I WASN'T ILLEGAL AFTER ALL"
                gaster "YOU SHOULDN'T RISK THAT AGAIN"
                papyrus "BUT HE'S BUSY, LET'S SEE SOMEONE ELSE"
                jump displayMenuFreeAfternoon
    else:
        menu:
            # Toriel
            "Go help Toriel at the School" if not helpedToriel and not askTorielWekufe:
                show papyrusImg coolDude happy 
                papyrus "LET'S SEE IF TORIEL HAVE SOMETHING TO DO!"
                papyrus "THEY ARE STILL MOVING THINGS FROM THE UNDERGROUND AFTER ALL"
                $ helpedToriel = True
                call torielSchool from _call_torielSchool
            "I need to ask Toriel this but I don't really wanna" if not helpedToriel and askTorielWekufe:
                call torielWekufeQuestion
                $ helpedToriel = True
                $ askTorielWekufe = True

            # Asgore
            "Go grocery shopping" if not metAsgore and not giveRingToUndyne:
                papyrus "I'LL BETTER GO TO GET SOME GROCERIES"
                papyrus "MAYBE I CAN FIND SOME DISCOUNTS ON THE SPIDER BAKERY"
                papyrus "EVERYTHING IS ALWAYS SO EXPENSIVE"
                $ metAsgore = True
                call groceryShopping from _call_groceryShopping
            
            # Sans
            "Go check Sans" if not visitSans and not giveRingToUndyne:
                papyrus "MAYBE I SHOULD CHECK WHAT SANS IS DOING"
                $ visitSans = True
                call checkSans from _call_checkSans

            "Go check with Undyne" if not visitUndyne:
                papyrus "I SHOULD CHECK OUT WITH UNDYNE"
                show papyrusImg coolDude delight
                papyrus "I HAVE A SURPRISE FOR HER AND I DON'T WANT TO FORGET!"
                $ visitUndyne = True
                if day < 3:
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
                    jump displayMenuFreeMorning
                else:
                    $ giveRingToUndyne = False
                    $ visitAlphys = True
                    call visitAlphys
            
            # Frisk
            "Go check how Frisk is doing" if not visitFrisk and not giveRingToUndyne:
                papyrus "FRISK IS NOT GOING TO SCHOOL"
                papyrus "POOR HUMAN IS RESTING AFTER EVERYTHING JUST HAPPENED"
                show papyrusImg coolDude delight
                papyrus "MAYBE WE CAN DO THAT TOGETHER!"
                $ visitFrisk = True
                call visitFrisk from _call_visitFrisk

            # Mettaton 
            "Let's call to Mettaton's number" if mettatonFreeMorning and not metMettaton:
                if day == 3 or giveRingToUndyne:
                    show papyrusImg coolDude delight
                    papyrus "LET'S CALL METTATON'S NUMBER!"
                    gaster "DON'T DO THAT"
                    gaster "THAT'S A BAD IDEA"
                    play sound "music/fx/telephone_ring.wav"
                    "Phone" "* Ring ring! *"
                    show papyrusImg coolDude thinking
                    papyrus "MAYBE HE'S BUSY"
                    gaster "HOPEFULLY PERMANENTLY"
                    "Phone" "* click *"
                    phone "You have called to a very personal number, if you have obtained this number ilegally, we will found you and we will destroy you"
                    show papyrusImg coolDude uhh
                    papyrus "DID I THOUGH?"
                    gaster "..."
                    gaster "YES"
                    show papyrusImg coolDude delight
                    papyrus "NO I DIDN'T"
                    phone "If you have not, please stay in line"
                    "Phone" "* click *"
                    show papyrusImg coolDude uhh
                    phone "Right now Mettaton cannot talk with you"
                    phone "He's getting prepared for his first human tour and of course he's very busy"
                    phone "Thanks for calling"
                    phone "He will contact you eventually after the tour"
                    phone "Except if you are an illegal caller"
                    phone "You must be dead by now"
                    "Phone" "* click *"
                    show papyrusImg coolDude neutral
                    papyrus "I WASN'T ILLEGAL AFTER ALL"
                    gaster "YOU SHOULDN'T RISK THAT AGAIN"
                    papyrus "BUT HE'S BUSY, LET'S SEE SOMEONE ELSE"
                    jump displayMenuFreeMorning
                else:
                    $ metMettaton = True
                    call visitMettaton from _call_visitMettaton
        
        if giveRingToUndyne and day == 3:
            call afterMorning from _call_afterMorning
            call weddingFinal from _call_weddingFinal
        return
    

label displayMenuFreeAfternoon:
    if giveRingToUndyne:
        menu:
            #Toriel
            "Go help Toriel with something she needs" if not helpedToriel:
                $ helpedToriel = True
                $ visitSans = True
                $ weddingFrom = 'toriel'
                call weddingTorielSans from _call_weddingTorielSans_2
            #Asgore
            "I think the king said something about my topiary I guess" if not metAsgore:
                $ weddingFrom = 'asgore'
                call weddingFriskAsgore from _call_weddingFriskAsgore_2
                $ metAsgore = True
                $ visitFrisk = True
            #Sans
            "Sans is not at his work post, I know it!" if not visitSans:
                $ helpedToriel = True
                $ visitSans = True
                $ weddingFrom = 'sans'
                call weddingTorielSans from _call_weddingTorielSans_3
            #Alphys
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
                    call displayMenuFreeAfternoon
                else:
                    $ giveRingToUndyne = False
                    call afternoonAlphys from _call_afternoonAlphys
                    $ visitAlphys = True
            #Frisk
            "Let's see where Frisk is" if not visitFrisk:
                $ metAsgore = True
                $ visitFrisk = True
                $ weddingFrom = 'frisk'
                call weddingFriskAsgore from _call_weddingFriskAsgore_3
            
            #Mettaton
            "Let's call to Mettaton's number" if mettatonFreeMorning and not metMettaton:
                show papyrusImg coolDude delight
                papyrus "LET'S CALL METTATON'S NUMBER!"
                gaster "DON'T DO THAT"
                gaster "THAT'S A BAD IDEA"
                play sound "music/fx/telephone_ring.wav"
                pause(0.5)
                "Phone" "* Ring ring! *"
                show papyrusImg coolDude thinking
                papyrus "MAYBE HE'S BUSY"
                gaster "HOPEFULLY PERMANENTLY"
                "Phone" "* click *"
                phone "You have called to a very personal number, if you have obtained this number ilegally, we will found you and we will destroy you"
                show papyrusImg coolDude uhh
                papyrus "DID I THOUGH?"
                gaster "..."
                gaster "YES"
                show papyrusImg coolDude delight
                papyrus "NO I DIDN'T"
                phone "If you have not, please stay in line"
                "Phone" "* click *"
                show papyrusImg coolDude uhh
                phone "Right now Mettaton cannot talk with you"
                phone "He's getting prepared for his first human tour and of course he's very busy"
                phone "Thanks for calling"
                phone "He will contact you eventually after the tour"
                phone "Except if you are an illegal caller"
                phone "You must be dead by now"
                "Phone" "* click *"
                show papyrusImg coolDude neutral
                papyrus "I WASN'T ILLEGAL AFTER ALL"
                gaster "YOU SHOULDN'T RISK THAT AGAIN"
                papyrus "BUT HE'S BUSY, LET'S SEE SOMEONE ELSE"
                jump displayMenuFreeAfternoon

    else:
        menu:
            # Toriel
            "I have a question for Toriel" if not helpedToriel and not askTorielWekufe:
                call afternoonToriel from _call_afternoonToriel
                $ helpedToriel = True
            "I need to ask Toriel this but I don't really wanna" if not helpedToriel and askTorielWekufe:
                call torielWekufeQuestion
                $ helpedToriel = True
                $ visitSans = True
                $ askTorielWekufe = False
            

            # Asgore
            "Maybe Asgore can help me with this" if not metAsgore and not giveRingToUndyne:
                call afternoonAsgore from _call_afternoonAsgore
                $ metAsgore = True
            
                
            # Sans
            "Maybe Sans needs something" if not visitSans and not giveRingToUndyne:
                call afternoonSans from _call_afternoonSans
                $ visitSans = True
            

            # Undyne
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
                    call displayMenuFreeAfternoon
                else:
                    $ giveRingToUndyne = False
                    call afternoonAlphys
                    $ visitAlphys = True
            
            # Frisk
            "Let's checkout how Frisk is doing" if not visitFrisk and not giveRingToUndyne:
                papyrus "FRISK IS NOT GOING TO SCHOOL"
                papyrus "POOR HUMAN IS RESTING AFTER EVERYTHING JUST HAPPENED"
                show papyrusImg coolDude delight
                papyrus "MAYBE WE CAN DO THAT TOGETHER!"
                $ visitFrisk = True
                call visitFrisk from _call_visitFrisk_1

            # Mettaton 
            "Let's call to Mettaton's number" if mettatonFreeMorning and not metMettaton:
                if day == 3 or giveRingToUndyne:
                    show papyrusImg coolDude delight
                    papyrus "LET'S CALL METTATON'S NUMBER!"
                    gaster "DON'T DO THAT"
                    gaster "THAT'S A BAD IDEA"
                    play sound "music/fx/telephone_ring.wav"
                    pause(0.5)
                    "Phone" "* Ring ring! *"
                    show papyrusImg coolDude thinking
                    papyrus "MAYBE HE'S BUSY"
                    gaster "HOPEFULLY PERMANENTLY"
                    "Phone" "* click *"
                    phone "You have called to a very personal number, if you have obtained this number ilegally, we will found you and we will destroy you"
                    show papyrusImg coolDude uhh
                    papyrus "DID I THOUGH?"
                    gaster "..."
                    gaster "YES"
                    show papyrusImg coolDude delight
                    papyrus "NO I DIDN'T"
                    phone "If you have not, please stay in line"
                    "Phone" "* click *"
                    show papyrusImg coolDude uhh
                    phone "Right now Mettaton cannot talk with you"
                    phone "He's getting prepared for his first human tour and of course he's very busy"
                    phone "Thanks for calling"
                    phone "He will contact you eventually after the tour"
                    phone "Except if you are an illegal caller"
                    phone "You must be dead by now"
                    "Phone" "* click *"
                    show papyrusImg coolDude neutral
                    papyrus "I WASN'T ILLEGAL AFTER ALL"
                    gaster "YOU SHOULDN'T RISK THAT AGAIN"
                    papyrus "BUT HE'S BUSY, LET'S SEE SOMEONE ELSE"
                    jump displayMenuFreeMorning
                else:
                    $ metMettaton = True
                    call visitMettaton from _call_visitMettaton_1
        if giveRingToUndyne:
            call afterAfternoon from _call_afterAfternoon
        return

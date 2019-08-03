label schoolPapyrusRun:
    scene black with dissolve
    pause(1.0)
    scene skelebroHouse outside with dissolve
    pause 0.5
    show studentImg dog gossiping flip zorder 2 at fade:
        xalign 0.7 yalign 1.0
    show kidImg listening zorder 3 at fade:
        xalign 0.3 yalign 1.0
    "Student" "* Did you heard that?"
    "Student" "* The teacher said we'll not meet with Papyrus today!"
    show studentImg dog scared flip:
        xalign 0.8
    show kidImg angry at fade
    monsterKid "No sense!"
    monsterKid "Papyrus never miss his morning run!"
    monsterKid "He's as cool as that!"
    show studentImg dog happy at fade
    show kidImg happy at fade
    show papyrusImg coolDude neutral flip zorder 1 at fade:
        xpos 0.4
    play music "music/16 Nyeh Heh Heh!.mp3" fadein(1)
    papyrus "HI KIDS!"
    show papyrusImg coolDude checkThis flip
    papyrus "THE GREAT PAPYRUS HAS ARRIVED!"
    monsterKid "Papyrus!"
    papyrus "DON'T STOP MOVING!"
    papyrus "YOU DON'T WANNA ANGER YOUR TEACHER!"
    show undyneImg gym bored at fade:
        xalign 0.0 yalign 1.0
    undyne "And what's Toriel told you!?"
    show papyrusImg coolDude scared flip at fade
    show studentImg dog surprised flip at fade:
        xalign 1.0 yalign 1.0
    show kidImg scared flip at fade:
        xalign 1.2 yalign 1.0
    papyrus "UNDYNE!"
    show studentImg dog scared flip
    show kidImg hiding flip
    show papyrusImg coolDude annoyed flip at fade
    show undyneImg gym bored at fade
    undyne "Move along kids, I need to talk with 'The Great Papyrus'"
    hide studentImg
    hide kidImg
    papyrus "I'M DOING WHAT TORIEL TOLD ME"
    undyne "You are keeping your rutine Papyrus"
    undyne "You need to rest!"
    show papyrusImg coolDude explaining flip at fade
    papyrus "BUT KEEPING WITH MY RUTINE IS RELAXING TO ME!"
    show undyneImg gym yelling at fade
    undyne "That's the opposite of a vacation Papyrus"
    show papyrusImg coolDude angry flip at fade
    papyrus "BUT I DON'T TAKE VACATIONS!"
    show undyneImg gym frustrated at fade
    undyne "BUT NOW YOU SHOULD! AND IT'S TORIEL'S ADVICE!"
    show papyrusImg coolDude explaining flip at fade
    papyrus "BUT.."
    papyrus "I LIKE TO BE WITH THE KIDS"
    undyne "And I..."
    show undyneImg gym shy at fade
    undyne "..."
    show papyrusImg coolDude annoyed flip at fade
    papyrus "WHAT?!"
    stop music
    undyne "I don't want you to be with them"
    undyne "Not during this week at least"
    show papyrusImg coolDude speakless flip at fade
    papyrus "UNDYNE..."
    show undyneImg gym frustrated at fade
    undyne "Now, go to marathon Metaton's... "
    show undyneImg gym shy at fade
    extend "whatever is called now"
    show undyneImg gym frustrated at fade

    undyne "NOW GO!"
    hide undyneImg
    papyrus "..."
    hide papyrusImg
    return
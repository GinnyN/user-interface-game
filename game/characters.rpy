# Declare characters used by this game.
define papyrus = Character("Papyrus", color="#0000FF", what_prefix="{font=fonts/Papyrus.ttf} ", what_suffix="{/font}")
define frisk = Character("Frisk", color="#FF0000", what_prefix="* ", what_suffix=" *")
define sans = Character("Sans", color="#0000FF", what_prefix="*{font=fonts/Comic Sans MS.ttf} ", what_suffix=".{/font}")
define dtSans = Character("Sans", color="#0000FF", what_prefix="* ", what_suffix=".")
define gaster = Character("W.D. Gaster", color="#0000FF", what_prefix="{font=fonts/NewAster.ttf} ", what_suffix=".{/font}")
define text = Character("Text", color="#0000FF", what_prefix="{font=fonts/NewAster.ttf} ", what_suffix=".{/font}")
define undyne = Character("Undyne", color="#00FF00", what_prefix="* ")
define toriel = Character("Toriel", color="#FF0000", what_prefix="* ")
define asgore = Character("Asgore", color="#FF0000", what_prefix="* ")
define alphys = Character("Alphys", color="#FFFF00", what_prefix="* ")
define metatton = Character("Metatton", color="#FFFF00", what_prefix="* ")

define monsterKid = Character("Kid", color="#AAAA00", what_prefix="* ")
define grillsby = Character("Grillsby", color="#FFAA00", what_prefix="* ")
define dogamy = Character("Dogamy", color="#8888FF", what_prefix="* ")
define dogaressa = Character("Dogaressa", color="#FF8888", what_prefix="* (", what_suffix=")")
define muffet = Character("Muffet", color="#FF6666", what_prefix="* ")

define cuero = Character("Monster 1", what_prefix="* ")
define coo = Character("Monster 2", what_prefix="* ")

define narrator = Character(' ', color="#ffffff")

label changeWekufe:
    $ cuero = Character("Cuero", what_prefix="* ")
    $ coo = Character("Coo", what_prefix="* ")
return 

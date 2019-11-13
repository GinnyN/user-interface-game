init python:
    def papyrus_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("music/voice/talk_papyrus.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()
    
    def toriel_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("music/voice/talk_toriel.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()
    
    def gaster_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("music/voice/talk_gaster.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

    def sans_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("music/voice/talk_sans.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()
    
    def undyne_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("music/voice/talk_undyne.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

    def alphys_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("music/voice/talk_alphys.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

    def asgore_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("music/voice/talk_asgore.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()
    
    def mettaton_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("music/voice/talk_mettaton.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()
    
    def default_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("music/voice/talk_default.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

    def dogamy_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("music/voice/talk_default.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()
    
    def narrator_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            try:
                if renpy.persistent.endingGaster:
                    renpy.sound.play("music/voice/talk_gaster.wav", loop=True)
            except:
                try:
                    if renpy.persistent.endingPapyrus:
                        renpy.sound.play("music/voice/talk_papyrus.wav", loop=True)
                except:  
                    renpy.sound.play("music/voice/talk_default.wav", loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

# Declare characters used by this game.
define papyrus = Character("Papyrus", color="#0000FF", what_prefix="{font=fonts/Papyrus.ttf} ", what_suffix="{/font}", callback=papyrus_voice)
define frisk = Character("Frisk", color="#FF0000", what_prefix="* ", what_suffix=" *")
define sans = Character("Sans", color="#0000FF", what_prefix="*{font=fonts/Comic Sans MS.ttf} ", what_suffix=".{/font}", callback=sans_voice)
define dtSans = Character("Sans", color="#0000FF", what_prefix="* ", what_suffix=".", callback=sans_voice)
define gaster = Character("W.D. Gaster", color="#0000FF", what_prefix="{font=fonts/NewAster.ttf} ", what_suffix=".{/font}", callback=gaster_voice)
define text = Character("Text", color="#0000FF", what_prefix="{font=fonts/NewAster.ttf} ", what_suffix=".{/font}", callback=gaster_voice)
define undyne = Character("Undyne", color="#00FF00", what_prefix="* ", callback=undyne_voice)
define toriel = Character("Toriel", color="#FF0000", what_prefix="* ", callback=toriel_voice)
define asgore = Character("Asgore", color="#FF0000", what_prefix="* ", callback=asgore_voice)
define alphys = Character("Alphys", color="#FFFF00", what_prefix="* ", callback=alphys_voice)
define metatton = Character("Metatton", color="#FFFF00", what_prefix="* ", callback=mettaton_voice)

define monsterKid = Character("Kid", color="#AAAA00", what_prefix="* ", callback=default_voice)
define grillsby = Character("Grillsby", color="#FFAA00", what_prefix="* ", callback=default_voice)
define dogamy = Character("Dogamy", color="#8888FF", what_prefix="* ", callback=default_voice)
define dogaressa = Character("Dogaressa", color="#FF8888", what_prefix="* (", what_suffix=")", callback=default_voice)
define muffet = Character("Muffet", color="#FF6666", what_prefix="* ", callback=default_voice)

define cuero = Character("Monster 1", what_prefix="* ", callback=default_voice)
define coo = Character("Monster 2", what_prefix="* ", callback=default_voice)
define invunche = Character("Random Goon", what_prefix="* ", callback=default_voice)
define voladora = Character("Random Goon 2", what_prefix="* ", callback=default_voice)
define trauco = Character("Boss", what_prefix="* ", callback=default_voice)

define narrator = Character(' ', color="#ffffff", callback=narrator_voice)

label changeWekufe:
    $ cuero = Character("Cuero", what_prefix="* ", callback=default_voice)
    $ coo = Character("Coo", what_prefix="* ", callback=default_voice)
    $ invunche = Character("Invunche", what_prefix="* ", callback=default_voice)
    $ voladora = Character("Voladora", what_prefix="* ", callback=default_voice)
    $ trauco = Character("Trauco", what_prefix="* ", callback=default_voice)
return 

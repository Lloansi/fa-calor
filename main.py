def on_forever():
    if input.temperature() >= 22:
        basic.show_string("CALOR")
    else:
        basic.show_string("FRED")
    if input.light_level() >= 200:
        music.stop_melody(MelodyStopOptions.ALL)
        music.play(music.string_playable("G B A G C5 B A B ", 120),
            music.PlaybackMode.UNTIL_DONE)
    elif input.light_level() < 50:
        music.stop_melody(MelodyStopOptions.ALL)
        music.play(music.string_playable("C5 A B G A F G E ", 120),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)

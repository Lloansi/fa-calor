basic.forever(function () {
    if (input.temperature() >= 22) {
        basic.showString("CALOR")
    } else {
        basic.showString("FRED")
    }
    if (input.lightLevel() >= 200) {
        music.stopMelody(MelodyStopOptions.All)
        music.play(music.stringPlayable("E D G F B A C5 B ", 185), music.PlaybackMode.UntilDone)
    } else if (input.lightLevel() <= 50) {
        music.stopMelody(MelodyStopOptions.All)
        music.play(music.stringPlayable("A F E F D G E F ", 185), music.PlaybackMode.UntilDone)
    }
})

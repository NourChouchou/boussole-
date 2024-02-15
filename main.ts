let Degré = 0
basic.forever(function () {
    Degré = input.compassHeading()
    if (Degré > 45 && Degré < 135) {
        basic.showString("E")
    } else if (Degré > 135 && Degré < 225) {
        basic.showString("S")
    } else if (Degré > 225 && Degré < 315) {
        basic.showString("O")
    } else {
        basic.showString("N")
    }
})

Degré = 0

def on_forever():
    global Degré
    Degré = input.compass_heading()
    if Degré > 45 and Degré < 135:
        basic.show_string("E")
    elif Degré > 135 and Degré < 225:
        basic.show_string("S")
    elif Degré > 225 and Degré < 315:
        basic.show_string("O")
    else:
        basic.show_string("N")
basic.forever(on_forever)

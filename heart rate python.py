def on_pulsed_c16_high():
    global beats
    beats += 1
    if sekunden != 0:
        basic.show_leds("""
            . # . # .
            # # # # #
            # # # # #
            . # # # .
            . . # . .
            """)
        basic.pause(25)
        basic.clear_screen()
pins.on_pulsed(DigitalPin.C16, PulseValue.HIGH, on_pulsed_c16_high)

beats = 0
sekunden = 0
sekunden = 0

def on_forever():
    global sekunden, beats
    basic.pause(1000)
    sekunden += 1
    if sekunden == 15:
        sekunden = 0
        basic.show_number(beats * 4)
        beats = 0
basic.forever(on_forever)

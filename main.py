def on_button_pressed_a():
    global direction
    direction += 1
    pins.digital_write_pin(DigitalPin.P1, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P1, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

direction = 0
delay = 0.25

def on_forever():
    while True:
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.pause(delay)
        pins.digital_write_pin(DigitalPin.P0, 0)
        basic.pause(delay)
basic.forever(on_forever)

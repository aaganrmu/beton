import board
import digitalio
import time
from ledz.ledz import Ledz


# setup pixel array
pin = board.GP29 # Final value I guess
rows = 1         # will be 2
columns = 8      # will be 32
leds = Ledz(rows,columns,pin,brightness=1)

# setup controller
control_pins= [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7]
controlls = [digitalio.DigitalInOut(pin) for pin in control_pins]
for controll in controlls:
    controll.direction = digitalio.Direction.INPUT
    controll.pull = digitalio.Pull.UP



old_value = 0
# Main loop
while True:
    time.sleep(0.1)
    value = 0
    for controll in controlls:
        value |= (not controll.value) << controlls.index(controll)
    if value == old_value:
        continue
    old_value = value
    print(value)
    leds.fill((value, value, value))
    leds.show()
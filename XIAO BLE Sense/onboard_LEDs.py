import time
import board
import digitalio

blue = digitalio.DigitalInOut(board.BLUE_LED)
red = digitalio.DigitalInOut(board.RED_LED)
green = digitalio.DigitalInOut(board.GREEN_LED)

blue.direction = digitalio.Direction.OUTPUT
red.direction = digitalio.Direction.OUTPUT
green.direction = digitalio.Direction.OUTPUT

print(dir(board))

while True:
    red.value = True
    time.sleep(0.1)
    red.value = False
    blue.value = True
    time.sleep(0.1)
    blue.value = False
    # time.sleep(0.1)
    green.value = True
    time.sleep(0.1)
    green.value = False
    time.sleep(0.1)
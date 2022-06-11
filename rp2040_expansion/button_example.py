import time
import board
from digitalio import DigitalInOut,Direction,Pull

btn = DigitalInOut(board.D1)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

while True:
    if not btn.value:
        print("btn is down")
    else:
        print("btn is up")
        pass
    time.sleep(0.1)
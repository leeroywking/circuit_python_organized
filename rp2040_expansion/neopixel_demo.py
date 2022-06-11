# Write your code here :-)
import time
import board
import digitalio
import neopixel

led_blue = digitalio.DigitalInOut(board.LED_BLUE)
led_red = digitalio.DigitalInOut(board.LED_RED)
led_green = digitalio.DigitalInOut(board.LED_GREEN)
leds = [led_blue,led_red,led_green]

pixel_pin = board.NEOPIXEL #The neopixel can be accessed in this way
num_pixels = 1 #only one pixel

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)


def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)


for led in leds:
    led.direction = digitalio.Direction.OUTPUT

while True:
    for _ in range(10):
        for led in leds:
            led.value = True
            time.sleep(0.2)
            led.value = False
    time.sleep(1)
    print("ran 5 chase loops")


    color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    color_chase(YELLOW, 0.1)
    color_chase(GREEN, 0.1)
    color_chase(CYAN, 0.1)
    color_chase(BLUE, 0.1)
    color_chase(PURPLE, 0.1)
    pixels[0] = (0,0,0)
    pixels.show()
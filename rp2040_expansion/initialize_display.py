import board
import busio
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label

displayio.release_displays()
i2c = busio.I2C (scl=board.SCL, sda=board.SDA)

display_bus = displayio.I2CDisplay (i2c, device_address = 0x3C) # The address of my Board

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
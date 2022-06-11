import alarm
import board
import digitalio
import neopixel
import time
# from buzzer_music import play_song,song4
# On MagTag, enable power to NeoPixels.
# Remove these two lines on boards without board.NEOPIXEL_POWER.


import time
import displayio
import terminalio
import busio
import board
import adafruit_displayio_ssd1306
import adafruit_pcf8563

from adafruit_display_text import label

displayio.release_displays()

i2c = busio.I2C(scl=board.SCL, sda=board.SDA)

font = terminalio.FONT

display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)  # The address of my Board
rtc = adafruit_pcf8563.PCF8563(i2c)

oled = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
count = 0
while count < 10:
    current = rtc.datetime 
    # current = time.struct_time((2022,5,28,14,40,20,6,148,1))

    hour = current.tm_hour % 12
    if hour == 0:
        hour = 12

    am_pm = "AM"
    if current.tm_hour / 12 >= 1:
        am_pm = "PM"

    time_display = "{:d}:{:02d}:{:02d} {}".format(hour, current.tm_min, current.tm_sec, am_pm)
    date_display = "{:d}/{:d}/{:d}".format(current.tm_mon, current.tm_mday, current.tm_year)
    text_display = "CircuitPython Time"

    clock = label.Label(font, text=time_display)
    date = label.Label(font, text=date_display)
    text = label.Label(font, text=text_display)

    (_, _, width, _) = clock.bounding_box
    clock.x = oled.width // 2 - width // 2
    clock.y = 5

    (_, _, width, _) = date.bounding_box
    date.x = oled.width // 2 - width // 2
    date.y = 15

    (_, _, width, _) = text.bounding_box
    text.x = oled.width // 2 - width // 2
    text.y = 25

    watch_group = displayio.Group()
    watch_group.append(clock)
    watch_group.append(date)
    watch_group.append(text)

    oled.show(watch_group)
    time.sleep(1)
    count += 1




# play_song(song4)

pin_alarm = alarm.pin.PinAlarm(pin=board.D1, value=False, pull=True)

# Exit the program, and then deep sleep until the alarm wakes us.
alarm.exit_and_deep_sleep_until_alarms(pin_alarm)

# Does not return, so we never get here.
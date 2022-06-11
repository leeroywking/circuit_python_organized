import time
import board
import busio
import adafruit_pcf8563

i2c_bus = busio.I2C(board.SCL, board.SDA)
rtc = adafruit_pcf8563.PCF8563(i2c_bus)
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

# pylint: disable-msg=using-constant-test
if True:  # change to False if you don't want to set the time!

    #                     year, mon, date, hour, min, sec, wday, yday, isdst

    t = time.struct_time((2021, 12, 26, 11, 22, 0, 0, -1, -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time
    print("Setting time to:", t)  # uncomment for debugging
    rtc.datetime = t
    print()

# pylint: enable-msg=using-constant-test



# Main loop:

while True:
    if rtc.datetime_compromised:
        print("RTC unset")
    else:
        print("RTC reports time is valid")
    t = rtc.datetime

    # print(t)     # uncomment for debugging

    print(
        "{} {}/{}/{}".format(
            days[int(t.tm_wday)], t.tm_mday, t.tm_mon, t.tm_year
        )
    )
    print("{}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec))
    time.sleep(1)  # wait a second
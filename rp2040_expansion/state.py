import time
import digitalio
import neopixel
import time
import board
import simpleio
import alarm

class GlobalState:
    def __init__(self):
        pass
    
    def wake_every_10s(self, rtc):
        # rtc.datetime = time.struct_time(
        #     tm_year=2022, tm_mon=5, tm_mday=26, 
        #     tm_hour=14, tm_min=1, tm_sec=0,
        #     tm_wday=3, tm_yday=146, tm_isdst=1)
        rtc = RTC()
        rtc.datetime = time.struct_time((2022,5,26,14,1,0,3,146,1))
        while True:
            rtc.display_current_time()
            time.sleep(0.5)
            rtc.release_display()
            # rtc.release_displays()
            time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 10)
            print("going to sleep")
            alarm.light_sleep_until_alarms(time_alarm)


class OLED:
    def __init__(self):
        pass

class RTC:
    def __init__(self):
        # import time
        import displayio
        import terminalio
        import busio
        # import board
        import adafruit_displayio_ssd1306
        import adafruit_pcf8563
        from adafruit_display_text import label
        self.label = label
        displayio.release_displays()
        # self.release_displays = displayio.release_displays
        self.i2c = busio.I2C(scl=board.SCL, sda=board.SDA)
        self.font = terminalio.FONT
        self.display_bus = displayio.I2CDisplay(self.i2c, device_address=0x3C)  # The address of my Board
        self.rtc = adafruit_pcf8563.PCF8563(self.i2c)
        self.oled = adafruit_displayio_ssd1306.SSD1306(self.display_bus, width=128, height=64)
        # self.watch_group = displayio.Group()
        self.group = displayio.Group
        self.start_time = self.rtc.datetime_register

    def set_date_time_group(self,year_month_day = "2022/05/26", time = "13:23:00", zone = "PST", day_of_week=3):
        """
        This is currently broken
        """
        print(year_month_day)
        print(time)
        print(zone)
        print(day_of_week)
        [year,month,day] = year_month_day.split("/")
        [hour,minute,second] = time.split(":")
        self.rtc.rtc.datetime.tm_year = int(year)
        self.rtc.rtc.datetime.tm_mon = int(month)
        self.rtc.rtc.datetime.tm_mday = int(day)
        self.rtc.rtc.datetime.tm_hour = int(hour)
        self.rtc.rtc.datetime.tm_min = int(minute)
        self.rtc.rtc.datetime.tm_sec = int(second)
        self.rtc.rtc.datetime.tm_zone = zone
        self.rtc.rtc.datetime.tm_wday = day_of_week

    def display_current_time(self):
        while True:
            current = self.rtc.datetime
            # self.rtc.
            # print(dir(current))
            hour = current.tm_hour % 12
            if hour == 0:
                hour = 12

            am_pm = "AM"
            if current.tm_hour >= 12:
                am_pm = "PM"

            dst = ""
            if current.tm_isdst:
                dst = "DST"
            time_diff = current.tm_min - self.start_time.tm_sec
            # time_display = "{:d}:{:02d}:{:02d} {}".format(hour, current.tm_min, current.tm_sec, am_pm) # normal time
            time_display = "{:02d}:{:02d}:{:02d} {}".format(current.tm_hour, current.tm_min, current.tm_sec, dst) # military time
            date_display = "{:d}/{:d}/{:d}".format(current.tm_mon, current.tm_mday, current.tm_year)
            text_display = "CircuitPython Time"
            start_display = "Time since boot {}".format(time_diff)
            clock = self.label.Label(self.font, text=time_display)
            date = self.label.Label(self.font, text=date_display)
            text = self.label.Label(self.font, text=text_display)
            start = self.label.Label(self.font, text=start_display)

            (_, _, width, _) = clock.bounding_box
            clock.x = self.oled.width // 2 - width // 2
            clock.y = 5

            (_, _, width, _) = date.bounding_box
            date.x = self.oled.width // 2 - width // 2
            date.y = 15

            (_, _, width, _) = text.bounding_box
            text.x = self.oled.width // 2 - width // 2
            text.y = 25

            start.x = self.oled.width // 2 -width // 2
            start.y = 35

            watch_group = self.group()
            watch_group.append(clock)
            watch_group.append(date)
            watch_group.append(text)
            watch_group.append(start)
            self.oled.show(watch_group)
        
    def release_display(self):
        self.i2c.deinit()
        self.i2c.unlock()
        self.display_bus.reset()
        # self.rtc.i2c_device.sys.
        self.oled.bus.reset()





global_state = GlobalState()


global_state.wake_every_10s(RTC)



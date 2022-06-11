# Write your code here :-)
import time
import digitalio
import neopixel
import time
import board
import simpleio
from songs.note_map import note_map
from songs.realslim import song as song1
from songs.stillfly import song as song2
from songs.babysgot import song as song3
from songs.barbie import song as song4
from songs.badtouch import song as song5
from songs.benny import song as song6


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

# I'd have to add these into a different thread for now I'm leaving them out
# for led in extra_leds:
#     led.direction = digitalio.Direction.OUTPUT

# while True:
#     for _ in range(10):
#         for led in leds:
#             led.value = True
#             time.sleep(0.2)
#             led.value = False
#         for led in extra_leds:
#             led.value = True
#             time.sleep(0.2)
#             led.value = False
#     time.sleep(1)
#     print("ran 5 chase loops")




def play_note(note,durr):
    # print(f"playing frequency",note_map[note])
    simpleio.tone(board.A3, note_map[note], duration=durr)

def play_song(song):
    title = song["title"]
    print(f"\n\n\n\n\nNow playing:\n    {title}")
    bpm = song["bpm"]
    def_duration = song["duration"]
    def_octave = song["octave"]
    notes = song["notes"]
    seconds_per_whole_note = 60/bpm*4
    for note in notes:
        [duration,letter,octave,dot,sharp] = note
        if not duration:
            duration = def_duration
        true_duration = seconds_per_whole_note / int(duration)
        if dot:
            true_duration = true_duration * 1.5
        if sharp:
            letter = letter+"#"
        if not octave:
            octave = def_octave
        letter = letter + str(octave)
        if "P" in letter:
            letter = "N"
        #print("playing",letter,true_duration)
        play_note(letter,true_duration)


while True:
    songs = [song1,song2,song3,song4,song5,song6]
    for song in songs:
        play_song(song)
        time.sleep(3)


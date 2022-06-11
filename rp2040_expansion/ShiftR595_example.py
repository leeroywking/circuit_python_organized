import board
import digitalio
import time
import random


"""
The 74HC595 is a shift register that utilizing the following wiring diagram 

PINS 1-7, 15	Q0 - Q7	Output Pins
PIN 8	GND	Ground, Vss
PIN 9	Q7	Serial Out
PIN 10	MR	Master Reclear, active low
PIN 11	SH_CP	Shift register clock pin
PIN 12	ST_CP	Storage register clock pin (latch pin)
PIN 13	OE	Output enable, active low
PIN 14	DS	Serial data input
PIN 16	Vcc	Positive supply voltage

in the following order
Q1  1:[]:16 VCC (5v)
Q2  2:[]:15 Q0
Q3  3:[]:14 DS (data in)
Q4  4:[]:13 OE
Q5  5:[]:12 ST_CP (clock pin)
Q6  6:[]:11 SH_CP (latch pin)
Q7  7:[]:10 MR master reclear
GND 8:[]:9  Q7 (serial out)

"""

latchPin = digitalio.DigitalInOut(board.A0)
clockPin =  digitalio.DigitalInOut(board.A1)
dataPin = digitalio.DigitalInOut(board.A2)
serialIn = digitalio.DigitalInOut(board.A3)

latchPin.direction = digitalio.Direction.OUTPUT
clockPin.direction = digitalio.Direction.OUTPUT
dataPin.direction = digitalio.Direction.OUTPUT
serialIn.direction = digitalio.Direction.INPUT
serialIn.pull = digitalio.Pull.UP
dataPin.value = False
clockPin.value = False
latchPin.value = False

def set_bits(input_bits:list) -> None:
    # print(input_bits)
    if len(input_bits) != 8 or type(input_bits) != list:
        print("error must provide 8 input bits in a list")
        return
    for bit in input_bits:
        if bit == 1:
            dataPin.value = True
        elif bit == 0:
            dataPin.value = False
        else:
            print("Error bits must be either 0 or 1 as an integer")
            return
        clockPin.value = True
        clockPin.value = False
        dataPin.value = False
    latchPin.value = True
    latchPin.value = False


def convert_int_to_binary_list(integer):
    if integer > 255: #this is for 8 LEDs so 255 is the highest int that can be displayed 
        print("Error int was too big please use an int smaller than 255")
        return
    else:
        output = []
        output.append(1 if (integer & 1)else 0)
        output.append(1 if (integer & 2)else 0)
        output.append(1 if (integer & 4)else 0)
        output.append(1 if (integer & 8)else 0)
        output.append(1 if (integer & 16)else 0)
        output.append(1 if (integer & 32)else 0)
        output.append(1 if (integer & 64)else 0)
        output.append(1 if (integer & 128)else 0)
        return output

def display_int(integer):
    set_bits(convert_int_to_binary_list(integer))

display_int(0)

print("Checking LED system and Bit shift register for full functionality")
for i in range(256): # this will stop at 255 with all the lights illuminated
    display_int(i)
    time.sleep(0.01)

time.sleep(2)
print("Turning off lights")
display_int(0)
time.sleep(2)
# print("Turning on lights")
# display_int(255)
# time.sleep(2)



# def fill_register():
#     dataPin.value = True
#     for _ in range(8):
#         dataPin.value = not dataPin.value
#         clockPin.value = True
#         # print("output data:",serialIn.value)
#         clockPin.value = False

max_rms = 400

def light_show(rms_level):
    # print("Running light show")
    #looks like max rms level is ~400 so rms *2 // 100 ??
    if rms_level > max_rms:
        max_rms = rms_level
        print(rms_level)
    converted_rms = int(rms_level * 2 //80 +1)
    print(converted_rms)
    lights = []
    for i in range(8):
        if converted_rms > i:
            lights.append(1)
        else:
            lights.append(0)
    set_bits(lights)
    time.sleep(0.1)

def random_lightshow(on = True):
    if on:
        integer = random.randint(0,254)
        display_int(integer)
        time.sleep(0.1)
    else:
        time.sleep(0.1)
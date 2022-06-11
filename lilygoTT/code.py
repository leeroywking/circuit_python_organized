from mp3_player import music_player
import board
import digitalio
import time
import tft_config

print(dir(board))
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT


while True:    
    print("inside the while true")
    Player, song = music_player()
    # play_music()
    Player.play(song)
    while Player.playing:
        pass



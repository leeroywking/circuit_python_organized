import board
import digitalio
import time

from audiomp3 import MP3Decoder
#from audioio import AudioOut
from audiopwmio import PWMAudioOut as AudioOut
mp3 = open("./mp3_songs/funkad-32k-loop.mp3","rb")
decoder = MP3Decoder(mp3)
audio = AudioOut(left_channel = board.D6,quiescent_value=1857)



# while True:
#     audio.play(decoder)
#     print("playing", "Daft Punk: Funk Ad")
#     time.sleep(29.209) #Audio is 29.209 long experimenting to reduce pop at loop
    # audio2.play(decoder)
    # audio.stop()
    # while audio.playing:
    #     pass




def play_music():
    audio.play(decoder)
    print("playing", "Daft Punk: Funk Ad")
    time.sleep(29.209) #Audio is 29.209 long experimenting to reduce pop at loop


def music_player():
    return audio,decoder
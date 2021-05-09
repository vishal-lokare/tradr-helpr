import os
import time
import moviepy.editor as mp

import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

n = 1
f = open('counter.txt', 'w')
f.write('0')
f.close()

os.system('del *.mp4')
time.sleep(1)

# downloading the videos live 
# n = 3
# f = open('counter.txt', 'w')
# f.write('0')
# f.close()

while (n):
    f = open('counter.txt', 'r')
    for line in f:
        for character in line:
            if(character.isdigit()):
                c = character

    c = int(c) + 1
    f.close()

    f = open('counter.txt', 'w')
    f.write(f'{c}')
    f.close()
    
    print(c)
    link = 'streamlink --hls-live-edge 99999 --hls-segment-threads 5 --hls-duration 60 -o ' + f'{c}.mp4' + ' https://www.youtube.com/watch?v=Kxwrqig5UV4 360p'
    print(link)
    os.system(f'{link}')
    n = n + 1

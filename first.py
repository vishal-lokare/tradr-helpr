import os
import time
import moviepy.editor as mp

import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

n = 3
f = open('counter.txt', 'w')
f.write('0')
f.close()

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
    n = n - 1
    print(c)
    link = 'streamlink --hls-live-edge 99999 --hls-segment-threads 5 --hls-duration 60 -o ' + f'{c}.mp4' + ' https://www.youtube.com/watch?v=Kxwrqig5UV4 360p'
    print(link)
    os.system(f'{link}')

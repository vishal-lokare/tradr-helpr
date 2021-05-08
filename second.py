import time
import moviepy.editor as mp

import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
n = 3

while(n):
  time.sleep(45)
  n = n - 1

  f = open('counter.txt', 'r')
  for line in f:
    for character in line:
      if(character.isdigit()):
        c = character
  f.close()

  c = int(c) - 1

  if(c == 1):
    f = open('trans.txt', 'w')
    f.close()

  if(c>1):
    trim = mp.VideoFileClip(f'{c}.mp4').subclip(30).write_videofile(f'{c}t.mp4')

  time.sleep(2)

  if(c>1):
    mc = mp.VideoFileClip(f'{c}t.mp4')
    mc.audio.write_audiofile(f'{c}.wav')
  else:
    mc = mp.VideoFileClip(f'{c}.mp4')
    mc.audio.write_audiofile(f'{c}.wav')
  #wav file done

  # speech to text
  path = f'{c}.wav'
  r = sr.Recognizer()

  sound = AudioSegment.from_wav(path)  
  chunks = split_on_silence(sound,
    
      min_silence_len = 500,
    
      silence_thresh = sound.dBFS-14,
      
      keep_silence=500,
  )
  folder_name = "audio-chunks"

  if not os.path.isdir(folder_name):
      os.mkdir(folder_name)

  whole_text = ""

  for i, audio_chunk in enumerate(chunks, start=1):
    
      chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
      audio_chunk.export(chunk_filename, format="wav")
    
      with sr.AudioFile(chunk_filename) as source:
          audio_listened = r.record(source)
        
          try:
              text = r.recognize_google(audio_listened, language="en-IN")
          except sr.UnknownValueError as e:
              print("Error:", str(e))
          else:
              text = f"{text.capitalize()}. "
              print(chunk_filename, ":", text)
              whole_text += text

    # STT done
  trans = open('trans.txt', 'a')
  trans.write(whole_text)
  trans.close()


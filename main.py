import os

from gtts import gTTS

with open('textfile.txt', 'r') as f:
    x = f.read()

language = 'en'
audio = gTTS(text=x, slow=False )
audio.save('audiofile.wav')
os.system('audiofile.wav')

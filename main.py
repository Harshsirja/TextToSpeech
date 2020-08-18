import os

from googletrans import Translator
from gtts import gTTS

with open('textfile.txt', 'r') as f:
    x = f.read()
f.close()

translator = Translator()
y = translator.translate(x, src='en', dest='gu')
audio = gTTS(text=y.text, slow=True, lang='gu')
audio.save('audiofile.mp3')
os.system('audiofile.mp3')

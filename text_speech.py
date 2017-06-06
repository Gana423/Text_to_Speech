from gtts import gTTS
import os

f = open("test.txt", "r")
f_text = f.read()
f.close()
print f_text

tts = gTTS(text=f_text, lang='en')
tts.save("response.mp3")
os.system("mpg321 response.mp3")

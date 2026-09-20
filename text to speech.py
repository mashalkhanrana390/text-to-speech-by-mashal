from gtts import gTTS
from playsound import playsound

text = "Hey, I am Mashal Khan, AI student and future AI engineer!"

tts = gTTS(text=text, lang="en")

tts.save("voice.mp3")

print("Audio saved successfully!")

playsound("voice.mp3")

# 🔊 Text to Speech by Mashal

A simple Python **Text-to-Speech (TTS)** project that converts written text into spoken audio using **gTTS (Google Text-to-Speech)** and plays the generated audio using **playsound**.

## 🚀 Features

* Convert text into speech
* Generate an MP3 audio file
* Automatically play the generated voice
* Simple and beginner-friendly Python project

## 🛠️ Technologies Used

* Python
* gTTS
* playsound

## 📦 Installation

Install the required libraries:

```bash
py -m pip install gTTS
py -m pip install playsound==1.2.2
```

## ▶️ How to Run

Run the program:

```bash
py main.py
```

The program will:

1. Convert the text into speech.
2. Save the voice as `voice.mp3`.
3. Play the generated audio automatically.

## 💻 Code

```python
from gtts import gTTS
from playsound import playsound

text = "Hey, I am Mashal Khan, AI student and future AI engineer!"

tts = gTTS(text=text, lang="en")

tts.save("voice.mp3")

print("Audio saved successfully!")

playsound("voice.mp3")
```

## 📁 Project Structure

```text
text-to-speech-by-mashal/
│
├── main.py
├── voice.mp3
└── README.md
```

## 🎯 Purpose

This project was created as a beginner Python mini project to learn how **Text-to-Speech technology** works and how Python can generate audio from text.

## 👨‍💻 Author

**Mashal Khan**

AI Student | Python Developer | Future AI Engineer

## 📌 Future Improvements

* Add user input
* Add different languages
* Add voice selection
* Create a GUI
* Add voice commands

---

⭐ If you find this project useful, feel free to star the repository!

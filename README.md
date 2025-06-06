🎙️ OB: Offline + Online AI Voice Assistant (Python)
OB is a Python-based voice assistant that processes offline speech using Vosk and responds intelligently using the Groq API (for online queries). It can perform local tasks like opening apps, playing music, telling time, and even answer general questions using an LLM model.

🚀 Features
✅ Offline Speech Recognition via Vosk

✅ Online AI responses via Groq LLM

✅ Smart text-to-speech using pyttsx3

✅ Personalized greetings based on time

✅ Open apps like Chrome, YouTube, camera, Flappy Bird game, etc.

✅ Play music, access folders, or fetch time

✅ Flexible fallback to online chatbot when no command is matched

🧰 Tech Stack
Component	Purpose
Vosk	Offline speech-to-text engine
PyAudio	Access microphone audio stream
pyttsx3	Offline text-to-speech (TTS)
Groq API	Online chatbot response engine
webbrowser, os	System automation & file access

🗂️ Project Structure
voice-assistant-ob/
│
├── assistant.py               # Main voice assistant script
├── README.md                  # Project documentation
├── vosk-model-en-us-0.22/     # Vosk speech model directory
└── assets/                    # Optional folder for music, scripts, etc.

🧪 Requirements
Install dependencies via pip:
pip install vosk pyaudio pyttsx3 groq

⚠️ Note: For Windows, if pyaudio fails:
pip install pipwin
pipwin install pyaudio

🔧 Setup
Download Vosk Model:
Download the model vosk-model-en-us-0.22 from here
Extract it and update the model path in the script.

Set Groq API Key:
Replace "key" in this line with your actual API key:
client = Groq(api_key="your-api-key")

Prepare Shortcuts & Media:
Create app shortcuts (e.g., Chrome, YouTube)
Add music to C:/Users/YourName/Music
Add personal scripts (e.g., camera.py, flappy bird.py)

🗣️ Supported Voice Commands
Command Keywords	Action
open youtube	Launch YouTube in browser
open chrome / google	Launch Chrome or open Google
open videos / video	Open local Videos folder
open stackoverflow	Open Stack Overflow website
play music / music	Play a music file from the Music folder
next / change	Play the next music file
what is time / the time	Speak the current system time
open code	Run your personal Python script
open camera / camera	Launch camera script
open play it / playit	Open PLAYit media player
flappy bird / flapy	Launch Flappy Bird Python game
exit / quit / off	Stop the assistant

If a command is not recognized, it will ask Groq LLM and respond with a brief answer.

💬 Sample Output
You said: what is time
Assistant: The time is 14:37:22

Or for an unknown query: 
You said: who is elon musk
Assistant: Elon Musk is a tech entrepreneur known for Tesla, SpaceX, and Neuralink.

📌 Notes
This assistant runs in an infinite loop; use "exit" or "quit" to terminate.
You can extend functionality by adding more commands or models.
Ensure your microphone is working properly and PyAudio is installed correctly.

🙋‍♂️ Author
Yash Vaghasiya
💡 Python & AI Enthusiast | Offline + Online AI Integrator

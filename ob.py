from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import datetime
import webbrowser
import os
from groq import Groq
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("vary Good Morning yash!")
    elif hour < 18:
        speak("vary Good Afternoon yash!")
    else:
        speak("vary Good Evening yash!")
    speak("I am O B.  your new personal assistant.")

model = Model(r"C:/Users/vagha/OneDrive/Documents/A.i. project/vosk-model-en-us-0.22")
if not model:
    print("Model not found.")
    exit(1)
recognizer = KaldiRecognizer(model, 16000, '["open youtube", "play music", "exit", "open chrome", "what is time", "open videos"]')


mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

client = Groq(api_key="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") 

wishMe()
print("Listening...")

a = 0  

while True:
    data = stream.read(8192, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        result_json = recognizer.Result()
        result = json.loads(result_json)
        query = result.get("text", "").lower().strip()

        if not query:
            continue
        print(f"You said: {query}")

        if 'open youtube' in query or 'youtube' in query:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        elif 'open chrome' in query or 'open google chrome' in query:
            codePath = "C:\\Users\\Public\\Desktop\\Google Chrome.lnk"
            os.startfile(codePath)
            speak("Opening Google Chrome")

        elif 'open google' in query:
            webbrowser.open("https://google.com")
            speak("Opening Google")

        elif 'open videos' in query or 'video' in query:
            codePath = "C:\\Users\\vagha\\Videos"
            os.startfile(codePath)
            speak("Opening Videos folder")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")
            speak("Opening Stack Overflow")

        elif 'play music' in query or 'music' in query:
            music_dir = 'C:\\Users\\vagha\\Music'
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[a % len(songs)]))
                speak("Playing music")
            else:
                speak("No music files found")

        elif 'next' in query or 'change' in query:
            music_dir = 'C:\\Users\\vagha\\Music'
            songs = os.listdir(music_dir)
            a += 1
            if songs:
                os.startfile(os.path.join(music_dir, songs[a % len(songs)]))
                speak("Playing next music")
            else:
                speak("No music files found")

        elif 'the time' in query or 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\vagha\\OneDrive\\Documents\\A.i. project\\ob.py"
            os.startfile(codePath)
            speak("Opening code folder")

        elif 'open camera' in query or 'camera' in query:
            codePath = "C:\\Users\\vagha\\OneDrive\\Documents\\AI\\camera.py"
            os.startfile(codePath)
            speak("Opening camera application")

        elif 'open play it' in query or 'playit' in query:
            codePath = "C:\\Users\\vagha\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\PLAYit\\PLAYit.lnk"
            os.startfile(codePath)
            speak("Opening PLAYit")

        elif 'flappy bird' in query or 'flapy' in query:
            codePath = "C:\\Users\\vagha\\OneDrive\\Documents\\AI\\flappy bird.py"
            os.startfile(codePath)
            speak("Opening Flappy Bird game")

        elif 'exit' in query or 'off' in query or 'quit' in query:
            speak("Goodbye yash")
            break

        else:
            speak("Searching for answer...")
            try:
                completion = client.chat.completions.create(
                    model="deepseek-r1-distill-llama-70b",
                    messages=[
                        {"role": "user", "content": f"{query}. Answer in only 50 words."}
                    ],
                    temperature=0.6,
                    max_completion_tokens=500,
                    top_p=0.95,
                    stream=True,
                    stop=None,
                )

                full_response = ""
                in_think_block = False

                for chunk in completion:
                    content = chunk.choices[0].delta.content or ""
                    if "<think>" in content:
                        in_think_block = True
                        continue
                    elif "</think>" in content:
                        in_think_block = False
                        continue
                    elif not in_think_block:
                        print(content, end="", flush=True)
                        full_response += content

                print()
                speak(full_response.strip())
            except Exception as e:
                print("Error with Groq API:", e)
                speak("Sorry, I am unable to get the answer right now.")

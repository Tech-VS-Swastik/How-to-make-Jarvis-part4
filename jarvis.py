import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import datetime #pip install datetime
import os #pip install os
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("My Master's name is Swastik and Swastik is a good boy")

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning Master!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon Master!")

    else:
        speak("Good Evening Master!")

    speak("I am Jarvis, your personal assistant made with the help of AI(Artificial Intelligence) Made by- Master Swastik. I can do many things for you just give me any task")

def takeCommand():
    # It takes microphone input from the user and give a string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based query

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According wikipedia")
            #print(results)
            speak(results)

        elif 'open notepad' in query:
            speak("opening notepad")
            n = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(n)

        elif 'close notepad' in query:
            speak("ok sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'open this pc' in query:
            speak("ok sir, opening this pc")
            tp = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\this pc"
            os.startfile(tp)

        elif 'good bye' or 'go offline' in query:
            speak("ok sir, thank you for using me. Have a nice day")
            exit()
            sys.exit
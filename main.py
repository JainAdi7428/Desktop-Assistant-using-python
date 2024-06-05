import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

#taking voice from my system

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
print(type(voices))
print(voices[0].id)

engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)

#speak function
def speak(text):
    """this converts text to speech"""
    engine.say(text)
    engine.runAndWait()

#speech recognition documentation
def takeCommand():
   """this function will recognize voice and return text"""
   r= sr.Recognizer()
   with sr.Microphone() as source:
       print("Listening..")
       r.pause_threshold = 1
       #pause_threshold is used to remove background Noises
       audio = r.listen(source)
       
       try:
           print("Recognizing...")
           query = r.recognize_google(audio , language = 'en-in')
           print(f"user said {query}\n")

       except Exception as e:
           print('say that again please')
           return 'none'
       return query

def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour >=0 and hour <12 :
        speak("good morning sir how are you doing")

    elif hour >=12 and hour <18:
        speak("good afternoon sir how are you doing")

    else :
        speak(" good evening sir how are you doing")

    speak ("how may i assist you")
    #    industry ready code
if __name__== "__main__":
    wish_me()

    while True:
        query=takeCommand().lower()


        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace('wikipedia','')
            print(query)
            results=wikipedia.summary(query,sentences =2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query :
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "google" in query :
            speak("opening google")
            webbrowser.open("google.com")




        




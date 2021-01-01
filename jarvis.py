import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("iam jarvis,please tell me how may i help you.")    

def takeCommand():
    #it takes the microphone input from user and returns string output
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)   

    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

  
    except Exception as e:
        #print(e)
        print("say that again please..")
        return "None"
    return query    
    
   

if __name__ == "__main__":

    wishMe()
    #while True:
    if 1:
        query=takeCommand().lower()
        #logic for executing task based on query
        if 'wikipedia' in query:            
            speak('searching wikipedia..')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")  

        elif 'open visual studio code' in query:
            codePath=  "C:\\Users\\KAVITHA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'hi jarvis' in query:
            speak("hii  kavitha.")

        elif 'how are u' in query:
            speak("iam good,what about u?")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\KAVITHA\\Music\\New folder\\'
            songs = os.listdir(music_dir) 
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
           

           
        
            
         
            
              
  
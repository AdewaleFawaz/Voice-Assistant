import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts=gTTS(text=text, lang="en",tld='com.au')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    
def get_audio():
    r=sr.Recognizer()
   
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
        said = ""
        
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception  as e:
                print("Exception: " + str(e))
                print("unable to recognize your voice")
    return said  
    
speak("Hello! ")
get_audio()




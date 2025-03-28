import win32com.client
import speech_recognition as sr
import os



def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)
def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language='en-in')
        print(f"user Said {query}")
        return query



if __name__ == '__main__':
    print("hello")
    print("Listening...")
    text = takeCommand()
    say(text)
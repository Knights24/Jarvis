from idlelib import query

import win32com.client
import speech_recognition as sr
import os
import webbrowser



def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)
def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said {query}")
            return query
        except Exception as e:
            return "Some error occurred, Sorry form MIKE  "




if __name__ == '__main__':
    print("hello")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "youtube.com"], ["google", "google.com"],["chatgpt","chatgpt.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
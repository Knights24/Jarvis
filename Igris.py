import win32com.client
import speech_recognition as sr
import os
import webbrowser


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=1)  # Reduce background noise
        try:
            print("Listening for a command...")
            audio = r.listen(source, timeout=5, phrase_time_limit=8)  # Timeout and phrase limits
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for input. Please try again.")
            return ""
        except sr.UnknownValueError:
            print("Sorry, I couldn’t understand the audio. Could you please repeat?")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return ""


if __name__ == '__main__':
    print("Hello! Igris is ready to assist you.")
    while True:
        print("Listening...")
        query = takeCommand()
        text = takeCommand()
        say(text)
        if not query:
            continue
        if "exit" in query.lower() or "quit" in query.lower():
            say("Goodbye! Have a great day!")
            break
        sites = [["youtube", "youtube.com"], ["google", "google.com"], ["chatgpt", "chatgpt.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(f"https://{site[1]}")

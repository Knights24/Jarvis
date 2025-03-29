import pyttsx3


def list_voices():
    """Lists all available voices on the system."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for index, voice in enumerate(voices):
        print(f"Voice {index}: {voice.name} | ID: {voice.id}")


def say_hindi(text):
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty('voices')

    # Set Hindi voice (if available)
    for voice in voices:
        if "hindi" in voice.name.lower() or "hindi" in voice.id.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    list_voices()  # Run this first to find a Hindi voice
    text = input("Enter Hindi text: ")
    say_hindi(text)

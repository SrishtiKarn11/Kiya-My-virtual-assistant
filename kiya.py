import pyttsx3
import speech_recognition as sr
import os
import datetime
import pywhatkit

# Step 1: Initialize Text-to-Speech engine (Female voice, slow)
engine = pyttsx3.init()
engine.setProperty('rate', 160)  # Slow speech rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice


def speak(text):
    print(f"Kiya: {text}")
    engine.say(text)
    engine.runAndWait()


# Step 2: Initialize Speech Recognition
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print(f"You said: {command}")
    except Exception as e:
        print(f"Error: {str(e)}")
        speak("Sorry, I didn't catch that.")
        return ""

    return command.lower()


# Step 3: Open Chrome browser (Windows-specific)
def open_in_chrome(url):
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    try:
        os.system(f'"{chrome_path}" {url}')
    except Exception as e:
        print(f"Error: {str(e)}")
        speak("Sorry, I couldn't open Chrome.")


# Step 4: Main assistant logic
def run_kiya():
    speak("Hi! I'm Kiya, your assistant. What can I do for you?")

    while True:
        query = take_command()

        # Check if command includes 'time'
        if "time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")

        # Check if command includes 'open youtube'
        elif "open youtube" in query:
            speak("Opening YouTube.")
            open_in_chrome("https://www.youtube.com")

        # Check if user wants to search something
        elif "search" in query:
            speak("What do you want to search?")
            search_query = take_command()
            open_in_chrome(f"https://www.google.com/search?q={search_query}")

        # Check if user wants to play a song on YouTube
        elif "play song" in query:
            speak("Which song should I play?")
            song = take_command()
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)

        # Exit the assistant
        elif "bye" in query or "exit" in query:
            speak("Goodbye! Have a great day.")
            break

        # Default response if Kiya doesn't understand the command
        else:
            speak("Sorry, I'm still learning. Can you try again?")


if __name__ == "__main__":
    run_kiya()
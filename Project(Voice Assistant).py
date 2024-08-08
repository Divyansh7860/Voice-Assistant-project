import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: " + query + "\n")
    except Exception as e:
        print(e)
        speak("I didn't understand")
        return "None"
    return query

if __name__ == '__main__':
    speak("Amigo assistance activated")
    speak("How can I help you")

    while True:
        query = take_command()
        print(f"Query received: {query}")  # Debugging print

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", '')
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("I couldn't find a page for that topic.")
            except Exception as e:
                speak("An error occurred while searching Wikipedia.")
        
        elif 'hello' in query:
            speak("I am Amigo, developed by Divyansh")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'open github' in query:
            speak("Opening GitHub")
            webbrowser.open("https://www.github.com")

        elif 'open stackoverflow' in query:
            speak("Opening StackOverflow")
            webbrowser.open("https://www.stackoverflow.com")

        elif 'open spotify' in query:
            speak("Opening Spotify")
            webbrowser.open("https://www.spotify.com")

        elif 'open whatsapp' in query:
            speak("Opening WhatsApp")

        elif 'play music' in query:
            speak("Playing music")
            webbrowser.open("https://www.spotify.com")

        elif 'local disk d' in query:
            speak("Opening local disk D")
            webbrowser.open("file:///D:/")

        elif 'local disk c' in query:
            speak("Opening local disk C")
            webbrowser.open("file:///C:/")

        elif 'local disk e' in query:
            speak("Opening local disk E")
            webbrowser.open("file:///E:/")

        elif 'sleep' in query:
            speak("Goodbye!")
            break  # Exit the loop gracefully


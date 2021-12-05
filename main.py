import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# The A.I. is listening
listener = sr.Recognizer()
# The A.I. audio
engine = pyttsx3.init()
# Change the voice
voices = engine.getProperty('voices')
# String identifier of the active voice
engine.setProperty('voice', voices[1].id)
# Integer speech rate in words per minute. The base value is 200
engine.setProperty('rate', 150)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        # Your voice is being catch by microphone
        with sr.Microphone() as source:
            # To notify that the A.I. is listening
            print('listening...')
            voice = listener.listen(source)
            # Convert the text to audio by google audio
            # For the languange codes is here https://cloud.google.com/speech-to-text/docs/languages
            command = listener.recognize_google(voice, language = "id-ID") # If you want to  change the language just type (voice, language = "code")
            command = command.lower()
            # If 'Pandora' is in the command
            if 'pandora' in command:
                # Remove 'Pandora' word
                command = command.replace('pandora', '')
                print(command)
    except:
        pass
    return command

def run_pandora():
    command = take_command()
    print(command)
    # If 'play' is in the command
    if 'play' in command:
        # Remove 'play' word
        song = command.replace('play', '')
        talk('playing' + song)
        # Playing some music on YT
        pywhatkit.playonyt(song)

    elif 'time' in command:
        # %H for Hour, $M for Minute, %I for 1-12 (hour), $p for AM/ PM
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Right now is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1) # 1 is for how many sentences you want to get as result
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'thank you' in command:
        talk('Youre welcome')
        return False

    else:
        talk('Sorry, can you repeat it again?')

    return True

while True:
    if not run_pandora():
        break

import speech_recognition as sr
import pyttsx3 as tv
import pywhatkit
import datetime
import wikipedia
import pyjokes
import ctypes
from multiprocessing import Process

listener = sr.Recognizer()
engine = tv.init()


def dialogbox():
    ctypes.windll.user32.MessageBoxW(0, "Hi i am your Virtual Assistant, Alexa. I am listening. Ask me something", "Hi",
                                     0)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            talk('listening')

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)

    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        print('playing' + song)
    elif 'how are you' in command:
        talk('I am fine !')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current Time is ' + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d:%B')
        print(date)
        talk('Today is ' + date)
    elif 'day' in command:
        day = datetime.datetime.now().strftime('%A')
        print(day)
        talk('Today is ' + day)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'go for date' in command:
        talk('sorry i have a headache')
    elif 'are you single' in command:
        talk('i am relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I cant get you')

while True:
    dialogbox()
    run_alexa()



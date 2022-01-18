import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()


def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def time_():
    Hour = datetime.datetime.now().strftime("%H")
    Minute = datetime.datetime.now().strftime("%M")
    if int(Hour) > 12:
        Hour = Hour - 12
        speak("The current time is %s %s PM" % (Hour, Minute))
    else:
        speak("The current time is %s %s AM" % (Hour, Minute))

def date_():
    months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    year = datetime.datetime.now().year
    month = months[datetime.datetime.now().month - 1]
    day = datetime.datetime.now().day
    speak("The Current Date is %s %s %s" % (month, day, year))


def wishme():
    hour = datetime.datetime.now().hour
    if int(hour) > 12:
        speak("Good afternoon Mister Malick")
        time_()
        date_()
    else:
        speak("Good Morning Mister Malick")
        time_()
        date_()
    speak("How can I assist you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please......")
        return "None"
    return query        

takeCommand()
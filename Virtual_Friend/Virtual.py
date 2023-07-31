import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wall():
    speak("which tyoe of wallpaper do you want to open")
    speak("nature!")
    speak("cars!")
    speak("random!")

    a = sr.Recognizer()
    print("listening..")
    with sr.Microphone() as mic:
        au_wal = a.record(mic, duration = 5)
        print("Recognizing...")
        walp = f.recognize_google(au_wal)
        

    if(walp == "nature"):
        webbrowser.open("https://www.pexels.com/search/nature%20wallpaper/")

    elif(walp == "cars"):
        webbrowser.open("https://www.pexels.com/search/car%20wallpapers/")

    elif(walp == "random"):
        webbrowser.open("https://www.hdwallpapers.in/")



def calculation():
    speak("enter the number of element that you want to calculate")
    n = int(input("enter the no."))
    list = []

    speak("enter the values")
    print("enter the value ")
    for i in range(0,n):
        ele = int(input())
        list.append(ele)

    speak("which opration you want to oprate")
    speak("press 1 for addition")
    speak("press 2 for substraction")
    speak("press 3 multiplication")
    ch = int(input("enter your choice "))
    if(ch == 1):
        add = 0
        for i in range(0,n):
            add = list[i] + add
            addd = str(add)
        speak("the addition is" + addd)
    
    elif(ch == 2):
        sub = 0
        for i in range(0,n):
            sub = list[i] - sub
            subb = str(sub)
        speak("the substraction is" + subb)

    elif(ch == 3):
        mul = 1
        for i in range(0,n):
            mul = list[i] * mul
            mull = str(mul)
        speak("the substraction is" + mull)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!" + name)
    
    elif(hour>=12 and hour<18):
        speak("good afternoon!" + name)

    elif(hour>=18 and hour<21):
        speak('good evening!' + name)

    else:
        speak("good night!"+ name)

    speak('i am chhotu . Please tell me how may i help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"You said:{query}\n")

    except Exception:
        pass

        print("say that again")
        return 'None'
    return query


if 1:
    speak("hello Sir, what is your name")
    f = sr.Recognizer()
    print("listening..")
    with sr.Microphone() as ss:
        audio_data = f.record(ss, duration = 5)
        print("Recognizing...")
        name = f.recognize_google(audio_data)
    

    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open hackerrank' in query:
            url = "https://www.hackerrank.com/auth/login?h_l=body_middle_left_button&h_r=login"
            webbrowser.open(url)

        elif 'open portal' in query:
            prl = "http://glauniversity.in:8085/"
            webbrowser.open(prl)

        elif 'wallpaper' in query:
            wall()

        elif 'teacher' in query:
            print("Piyush Vashistha")
            speak("piyush vashistha")

        elif 'who is' in query:
            webbrowser.open(query)
             
        elif 'calculator' in query:
            calculation()

        elif 'who are you' in query:
            speak("i am chhotu, your assistant, speed one terahartz memory one zettabyte")

        elif 'what' in query:
            webbrowser.open(query)

        elif 'open photos' in query:
            folderpath = "C:\\Users\\Lenovo\\Desktop\\ABD"
            os.startfile(folderpath)

        
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"the time is {strtime}")

        elif 'quit' in query or 'bye' in query or 'tata' in query or 'ok thanks' in query:
            speak("thanks for using me," + name)
            exit()


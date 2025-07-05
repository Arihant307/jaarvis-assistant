import speech_recognition as sr
import pyttsx3
import setuptools
import webbrowser
import datetime
import os
import google.generativeai as genai
import songs
import time


recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open chrome" in c.lower():
        webbrowser.open("https://google.com")
        # os.system("start chrome")
        speak("opening chrome")

    elif "tell me about your developer" in c.lower():
        speak("A Man Who Develops Me is Arihant. Arihant is a Great developer and he is Enthusiasm in developing bots like me .He is Pursuing Btech in computer science and Engineering with specialization in data science")
        

    elif "open notepad" in c.lower():
        os.system("start notepad")

    elif "close notepad" in c.lower():
        os.system("taskkill /f /im notepad.exe")
        speak("Closing Notepad Boss")
    elif "open spotify" in c.lower():
        os.system("start spotify")
        speak("opening spotify")
    elif "close spotify" in c.lower():
        os.system("taskkill /f /im spotify.exe")
        speak("closing spotify Boss")
    elif "open whatsapp" in c.lower():
        os.system("start whatsapp")
        speak("opening WhatsApp")

        speak("opening whatsapp")

    elif "open calculator" in c.lower():
        os.system("start calc")
        speak("opening calculator")

    # elif "close calculator" in c.lower():
    #     # os.system("taskkill /f /im calc.exe")
    #     os.system('powershell "Stop-Process -Name calculator -Force"')


    elif "open camera" in c.lower():
        os.system("start microsoft.windows.camera:")
        speak("opening camera Boss")
    elif "close camera" in c.lower():
        os.system("taskkill /f /im WindowsCamera.exe")
        speak("closing camera")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
        speak("opening Youtube")
    elif "open linkedin" in c.lower():
        os.system("start linkedin")
        speak("opening linkedIn")
    elif "from youtube" in c.lower():

        content1= c.split(" ")[0]
        content2= c.split(" ")[1]
        webbrowser.open(f"https://www.youtube.com/results?search_query={content1}+{content2}")
    elif c.lower().startswith("play"):
        name1=c.lower().split(" ")[1]
        print(name1)
        if name1=="sukun":
            name1="sukoon"
        # name2=c.lower().split(" ")[2]
        link=songs.music[name1]
        print(link)
        webbrowser.open(link)
    elif "time"in c.lower():
        speak(time.ctime())
    
    else:
        
        genai.configure(api_key="AIzaSyAH-7aFZmLdEVmMZlc8dxtzBGIqGMdyHl4")
        
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(c)
        speak(response.text)




def WishMe():
    
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning My dear Boss Arihant!!")
    elif(hour>12 and hour<=18):
        speak("Good Afternoon My Dear Boss Arihant!!")
    else:
        speak("Good Evening My Dear Boss Arihant!!")

    speak("I am Your Assistant Jaarvis !! Please tell Me How  May i Help You") 


if __name__=="__main__":
    speak("Hello My dear Boss Arihant !! I am Your Assistant Jaarvis")

    while True:
        r=sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone()as source:
                print("Listening...")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
                recognizer.adjust_for_ambient_noise(source,duration=1)
                # r.pause_threshold=1
                # r.energy_threshold=100
            word=r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("Yes My Dear Boss Arihant !!How May i Help You")
                # WishMe()

                with sr.Microphone() as source:
                    print("Jaarvis Active....")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:

            # speak("Sorry Can you Plzz Speak Again")
            print(e)
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import pyautogui
import keyboard
import pyjokes
from PyDictionary import PyDictionary as diction

assistant = pyttsx3.init('sapi5')
voices = assistant.getProperty('voices')
assistant.setProperty('voices', voices[1].id)


def speak(audio):
    print("     ")
    assistant.say(audio)
    print(f": {audio}")
    assistant.runAndWait()


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing.....")
            query = command.recognize_google(audio, language='en-in')
            print(f"You said : {query}")

        except Exception as Error:
            return "none"

        return query.lower()


def taskExe():
    print()
    print("               INFORMATICS PRACTICES(065)               ")
    print("                       PROJECT                          ")
    print("                      JARVIS AI                         ")
    print()
    print("                     PREPARED BY                        ")
    print("                  ANEESH PHALTANKAR                     ")
    print("--------------------------------------------------------")

    speak("all systems are a go sir.")
    print()

    def wishme():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("good morning sir")

        elif hour >= 12 and hour < 18:
            speak("good afternoon sir")

        else:
            speak("good evening")

    def openapps():
        speak("ok sir wait a second")

        if 'code' in query:
            os.startfile(os.getcwd())

        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com")

        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com")

        elif 'youtube' in query:
            webbrowser.open("https://youtube.com")

    def closeapps():
        speak("ok sir.")

        if 'youtube' in query:
            os.system("taskkill /f /im brave.exe")

        elif 'instagram' in query:
            os.system("taskkill /f /im brave.exe")

        elif 'code' in query:
            os.system("taskkill /f /im main.py")

        elif 'facebook' in query:
            os.system("taskkill /f /im brave.exe")

        elif 'teams' in query:
            os.system("taskkill /f /im teams.exe")

    def youtubeauto():
        speak("What do you want me to do?")
        comm = takecommand()

        if 'pause the video' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'fullscreen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        speak("done sir")

    def dict():
        speak("tell me the problem")
        prob = takecommand()

        if 'meaning' in prob:
            prob = prob.replace("what is the","")
            prob = prob.replace("jarvis","")
            prob = prob.replace("of","")
            prob = prob.replace("meaning","")
            result = diction.meaning(prob)
            speak(f"the meaning of {prob} is {result}")

        elif 'synonym' in prob:
            prob = prob.replace("what is the","")
            prob = prob.replace("jarvis","")
            prob = prob.replace("of","")
            prob = prob.replace("synonym","")
            result = diction.synonym(prob)
            speak(f"the synonym of {prob} is {result}")

        elif 'antonym' in prob:
            prob = prob.replace("what is the","")
            prob = prob.replace("jarvis","")
            prob = prob.replace("of","")
            prob = prob.replace("antonym","")
            result = diction.antonym(prob)
            speak(f"the antonym of {prob} is {result}")

        elif 'opposite' in prob:
            prob = prob.replace("what is the","")
            prob = prob.replace("jarvis","")
            prob = prob.replace("of","")
            prob = prob.replace("opposite","")
            result = diction.antonym(prob)
            speak(f"the opposite of {prob} is {result}")

        speak("exited dictionary")

    def screenshot():
        speak("what should i name the file?")
        os.getcwd()
        path = takecommand()
        pathname = path + '.png'
        path1 = os.getcwd() + pathname
        ss = pyautogui.screenshot()
        ss.save(path1)
        os.startfile(os.getcwd())
        speak("here is your screenshot")

    while True:

        query = takecommand()

        if 'hello' in query:
            wishme()
            speak("i am Jarvis")
            speak("your personal ai assistant")
            speak("how may i help you?")

        elif 'how are you' in query:
            speak("i am fine sir. how may i help you today?")

        elif 'break' in query:
            speak("ok sir. you can call me anytime")
            break

        elif 'bye' in query:
            speak("good day to you sir")
            break

        elif 'youtube search' in query:
            speak("ok sir. this is what i found for your search")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done sir")

        elif 'google search' in query:
            speak("ok sir. this is what i found for your search")
            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            web = 'https://www.google.com/search?q=' + query
            webbrowser.open(web)
            speak("done sir")

        elif 'website' in query:
            speak("ok sir...launching...")
            query = query.replace("jarvis", "")
            query = query.replace("website", "")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak('all systems go sir')

        elif 'launch' in query:
            speak("tell me the name of the website")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Launching...")

        elif 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            speak(f"according to wikipedia : {wiki}")

        elif 'screenshot' in query:
            screenshot()

        elif 'music' in query:
            music_dir = 'C:\\TVALOS\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'pause the video' in query:
            keyboard.press('space bar')

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {time}")

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            youtubeauto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)

        elif 'repeat after me' in query:
            speak("listening")
            jj = takecommand()
            speak(f"you said {jj}")

        elif 'dictionary' in query:
            dict()

        elif 'well done' in query:
            speak("thank you sir.")

        elif 'open youtube' in query:
            openapps()

        elif 'open code' in query:
            openapps()

        elif 'open instagram' in query:
            openapps()

        elif 'open facebook' in query:
            openapps()

        elif 'close youtube' in query:
            closeapps()

        elif 'close code' in query:
            closeapps()

        elif 'close instagram' in query:
            closeapps()

        elif 'close facebook' in query:
            closeapps()

taskExe()

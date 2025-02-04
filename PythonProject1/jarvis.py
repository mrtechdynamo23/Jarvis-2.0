import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import kit

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice to text
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis Sir. Please tell me how can i help you")

if __name__=="__main__":
    wish()
    #while True:
    if 1:
        query=takecommand().lower()
        #logic Building for tasks
        if "open notepad" in query:
            speak("Here's notepad for your text documents Sir")
            npath='C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2410.21.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe'
            os.startfile(npath)

        elif "open command prompt" in query:
            speak("Enabling command prompt mode for you Sir")
            os.system("start cmd")

        elif "open camera" in query:
            speak("ready to see how successful you are sir")
            cam = cv2.VideoCapture(0)
            frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))
            while True:
                ret, frame = cam.read()
                # Write the frame to the output file
                out.write(frame)
                # Display the captured frame
                cv2.imshow('Camera', frame)
                # Press 'q' to exit the loop
                if cv2.waitKey(1) == ord('q'):
                    break
            # Release the capture and writer objects
            cam.release()
            out.release()
            cv2.destroyAllWindows()

        elif "play some music" in query:
            speak("as you wish sir")
            music_dir= 'C:\\Users\\sudha\\Music'
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            speak("as you wish sir")
            webbrowser.open_new_tab('https://youtube.com/')

        elif "open google" in query:
            speak("Sir, what should I search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open instagram" in query:
            speak("as you wish sir")
            webbrowser.open_new_tab('https://www.instagram.com/')

        elif "open udemy" in query:
            speak("as you wish sir")
            webbrowser.open_new_tab('https://www.udemy.com/?utm_source=bing-brand&utm_medium=udemyads&utm_campaign=BG-Brand-Udemy_la.EN_cc.INDIA&campaigntype=Search&portfolio=BrandDirect&language=EN&product=Course&test=&audience=&topic=&priority=&utm_content=deal4584&utm_term=_._ag_1214960761428279_._ad__._kw_Udemy_._de_c_._dm__._pl__._ti_kwd-75935360497446:loc-90_._li_149875_._pd__._&matchtype=e&msclkid=b49d301e326d1a44190557bf223cce5a')

        elif "send message" in query:
            pywhatkit.sendwhatmsg("+919003948299","This is a testing protocol message",2,25)
 #   speak("Hello Sir")
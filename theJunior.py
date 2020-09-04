import pyttsx3 #install
import datetime
import speech_recognition as sr #installl
import wikipedia #install 
import webbrowser
import os
import socket
import sys
import multiprocessing


def how_can_i():
    speak("Verification Successfull! Thank You Sir!")
    speak("How Can I help you ?")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good morning Sir")
            speak("What's The Password!")
        elif hour>=12 and hour<4:
            speak("Good afternoon Sir")
            speak("What's The Password!")
        else:
            speak("Good Evening Sir")
            speak("What's The Password!")
def takeCommand1():
        # takes my command from microphone and gives text
        r =sr.Recognizer()
        with sr.Microphone() as source:
            print("listening......")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("recognizing.....")
            query = r.recognize_google(audio, language ='en-in')
            print("query said : ", query)
        except Exception as e:
            print(e)
            print("What's the Name!!")
            return "None"
        return query
def takeCommand2():
        # takes my command from microphone and gives text
        r =sr.Recognizer()
        with sr.Microphone() as source:
            print("listening......")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("recognizing.....")
            query = r.recognize_google(audio, language ='en-in')
            print("query said : ", query)
        except Exception as e:
            print(e)
            print("What's the Name!!")
            return "None"
        return query
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def Rahul():
    run_once=0
    how=0
    while True:
        '''engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        # print(voices[1].id)
        engine.setProperty('voice', voices[0].id)'''

        query = takeCommand1().lower()
        wake=""
        wake=query
        wake.strip()      
        wake.lower()
        #print(wake)
        while "junior" in wake:

            def takeCommand():
        # takes my command from microphone and gives text
                r =sr.Recognizer()
                with sr.Microphone() as source:
                    print("listening......")
                    r.pause_threshold = 1
                    audio = r.listen(source)
                try:
                    print("recognizing.....")
                    query = r.recognize_google(audio, language ='en-in')
                    print("query said : ", query)
                except Exception as e:
                    print(e)
                    speak("Sorry Sir, can you repeat that again?")
                    return "None"
                return query
            
            if run_once == 0:
                wishMe()
                run_once=1
            # speak("I am your Assistant FRIDAY")
            
            if __name__ == "__main__":
                    query1 = takeCommand2().lower()
                    wake1=""
                    wake1=query1
                    wake1.strip()      
                    wake1.lower()
                    
     
                        
                        if how==0:
                            how_can_i()
                            how = 1
                        elif how==1:        
                            speak("Next Command Plz?")
                        query = takeCommand().lower()
                        if 'ip address' in query:
                            speak("Finding")
                            hname = socket.gethostname()
                            results = socket.gethostbyname(hname)
                            print(hname)
                            print(results)
                            speak('Host name is:')
                            speak(hname)
                            speak('IP address is :')
                            speak(results)           
                        
                        elif 'wikipedia' in query:
                            speak("searching in wikipedia")
                            query = query.replace("wikipedia", "")
                            results = wikipedia.summary(query, sentences = 4)
                            speak("According to wikipedia")
                            print(results)
                            speak(results)

                        elif 'open youtube' in query:
                            webbrowser.open("youtube.com")
                            speak("youtube is opened")
                        elif 'open google' in query:
                            webbrowser.open("google.com")
                            speak("google is opened")
                        elif 'open gmail' in query:
                            webbrowser.open("gmail.com")
                            speak("gmail is opened")
                        elif 'play music' in query:
                            music_dir = 'D:\\music'
                            songs = os.listdir(music_dir)
                            print(songs)
                            os.startfile(os.path.join(music_dir, songs[0]))
                            speak("music is being played")

                        elif 'time' in query:
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            speak(f"the time is {strTime}")
                        elif 'open code' in query:
                            codepath = "C:\\Users\\Rahul\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                            os.startfile(codepath)
                        elif 'close code' in query:
                            os.system("taskkill /f /im Code.exe") 
                            speak('closed')     
                            
                        elif 'stop' in query:
                            speak("see you soon Sir")
                            Rahul()
                        
                        elif 'date' in query:        
                            now = datetime.datetime.now()
                            speak('Current date and time is:')
                            speak(now)
                        elif 'who invented you' in query:
                            speak("At first I was just an idea, then a bunch of people at CS Department put their heads together. And now here I am ! The Jarvis!")    
                        elif 'who are you' in query:
                            speak("I am your Assistant Sir! FRIDAY")
                            speak("i have all permissions about Devil Security server(DSS) and high-tech security")
                        elif 'open notepad' in query:
                            apppath = ""
                            os.startfile(apppath)
                            speak('Notepad is being started')
                        elif 'close notepad' in query:  
                            os.system("taskkill /f /im notepad++.exe")
                            speak('Notepad is closed')
                        elif 'college' in query:
                            speak('Your college name is Matsyodari Shikshan Santha Jalna,Sir') 
                        elif 'video song' in query:
                            apppath = ""
                            os.startfile(apppath)
                            speak('Your favorite song being played, sir')   
                        elif 'open files' in query:
                            apppath = "C:\\Windows\\explorer.exe"
                            os.startfile(apppath)
                            speak('Files are being opened')
                        elif 'close file' in query:
                            os.system("taskkill /f /im explorer.exe") 
                            speak('File Manager is closed')   
                        elif 'open cmd' in query:
                            apppath = "C:\\Windows\\System32\\cmd.exe"
                            os.startfile(apppath)
                            speak('terminal being opened') 
                        elif 'close cmd' in query:
                            os.system("Taskkill /f /im cmd.exe") 
                        # p= multiprocessing.Process(target=cmd.exe)
                            #os.terminate("C:\\Windows\\System32\\cmd.exe")
                            speak('terminal is closed')        
                        elif 'open chrome' in query:
                            apppath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                            os.startfile(apppath)
                            speak('chrome being opened') 
                        elif 'close chrome' in query:
                            os.system("taskkill /f /im chrome.exe") 
                            speak('Google Chrome is closed')      
                        elif 'open paint' in query:
                            apppath = "C:\\Windows\\System32\\mspaint.exe"
                            os.startfile(apppath)
                            speak('Paint being opened') 
                        elif 'close the paint' in query:
                            os.system("taskkill /f /im mspaint.exe") 
                            speak('Paint is closed')  
                        elif 'password' in query:
                            os.system('cmd \c "ipconfig"')   
                        elif 'password' in query:
                            os.system('cmd \c "ipconfig"')     
                        elif 'rain' in query: 
                            apppath = "C:\\Users\\Rahul\\Desktop\\rain22.jpg"
                            os.startfile(apppath)
                            speak('Image being opened')  
                        elif 'close image' in query:
                            os.system("taskkill /f /im Microsoft.Photos.exe") 
                            speak('Image being closed')  
                                
                        #else :
                        #   webbrowser.open(query)
                    
                       
Rahul()

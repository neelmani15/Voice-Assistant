# This is for Demo and it is same as main.py
import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pwt
import datetime
import wikipedia
import pyjokes as pj
import webbrowser as wb
import randfacts
from Selenium_web import infow
from Weather import *
from news import *

listenser = sr.Recognizer()
search=pt.init()
rate=search.getProperty('rate')
search.setProperty('rate','130')
voices=search.getProperty('voices')
search.setProperty('voice',voices[1].id)   # For male voice write voices[0].id
search.say('Hello Buddy My name is Siri')
search.runAndWait()
#search.say("Temprature of the location is " + str(temp()) + " Degree Celsius with a " + str(des()) + ", pressure is " + str(pres()) + ", humidity is "+ str(humid()) + " and wind speed is " + str(wind()))
#search.runAndWait()
def talk(text):
    search.say(text)
    search.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            #listenser.energy_threshold=20000
            #listenser.adjust_for_ambient_noise(search,1.5)
            print('Listening...')
            voice=listenser.listen(source)
            command=listenser.recognize_google(voice)
            command=command.lower()
            if 'siri' in command:
                command=command.replace('siri','')
                print(command)
    except:
        talk('Could not hear properly please say again')
        pass
    return command
def run_siri():
    command=take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk('Playing'+song)
        pwt.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M:%S')
        print(time)
        time1=datetime.datetime.now().strftime('%I:%M:%S  %p')   #For 12 hr format
        talk('Current time is '+time)
    elif 'about' in command:
        someone=command.replace('tell me about','')
        assistant = infow()
        assistant.get_info(someone)
        talk("searching {} in wikipedia".format(someone))
        #info=wikipedia.summary(someone,5)
        #print(info)
        #talk(info)
    elif 'temparature' in command:
        talk("Temprature of the location is " + str(temp()) + " Degree Celsius with a " + str(des()) + ", pressure is " + str(pres()) + ", humidity is " + str(humid()) + " and wind speed is " + str(wind()))
    elif 'joke' in command:
        t=pj.get_joke()
        print(t)
        talk(t)
    elif 'hotstar' in command:
        wb.open_new_tab('https://www.hotstar.com/in')
        talk('opening Hotstar')
    elif 'codechef' or 'codesafe' in command:
        wb.open_new_tab('https://www.codechef.com/')
        talk('opening codechef')
    elif 'leetcode' in command:
        wb.open_new_tab('https://leetcode.com/')
        talk('opening Leetcode')
    elif "fact" or "facts" in command:
        x=randfacts.get_fact()
        print(x)
        talk(x)
    elif "news" in command:
        array=news()
        for i in range(len(array)):
            talk(array[i])
            print(array[i])
    else:
        talk('Please say the command again')

while True:
    run_siri()

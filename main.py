import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pwt
import datetime
import wikipedia
import pyjokes as pj
import webbrowser as wb
import randfacts
from Selenium_web import *
from Weather import *
from news import *
import os
import smtplib
from dotenv import load_dotenv
load_dotenv()

API_Key_News=os.getenv("API_Key_News")
API_Key_Weather=os.getenv("API_Key_Weather")
gmail1=os.getenv("gmail1")
password=os.getenv("password")
gmail2=os.getenv("gmail2")
time = datetime.datetime.now()
search=pt.init('sapi5')
rate=search.getProperty('rate')
search.setProperty('rate','300')
voices=search.getProperty('voices')
search.setProperty('voice',voices[1].id)   # For male voice write voic es[0].id as name David # For Female ZIRA

# Talk or Speak Function
def talk(text):
    search.say(text)
    search.runAndWait()
# Wish Function to wish us according to time
def wishme():
    hr=int(time.hour)
    if hr>=0 and hr<12:
        talk("Good Morning!")
    elif hr>=12 and hr<16:
        talk("Good Afternoon!")
    elif hr>=16 and hr<19:
        talk("Good Evening!")
    else:
        talk("Good Night!")
# Function to send a mail
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(gmail1,password)
    server.sendmail(gmail1,to,content)
    server.close()

wishme()
talk('Hello Buddy My name is Siri, I am your Voice Assistant')
print('Today is '+ time.strftime("%d") + " of " + time.strftime("%B") + ", And its currently "+ (time.strftime("%I")) +":"+ (time.strftime("%M")) +":"+ (time.strftime("%S"))+ "  " +(time.strftime("%p")))
talk('Today is '+ time.strftime("%d") + " of " + time.strftime("%B") + ", And its currently "+ (time.strftime("%I")) +":"+ (time.strftime("%M")) + ":"+ (time.strftime("%S"))+" "+(time.strftime("%p")))
print("Temprature of the location is " + str(temp()) + " Degree Celsius with a " + str(des()) + ", pressure is " + str(pres()) + ", humidity is " + str(humid()) + " and wind speed is " + str(wind()))
talk("Temprature of the location is " + str(temp()) + " Degree Celsius with a " + str(des()) + ", pressure is " + str(pres()) + ", humidity is " + str(humid()) + " and wind speed is " + str(wind()))
talk("What can I do for you ?")
def take_command():
    """"
    It takes Microphone input from the user and Return String Output
    """
    listenser = sr.Recognizer()
    with sr.Microphone() as source:    #listenser.energy_threshold=20000     #listenser.adjust_for_ambient_noise(search,1.5)
        print('Listening...')
        listenser.energy_threshold=500
        listenser.pause_threshold=0.8
        voice=listenser.listen(source)
    try:
        print("Recognizing....")
        command=listenser.recognize_google(voice,language="en-in")
        print(command)
    except Exception as e:
        print(e)
        return "None"
    return command
def run_siri():
    command=take_command()
    command=command.lower()
    # Logic for the executing tasks based on command
    if 'news' in command:
        array,array1 = news()
        for i in range(len(array)):
            print(array[i])
            talk(array[i])
            print(array1[i])
            talk(array1[i])
    elif 'wikipedia' in command:
        someone=command.replace('wikipedia','')
        talk("Searching {} in wikipedia".format(someone))
        info=wikipedia.summary(someone,sentences=10)
        print(info)
        talk("According to wikipedia,"+str(info))
    # If we use "or" between elif command then it will repeatedly open the same browser
    elif 'open codechef' in command:
        wb.open_new_tab('https://www.codechef.com/')
        talk('Opening Codechef...')
        exit(0)
    elif 'open leetcode' in command:
        wb.open_new_tab('https://leetcode.com/')
        talk('Opening Leetcode...')
        exit(0)
    elif 'open stack overflow' in command:
        wb.open_new_tab('https://stackoverflow.com/')
        talk('Opening Stackoverflow...')
        exit(0)
    elif 'open hackerrank' in command:
        wb.open_new_tab('https://www.hackerrank.com/dashboard')
        talk('Opening HackerRank...')
        exit(0)
    elif 'open google meet' in command:
        talk('Please write a code to open Google meet')
        code=input("Enter the code to open Google meet: ")
        wb.open_new_tab('https://meet.google.com/'+code)
        talk('Opening Google meet...')
        exit(0)
    elif 'about' in command:
        someone=command.replace('tell me about','')       #info=wikipedia.summary(someone,5)   #print(info)    #talk(info)
        assistant = infow()
        assistant.get_info(someone)
        talk("searching {} in wikipedia".format(someone))
    elif 'joke' in command:
        t=pj.get_joke()
        print(t)
        talk(t)
    elif "play music" in command:
        music_dir='G:\\Audio'
        song=os.listdir(music_dir)
        print(song)
        os.startfile(os.path.join(music_dir,song[0]))
        exit(0)
    elif "play movie" in command:
        movies_dir='G:\South Movies'
        movie=os.listdir(movies_dir)
        print(movie)
        os.startfile(os.path.join(movies_dir,movie[0]))
        exit(0)
    elif "play" in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        pwt.playonyt(song)
        exit(0)
    elif "fact" in command:
        x=randfacts.get_fact()
        print("Did you know that, "+x)
        talk("Did you know that, "+x)
    elif "send email" in command:
        try:
            talk("What would I say on email ?")
            content=take_command()
            to=gmail2
            sendEmail(to,content)
            talk("Email has been sent!...")
        except Exception as e:
            print(e)
            talk("Sorry I am not able to send a email at the moment..")
    elif "ok" in command:
        exit(0)
    else:
        talk('Please say the command again')

while True:
    run_siri()
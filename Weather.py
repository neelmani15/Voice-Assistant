import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_Key_Weather=os.getenv("API_Key_Weather")
#city='Muzaffarpur'
# Taken Location from latitude and longitude of the location
api_address='http://api.openweathermap.org/data/2.5/weather?lat=26.1197&lon=85.3910&appid='+API_Key_Weather+'&units=metric'
res=requests.get(api_address)
json_data=res.json()
def temp():
    temprature=json_data["main"]["temp"]
    return temprature
def des():
    description=json_data["weather"][0]["description"]
    return description
#def des1():
 #   desc=json_data["weather"][0]["main"]
  #  return desc
def pres():
    pressure=json_data["main"]["pressure"]
    return pressure
def humid():
    humidity=json_data["main"]["humidity"]
    return humidity
def wind():
    speed=json_data["wind"]["speed"]
    return speed


#x = "Temprature of the location is " + str(temp()) + " Degree Celsius with a " + str(des()) + ", pressure is " + str(pres()) + ", humidity is " + str(humid()) + " and wind speed is" + str(wind())
#print(x)
#print("Temperature is ",temp())
#print("Weather is "+des())
#print("with "+des1())
#print("Pressure is ",pres())
#print("Humidity is ",humid())
#print("Spped of wind is ",wind())
#print(json_data)
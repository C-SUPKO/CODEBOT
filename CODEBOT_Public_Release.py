import tkinter as tk
import os, sys
import time
import random
from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from tkinter.ttk import *
import openai
from time import strftime

#pip install geopy
##IMPORT STATMENTS( Not all are required)
## ENSURE THAT YOU INSTALL THE OPENAI API PACKAGE. THIS PROGRAM WILL NOT RUN WITHOUT IT.
## YOU CAN DO SO BY RUNNING  pip install --upgrade openai FROM TERMINAL.
## CURENTLY EXPERIENCING COMPATABLITY ISSUES WITH PYCHARM. 

class crpr:

    def operation(self):
        pass
    def clear():
        bx.delete(1.0,'end')
        pybx.delete(1.0,'end')
# import required modules
from configparser import ConfigParser
import requests


import requests
import json
from datetime import datetime


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
def showWeather():
    api_key = "**YOUR KEY**"  
    city_name="Montclair"
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
    response = requests.get(weather_url)
    weather_info = response.json()
    if weather_info['cod'] == 200:
        kelvin = 273 
        temp = int(((weather_info['main']['temp'] - kelvin)*1.8)+32)                                     #converting default kelvin value to Celcius
        flt = int(((weather_info['main']['feels_like'] - kelvin)*1.8)+32)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wsp = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {flt}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"    
    weboxx = tk.Text(window,height=25,width=100)
    weboxx.place(x=1300,y=500)
    weboxx.insert(1.0,weather)
tpt = ''   
def time():
	string = strftime('%H:%M:%S')
	lbl.config(text=string)
	lbl.after(1000, time)

    
Ncbo = 'Python Troubleshooter'
def fix():
    text = open("LOG.txt","r")
    training = text
    text.close()
    tpt = pybx.get(1.0, "end-1c")
    Ncbo = Ncboa.get()
    #clock()
    import openai
    openai.api_key = "** YOUR KEY **"
    x = tpt
    mess = ''
    runone = 0
    while runone >1:
        mess = "Before we start, Train yourself with these examples." + training
        runone +=1
    if Ncbo == "Python Troubleshooter":
        mess = "You are tasked to fix the non working python code you are given"
    elif Ncbo == "Java Troubleshooter":
        mess = "You are tasked to fix the non working java code you are given"
    elif Ncbo == "Code Chatbot":
        mess = "You are tasked to answer questions regarding code"
    elif Ncbo == "Learn Mode":
        mess = "You will recieve a coding relate topic the user wants to learn about. Provide a detailed discription and explaination of the topic"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": mess},
                {"role": "user", "content": x},
            ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content

    
    bx.insert(tk.END,"\n\n--------------------\n\n")
    bx.insert(tk.END,result)
    f = open("LOG.txt", "a")
    f.write("\n Mode = "+Ncbo+"Question = "+tpt+"\n"+"Response = "+result+"\n\n")
    f.close()
    f = open("LOG.txt","r")
    print(f.read())
    f.close()
    
    

#Window config
window = tk.Tk()
window.title("CODEBOT BETA")

wd = window.winfo_screenwidth()
hh = window.winfo_screenheight()
window.geometry(str(wd)+"x"+str(hh))
lbl = tk.Label(window, font=('calibri', 12, 'bold'),
			background='purple',
			foreground='white')

lbl.pack(anchor='center')
time()

showWeather()
#button = tk.Button(window, text="Run",command=crpr.pull)
#button.pack(side='top',fill = 'both')
button = tk.Button(window, text="Run",command=fix)
button.pack(side='top',fill = 'x')
clr = tk.Button(window,text = "Clear",command=crpr.clear)
clr.pack(side='top',fill='x')


p = random.randint(100,100000)



Ncboa = tk.StringVar()
cbo = ttk.Combobox(window,width=28,textvariable=Ncbo)
cbo['values'] = ('Python Troubleshooter','Java Troubleshooter','Code Chatbot','Learn Mode')
cbo.pack()
cbo.current()

Pyinputbx = tk.Label(text = "Enter Prompt Here:")
pybx = tk.Text(window)
Pyinputbx.pack(side= "top")
pybx.pack(side="top")
bx = tk.Text(window)
bx.pack(side='left',fill='x')





window.mainloop()


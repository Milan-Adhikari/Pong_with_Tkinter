import tkinter as tk
from tkinter import *
import requests
from PIL import Image,ImageTk
import tkinter.font as font

# API =fb90eacf13513e0adf587ed068078130
# URL =api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

HEIGHT = 420
WIDTH = 600

root = tk.Tk()
root.title('Weather')
root.configure(height = HEIGHT,width = WIDTH)
root.resizable(False,False)

#canvas inside whom frames will be placed
canvas = tk.Canvas(root)
canvas.place(x=0,y=0,relwidth =1,relheight =1)

#background image
imag = ImageTk.PhotoImage(file = 'weather.png')
img_label = Label(canvas, image = imag)
img_label.place(relheight =1, relwidth =1)

def format(weather):
    try:
        country = weather['sys']['country']
        name = weather['name']
        temp = weather['main']['temp']
        feels = weather['main']['feels_like']
        des = weather['weather'][0]['description']

        final_str= 'Country:   %s\nCity:   %s\nTemperature:   %s\nFeels Like:   %s\nCondition:   %s\n'%(country,name,temp,feels,des)
    except:
        final_str = 'There was an Error Retrieving Information'
    return (final_str)

# function thats executed after button click
def get_weather(city,frame2):
    key = 'fb90eacf13513e0adf587ed068078130'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameter = {'APPID' : key,'q' : city , 'units' : 'Metric' }
    response = requests.get(url,params=parameter)
    weather = response.json()
    label2['text'] = format(weather)

#frame for entry
frame1 = tk.Frame(canvas,bg='#CC00CC',bd=5)
frame1.place(relx = 0.15,rely = 0.2,relheight =0.1,relwidth =0.7)

#entry inside frame1
entry = tk.Entry(frame1,font =('showcard gothic',13),fg='#FF0033')
entry.place(relheight =1, relwidth =0.685)

#button inside frame1
btn = tk.Button(frame1,font =('showcard gothic',13),fg ='#FF0033', text ='Get Weather',command = lambda: get_weather(entry.get(),frame2))
btn.place(relx = 0.7,relheight = 1,relwidth = 0.3)

#frame for output
frame2 = tk.Frame(canvas,bg='#CC00CC',bd=10)
frame2.place(relx = 0.15,rely =0.4,relheight = 0.4,relwidth = 0.7)
frame3 = tk.Frame(frame2,bg='white')
frame3.place(relx = 0.006,rely=0.022,relheight = 0.97,relwidth = 0.99)
label2 = Label(frame3,font =('showcard gothic',12),bg='white',fg='black',anchor ='w',justify = LEFT)
label2.place(relx=0,rely=0.14)
print(tk.font.families())

root.mainloop()
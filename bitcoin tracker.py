import tkinter as tk
from tkinter import *
import requests
from PIL import Image,ImageTk
import tkinter.font as font
from datetime import datetime

# API =ce025c7d0ff3833e142051ffdb4aebcff578803442d93d5435eef93d62b945e5
# URL ='https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR'

HEIGHT = 420
WIDTH = 600

root = tk.Tk()
root.title('Bitcoin Tracker')
root.configure(height = HEIGHT,width = WIDTH)
root.resizable(False,False)

#canvas inside whom frames will be placed
canvas = tk.Canvas(root)
canvas.place(x=0,y=0,relwidth =1,relheight =1)

#background image
imag = ImageTk.PhotoImage(file = 'weather.png')
img_label = Label(canvas, image = imag)
img_label.place(relheight =1, relwidth =1)

#function

def format_price(response):
    try:
        btc = response['BTC']
    except:
        final_str = 'There was an error'

    final_str = 'BTC: %s\n'%(btc)
    return(final_str)
def nepali_convert(response):
    us = response['USD']
    nep = (117.22)*us
    final = 'NRs: %s'%nep
    time = datetime.now().strftime('%H:%M:%S')
    label4['text'] = 'Updated at: %s'%(time)
    return(final)

def tracker():
    # key = 'ce025c7d0ff3833e142051ffdb4aebcff578803442d93d5435eef93d62b945e5'
    url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR'
    response = requests.get(url).json()
    label2['text'] = format_price(response)
    label3['text'] = nepali_convert(response)
    canvas.after(1000,tracker)

#frame for entry
frame1 = tk.Frame(canvas,bg='#CC00CC',bd=5)
frame1.place(relx =0.35,rely = 0.2,relheight =0.1,relwidth =0.3)

#button inside frame1
btn = tk.Button(frame1,font =('showcard gothic',13),fg ='#FF0033', text ='Start',command = tracker)
btn.place(relheight = 1,relwidth = 1)

#frame for output
frame2 = tk.Frame(canvas,bg='#CC00CC',bd=10)
frame2.place(relx = 0.15,rely =0.4,relheight = 0.4,relwidth = 0.7)
frame3 = tk.Frame(frame2,bg='white')
frame3.place(relx = 0.006,rely=0.022,relheight = 0.97,relwidth = 0.99)
label2 = Label(frame3,font =('showcard gothic',12),bg='white',fg='black',anchor ='center',justify = LEFT)
label2.place(relx=0.27,rely=0.3,)
label3 =Label(frame3,font =('showcard gothic',12),bg='white',fg='black',anchor ='center',justify = LEFT)
label3.place(relx = 0.27,rely =0.5)
label4 =Label(frame3,font =('showcard gothic',12),bg='white',fg='black',anchor ='center',justify = LEFT)
label4.place(relx = 0.27,rely =0.7)
label5 =Label(frame3,text ='Live Bitcoin Tracking',font =('showcard gothic',12),bg='white',fg='black',anchor ='center',justify = LEFT)
label5.place(relx = 0.27,rely =0.1)

root.mainloop()
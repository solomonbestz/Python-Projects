from tkinter import *
import time
from random import randint
import threading


window = Tk()

window.title("Threading")
window.geometry("500x400")


def five_seconds():    
    time.sleep(5)
    my_label.config(text="5 Seconds Is Up")

def rando():
    random_label.config(text=f"Random Number: {randint(1, 100)}")


my_label = Label(window, text="Hello There!")
my_label.pack(pady=20)

my_button1 = Button(window, text="5 Seconds", command=threading.Thread(target=five_seconds).start())
my_button1.pack(pady=20)

my_button2 = Button(window, text="Pick Random Number", command=rando)
my_button2.pack(pady=20)

random_label = Label(window, text="")
random_label.pack(pady=20)


window.mainloop()
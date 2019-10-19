from tkinter import *
import serial
import time

arduinoData = serial.Serial('com8', 9600)
def led_on():
    arduinoData.write(b'1')

def led_off():
    arduinoData.write(b'0')

window = Tk()
btn = Button(window, text='led1 on', command= led_on)
btn1 = Button(window, text='led1 off', command=led_off)

btn.grid(row=0,column=1)
btn1.grid(row=1, column=1)

window.mainloop()

input('press enter to exit')

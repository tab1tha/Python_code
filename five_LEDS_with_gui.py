from tkinter import *
import serial
import time


arduinoData = serial.Serial('com8', 9600)
def led1_on():
    arduinoData.write(b'1')

def led1_off():
    arduinoData.write(b'0')

def led2_on():
    arduinoData.write(b'A')

def led2_off():
    arduinoData.write(b'B')

def led3_on():
    arduinoData.write(b'C')

def led3_off():
    arduinoData.write(b'D')

def led4_on():
    arduinoData.write(b'E')

def led4_off():
    arduinoData.write(b'F')

def led5_on():
    arduinoData.write(b'G')

def led5_off():
    arduinoData.write(b'H')
    
window = Tk()
btn11 = Button(window, text='led1 on', command= led1_on)
btn12 = Button(window, text='led1 off', command=led1_off)
btn21 = Button(window, text='led2 on', command=led2_on)
btn22 = Button(window, text='led2 off', command=led2_off)
btn31 = Button(window, text='led3 on', command=led3_on)
btn32 = Button(window, text='led3 off', command=led3_off)
btn41 = Button(window, text='led4 on', command=led4_on)
btn42 = Button(window, text='led4 off', command=led4_off)
btn51 = Button(window, text='led5 on', command=led5_on)
btn52 = Button(window, text='led5 off', command=led5_off)

btn11.pack()
btn12.pack()
btn21.pack()
btn22.pack()
btn31.pack()
btn32.pack()
btn41.pack()
btn42.pack()
btn51.pack()
btn52.pack()


window.mainloop()

input('press enter to exit')

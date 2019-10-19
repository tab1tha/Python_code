import tkinter as tk
import tk_tools
import serial
import time

root = tk.Tk()
arduinoData = serial.Serial('com8', 9600)

batV_gauge = tk_tools.Gauge(root, height=120, width=250,
                            max_value=5, min_value=0,
                            label='Bat voltage',
                            unit='V',
                            divisions=1,
                            )
batV_gauge.grid(row=0, column=1, sticky='news')

# initialization of some variables.
count = 0
up = True

def update_gauge():
    global count, up

    increment = 30

    if up:
        count += increment
        if count > 5000:
            up = False
    else:
        count -= increment

        if count <= 0.0:
            up = True

    # update the gauges according to their value
    batV_gauge.set_value(count / 1000)
    arduinoData.write(b'count/1000')
    root.after(50, update_gauge)

if __name__ == '__main__':
    root.after(100, update_gauge)

    root.mainloop()
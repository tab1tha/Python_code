from tkinter import *
#initialise a window
window = Tk()
window.title('heyo Tabi')
#permanent size of window so that it does not keep changing with respect to text content
window.geometry('350x200')

#text in window and position where text will be printed
lbl = Label(window, text='Name please', font=("Arial Bold", 25), fg='pink')
lbl.grid(column=0, row=0)

#create an input box
box = Entry(window, width=10)
box.grid(column=1, row=0)
#to put the cursor in the prompt entry box by default
box.focus()

#button formed and it's clicking event defined
def clicked():
    #lbl.configure(text='you clicked me!!!')
    res = 'Welcome back ' + box.get()
    lbl.configure(text=res)
btn = Button(window, text='confirm', bg='white',fg='plum', command=clicked)
btn.grid(column=2, row =0)

#add a combobox widget, i.e drop down menu
from tkinter.ttk import *
combo = Combobox(window)
combo["values"] = (1,2,3,4,5, 'text')
combo.current(1)
combo.grid(column=0, row=5)
#combo.get() is used to get user's choice

#checkbutton
#create tkinter variable and set checkstate of button
chk_state=BooleanVar() #IntVar() can be used whereby the toggle values will be 0 and 1
chk_state.set(True) #set checkstate as ticked
chk= Checkbutton(window, text='tick if you agree',var= chk_state)
chk.grid(column=0, row=4)

#radio buttons implement exclusive OR
rad1 = Radiobutton(window, text='first', value=1) #the values are random numbers but must be different for each button
rad2 = Radiobutton(window, text='second', value=2)
rad3 = Radiobutton(window, text='third', value=8)
#define click event
rad1.grid(column=0, row=1)
rad2.grid(column=0, row=2)
rad3.grid(column=0, row=3)

##to get and use info from radio buttons do this
#selected = IntVar()
#rad1 = Radiobutton(window,text='First', value=1, variable=selected)
#rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
#rad3 = Radiobutton(window,text='Third', value=3, variable=selected)
#def clicked():
#    print(selected.get())
#btn = Button(window, text="Click Me", command=clicked)

#add a scrolled text window
from tkinter import scrolledtext
scrl = scrolledtext.ScrolledText(window, width=40, height=10)
scrl.grid(column=0, row=6 )
#to put some text in the scroll widget
scrl.insert(INSERT, 'you can write now')
##scrl.delete(1.0, END) #to clear scrolledtext widget


window.mainloop()

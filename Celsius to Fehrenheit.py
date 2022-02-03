from tkinter import *

# Makes the window 1 (the main window)
window = Tk()
window.title('Celsius To Fehrenheit Convertor')
window.geometry('700x400+300+140')

# make the commands
def Convert():
    Num = Number.get()
    Num = float(Num)
    result = (Num*9/5)+32
    Label(text=result).place(x=10, y=65)    
def kill():
    window.destroy()

#Labels & Entries & Buttons (tools)
Ask_for_number = Label(text='Enter your Celsius degrees:')
Number = Entry()
MyButton = Button(text='convert', command=Convert)
quit_Button = Button(text='quit', command=kill)

#sort the page view
Ask_for_number.place(x=10 ,y=10)
Number.place(x=70, y=10)
MyButton.place(x=10, y=40)
quit_Button.place(x=70, y=40)

window.mainloop()

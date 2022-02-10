from tkinter import *

#! Makes the main window
window = Tk()
window.title('Celsius To Fehrenheit Convertor')
window.geometry('400x200+200+70')
window.configure(bg="#3f3f3f")
window.resizable(width=False, height=False) # Unresizable

#! make the commands
def Convert():
    Num = float(number.get())
    Label(text=f"{(Num*9/5)+32}°F", bg="#3f3f3f", fg="white").place(x=230, y=60,)
def kill():
    window.destroy()

#! Labels & Entries & Buttons (tools)
Ask_for_number = Label(text='Enter your Celsius number:', bg="#3f3f3f", fg="white", highlightthickness=0, bd=0)
number = Entry(bg="#36393f", highlightthickness=0, fg="white", bd=0)
MyButton = Button(text='convert', command=Convert, background="#36393f", fg="white", highlightthickness=0)
quit_Button = Button(text='quit', command=kill, background="#36393f", fg="white", highlightthickness=0)

#! sort the page view
Ask_for_number.place(x=10 ,y=10)
number.place(x=200, y=10)
MyButton.place(x=10, y=40)
quit_Button.place(x=90, y=40)

window.mainloop()

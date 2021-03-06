from tkinter import *


def temperature():
    window3 = Toplevel()
    window3.title("Temperature Converter")
    window3.geometry('370x200+0+0')
    window3.resizable(width=False, height=False)
    window3.configure(bg='#1b1c1b')

    def from_celsius():
        # convert celsius to ft
        ft = float(length_screen.get()) * 9/5 +32

        # convert celsius to kelvin
        kelvin = float(length_screen.get()) + 273.15

        # convert celsius to rankine
        rankine = float(length_screen.get()) * 1.8 + 32 + 459.67

        # Enters the converted celsius to
        # the text widget
        text1.delete("1.0", END)
        text1.insert(END, ft)

        text2.delete("1.0", END)
        text2.insert(END, kelvin)

        text3.delete("1.0", END)
        text3.insert(END, rankine)

    # Create the Label widgets
    label_1 = Label(window3, text="Enter the temperature in Celsius", bg='red', fg='white', font=('20'))
    length_screen = StringVar()
    label_2 = Entry(window3, textvariable=length_screen, bg='#4f6658', fg='white', font=('10'))
    label_3 = Label(window3, text='Fahrenheit', bg='#1b1c1b', fg='white')
    label_4 = Label(window3, text='Kelvin', bg='#1b1c1b', fg='white')
    label_5 = Label(window3, text='Rankine', bg='#1b1c1b', fg='white', font=('20'))

    # Create the Text Widgets
    text1 = Text(window3, height=1, width=20)
    text2 = Text(window3, height=1, width=20)
    text3 = Text(window3, height=1, width=20)

    # Create the Button Widget
    b1 = Button(window3, text="Convert", fg="white", bg="#1f211f", activebackground="#71c971", command=from_celsius)
    label_stuff_3 = Label(window3, text='   ')
    label_stuff_5 = Label(window3, text='   ')

    #calling widgets and buttons
    label_1.grid(row=1, column=1)
    label_2.grid(row=2, column=1)
    label_3.grid(row=6, column=0)
    label_4.grid(row=7, column=0)
    label_5.grid(row=8, column=0)
    text1.grid(row=6, column=1)
    text2.grid(row=7, column=1)
    text3.grid(row=8, column=1)
    b1.grid(row=4, column=1)
    label_stuff_3.grid(row=5, column=1)
    label_stuff_3.configure(bg='#1b1c1b')
    label_stuff_5.grid(row=3, column=1)
    label_stuff_5.configure(bg='#1b1c1b')

    window3.mainloop()

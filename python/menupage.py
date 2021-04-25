import tkinter
import time

def display(panel, window):
    panel.pack_forget()

    # Frame
    menu_page = tkinter.Frame(
        window,
        bg="white",
        width=800,
        height=600
    )
    menu_page.pack()

    menu_page = tkinter.Label(
        window,
        text="Welcome to SwabTaste",
        bg="white",
        font=("arial", 25, 'bold')
    )
    menu_page.place(x=220, y=20)

    menu_page = tkinter.Label(
        window,
        text="ALL-YOU-CAN-EAT-BUFFET",
        bg="white",
        font=("arial", 13, 'bold')
    )
    menu_page.place(x=290, y=70)



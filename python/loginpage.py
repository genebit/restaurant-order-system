import tkinter

import login
import register

def display(window):
    # Frame
    login_page = tkinter.Frame(
        window,
        bg="white",
        width=800,
        height=600
    )
    login_page.pack()

    # Elements
    logo = tkinter.Label(
        window,
        text="SWAB TASTE",
        bg="white",
        font=("Castellar", 25)
    )
    logo.place(x=300, y=100)

    login_button = tkinter.Button(
        window,
        text = "Login",
        font=("sans-serif", 12),
        bg = "red",
        width = 30,
        height = 2,
        command=lambda: login.display(login_page, window)
    )
    login_button.place(x=100, y=300)

    register_button = tkinter.Button(
        window,
        text = "Register",
        font=("sans-serif", 12),
        bg = "red",
        width = 30,
        height = 2,
        command =lambda: register.display(login_page, window)
    )
    register_button.place(x=400, y=300)
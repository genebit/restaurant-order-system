import tkinter

import loginpage

def back_to_login(thispanel, window):
    thispanel.pack_forget()
    loginpage.display(window)

def display(prev, window):
    prev.pack_forget()
    
    # Frame
    login_page = tkinter.Frame(
        window,
        bg="white",
        width=800,
        height=600
    )
    login_page.pack()

    # Back Button
    back_button = tkinter.Button(
        window,
        text = "<",
        font=("sans-serif", 12),
        width = 5,
        height = 2,
        command=lambda: back_to_login(login_page, window)
    )
    back_button.place(x=100, y=100)
    
    # Elements
    header = tkinter.Label(
        window,
        text="LOGIN",
        bg="white",
        font=("Castellar", 25)
    )
    header.place(x=250, y=50)

    username_text = tkinter.Label(
        window,
        text="Username:",
        bg="white",
        font=("sans-serif", 15)
    )
    username_text.place(x=250, y=110)

    username = tkinter.Entry(
        window,
        width=30,
        font=("sans-serif", 15)
    )
    username.place(x=250, y=150)

    password_text = tkinter.Label(
        window,
        text="Password:",
        bg="white",
        font=("sans-serif", 15)
    )
    password_text.place(x=250, y=190)

    password = tkinter.Entry(
        window,
        width=30,
        show="•",
        font=("sans-serif", 15)
    )
    password.place(x=250, y=230)
    
    login_button = tkinter.Button(
        window,
        text="Login",
        font=("sans-serif", 12),
        bg="red",
        width=20
    )
    login_button.place(x=330, y=300)

    
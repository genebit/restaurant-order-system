import tkinter

import loginpage

def back_to_login(thispanel, window):
    thispanel.pack_forget()
    loginpage.display(window)

def display(prev, window):
    prev.pack_forget()
    
    # Frame
    register_page = tkinter.Frame(
        window,
        bg="white",
        width=800,
        height=600
    )
    register_page.pack()

    # Back Button
    back_button = tkinter.Button(
        window,
        text="<",
        font=("sans-serif", 12),
        width=5,
        height=1,
        command=lambda: back_to_login(register_page, window)
    )
    back_button.place(x=150, y=105)

    # Elements
    header = tkinter.Label(
        window,
        text="REGISTRATION",
        bg="white",
        font=("arial", 25, 'bold')
    )
    header.place(x=275, y=100)

    username_text = tkinter.Label(
        window,
        text="Username:",
        bg="white",
        font=("sans-serif", 15)
    )
    username_text.place(x=250, y=200)

    username = tkinter.Entry(
        window,
        width=30,
        font=("sans-serif", 15)
    )
    username.place(x=250, y=250)

    password_text = tkinter.Label(
        window,
        text="Password:",
        bg="white",
        font=("sans-serif", 15)
    )
    password_text.place(x=250, y=300)

    password = tkinter.Entry(
        window,
        width=30,
        show="•",
        font=("sans-serif", 15)
    )
    password.place(x=250, y=350)
    
    register_button = tkinter.Button(
        window,
        text = "Register",
        font=("sans-serif", 12),
        bg="red",
        width=20
        )
    register_button.place(x=330, y=450)
    


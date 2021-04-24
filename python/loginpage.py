import tkinter

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
        
    )

    login_button = tkinter.Button(
        window,
        text = "Login",
        font=("sans-serif", 12),
        bg = "red",
        width = 30,
        height = 2
        # command =login
        )
    login_button.place(x=100, y=300)

    register_button = tkinter.Button(
        window,
        text = "Register",
        font=("sans-serif", 12),
        bg = "red",
        width = 30,
        height = 2
        # command =register
        )
    register_button.place(x=400, y=300)
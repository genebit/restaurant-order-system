import tkinter
import sqlite3

import loginpage

username = 0
password = 0

user_exist = False
empty = ""

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

    global username
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

    global password
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
        width=20,
        command=login
    )
    login_button.place(x=330, y=300)

def login():
    if username.get() is not empty and password.get() is not empty:
        # Check to the database if the user exist
        if_user_exist(username.get(), password.get())
        print(user_exist)
        
    else:
        print("Missing field")

def if_user_exist(name, password):
    try:    
        file_destination = "./database/users.db"

        connection = None
        connection = sqlite3.connect(file_destination)
        
        cur = connection.cursor()
        cur.execute(f"SELECT Username, Password FROM Accounts WHERE Username='{name}' AND Password='{password}'")
        
        results = cur.fetchall()

        global user_exist

        # for items in results:
        #     if items[0] is not []:
        #         user_exist = True
        #     else:
        #         user_exist = False

        connection.close()

    except sqlite3.Error as err:
        print(err)

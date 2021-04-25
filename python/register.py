import tkinter
import sqlite3

import loginpage
import menupage

username = 0
password = 0
user_exist = False

register_page = 0

empty = ""

def back_to_login(thispanel, window):
    thispanel.pack_forget()
    loginpage.display(window)

def display(prev, window):
    prev.pack_forget()
    
    # Frame
    global register_page
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

    global username
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

    global password
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
        width=20,
        command=lambda: register(window)
        )
    register_button.place(x=330, y=450)

def register(window):
    if username.get() is not empty and password.get() is not empty:
        if_user_exist(username.get(), password.get())
        
        if user_exist == False:
            # Register
            register_user(username.get(), password.get())
            menupage.display(register_page, window)
        else:
            print("User found! Use login")
        
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
        
        try:
            username = results[0][0]
            password = results[0][1]
            
            if username is not [] and password is not []:
                user_exist = True
        except:
            username = None
            password = None

            user_exist = False
        connection.close()

    except sqlite3.Error as err:
        print(err)

def register_user(username, password):
    try:    
        file_destination = "./database/users.db"

        connection = None
        connection = sqlite3.connect(file_destination)
        
        cur = connection.cursor()
        inserted_data = "INSERT INTO Accounts(Username, Password)VALUES(?, ?);"
        
        cur.execute(inserted_data, (username, password))
        connection.commit()
        connection.close()

        print("Finished sending to database")
    except sqlite3.Error as err:
        print(err)
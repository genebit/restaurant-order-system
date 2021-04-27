import tkinter
import sqlite3
from PIL import ImageTk, Image

import menupage

loginPage = None
usernameInputField = None
passwordInputField = None
empty = ""

def show(window, img):
    # Frame
    global loginPage
    loginPage = tkinter.Frame(window)
    loginPage.pack()

    # Image Background Layout
    image = tkinter.Label(loginPage, image=img)
    image.pack()

    # Elements
    global usernameInputField
    usernameInputField = tkinter.Entry(loginPage, font=("sans-serif", 16), borderwidth=0, highlightthickness=0, width=37)
    usernameInputField.place(x=175, y=245)

    global passwordInputField
    passwordInputField = tkinter.Entry(loginPage, font=("sans-serif", 16), borderwidth=0, highlightthickness=0, width=37, show="•")
    passwordInputField.place(x=175, y=305)

    # Buttons
    loginButton = tkinter.Button(
        loginPage, text="LOGIN", font=("Roboto", 18), 
        borderwidth=0, highlightthickness=0, width=9,
        command=lambda : login(window, usernameInputField, passwordInputField)
    )
    loginButton.place(x=410, y=358)
    
    registerButton = tkinter.Button(
        loginPage, text="REGISTER", font=("Roboto", 18), 
        borderwidth=0, highlightthickness=0, width=9,
        # command=login : register()
    )
    registerButton.place(x=576, y=358)

def login(window, username, password):
    print("Logging user...")
    if usernameInputField.get() is not empty and passwordInputField.get() is not empty:
        print("Fields are satisfied, checking user if exist...")

        path = "./database/users.db"
        try:
            connection = None
            connection = sqlite3.connect(path)
            
            cur = connection.execute(f"SELECT * FROM Accounts WHERE Username='{username.get()}' AND Password='{password.get()}';")
            results = cur.fetchall()

            if results is not []:
                print("Authentication satisfied. Sending to Menu page...")
                menupage.show(loginPage, window)
            else:
                print("User is not recorded! Please Register and try again.")

        except sqlite3.Error as err:
            print(f"An error occured when 'Logging in', cause: {err}")
    else:
        print("Please fill in the fields")
    
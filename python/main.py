import tkinter
import sqlite3
from PIL import Image, ImageTk

import loginpage

window = tkinter.Tk()

empty = ""

# Login fields
l_img_path = "./img/login.png"
l_img = ImageTk.PhotoImage(Image.open(l_img_path))

# Register fields
r_usernameInputField = None
r_passwordInputField = None
r_img_path = "./img/registration.png"
r_img = ImageTk.PhotoImage(Image.open(r_img_path))

def login():
    print("Logging user...")
    if l_usernameInputField.get() is not empty and l_passwordInputField.get() is not empty:
        print("Fields are satisfied, checking user if exist...")

        path = "./database/users.db"
        try:
            connection = None
            connection = sqlite3.connect(path)
            
            cur = connection.execute(f"SELECT * FROM Accounts WHERE Username='{l_usernameInputField.get()}' AND Password='{l_passwordInputField.get()}';")
            results = cur.fetchall()

            if results is not []:
                print("Authentication satisfied. Sending to Menu page...")
            else:
                print("User is not recorded! Please Register and try again.")

        except sqlite3.Error as err:
            print(f"An error occured when 'Logging in', cause: {err}")
    else:
        print("Please fill in the fields")

def register():
    print("Registering...")

    l_page.pack_forget()

    # Frame
    r_page = tkinter.Frame(window, width=800, height=620, bg="black")
    r_page.pack()

    # Image Background
    r_img_holder = tkinter.Label(r_page, image=r_img)
    r_img_holder.pack()

    # Elements
    r_usernameInputField = tkinter.Entry(r_page, font=("sans-serif", 16), borderwidth=0, highlightthickness=0, width=37)
    r_usernameInputField.place(x=175, y=245)

    r_passwordInputField = tkinter.Entry(r_page, font=("sans-serif", 16), borderwidth=0, highlightthickness=0, width=37, show="•")
    r_passwordInputField.place(x=175, y=305)

try:

    print("Running...")
    
    # Frame
    l_page = tkinter.Frame(window, width=800, height=620)
    l_page.pack()

    # Image Background
    l_img_holder = tkinter.Label(l_page, image=l_img)
    l_img_holder.pack()

    # Elements
    l_usernameInputField = tkinter.Entry(l_page, font=("sans-serif", 16), borderwidth=0, highlightthickness=0, width=37)
    l_usernameInputField.place(x=175, y=245)

    l_passwordInputField = tkinter.Entry(l_page, font=("sans-serif", 16), borderwidth=0, highlightthickness=0, width=37, show="•")
    l_passwordInputField.place(x=175, y=305)

    # Buttons
    login_button = tkinter.Button(
        l_page, text="LOGIN", font=("Roboto", 18), 
        borderwidth=0, highlightthickness=0, width=9,
        bg="white", command=login
    )
    login_button.place(x=410, y=358)

    register_button = tkinter.Button(
        l_page, text="REGISTER", font=("Roboto", 18), 
        borderwidth=0, highlightthickness=0, width=9,
        bg="white", command=register
    )
    register_button.place(x=576, y=358)
    

    # Window Properties
    window.geometry("800x620")
    window.config(background="white")
    window.title("Swab Taste!")
    window.mainloop()

except Exception as err:
    print(f"An error occured when running the App, cause: {err}")

    
import tkinter
import sqlite3
from PIL import Image, ImageTk

import menupage

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

# Menu page
m_img_path = "./img/menupage.png"
m_img = ImageTk.PhotoImage(Image.open(m_img_path))

def login():
    print("* Logging user...")

    if l_usernameInputField.get() is not empty and l_passwordInputField.get() is not empty:
        print("* Fields are satisfied, checking user if exist...")

        path = "./database/users.db"
        try:
            connection = None
            connection = sqlite3.connect(path)
            
            cur = connection.cursor()
            cur.execute(f"SELECT * FROM Accounts WHERE Username='{l_usernameInputField.get()}' AND Password='{l_passwordInputField.get()}';")
            results = cur.fetchone()

            if results != None:
                print("* Authentication satisfied. Sending to Menu page...")
                menupage.show(l_page, window, m_img)
            else:
                print("* User is not recorded! Please Register and try again.")

            connection.close()

        except sqlite3.Error as err:
            print(f"An error occured when 'Logging in', cause: {err}")
    else:
        print("* Please fill in the fields")

def show_register_page():
    print("* Registering...")

    l_page.pack_forget()

    # Frame
    r_page = tkinter.Frame(window, width=800, height=620, bg="black")
    r_page.pack()

    # Image Background
    r_img_holder = tkinter.Label(r_page, image=r_img)
    r_img_holder.pack()

    # Elements
    global r_usernameInputField
    r_usernameInputField = tkinter.Entry(r_page, font=("sans-serif", 16), borderwidth=0, highlightthickness=0, width=37)
    r_usernameInputField.place(x=175, y=245)

    global r_passwordInputField
    r_passwordInputField = tkinter.Entry(r_page, font=("sans-serif", 16), borderwidth=0, highlightthickness=0, width=37, show="•")
    r_passwordInputField.place(x=175, y=305)

    register_button = tkinter.Button(
        r_page, text="REGISTER", font=("Roboto", 18), 
        borderwidth=0, highlightthickness=0, width=9,
        bg="white", command=lambda: register(r_page)
    )
    register_button.place(x=485, y=362)

    back_button = tkinter.Button(
        r_page, text="<", font=("Roboto", 20), 
        borderwidth=0, highlightthickness=0, width=1,
        bg="white", command=lambda: back(r_page)
    )
    back_button.place(x=44, y=178)

def register(panel):
    print("* Checking into the database")

    if r_usernameInputField.get() is not empty and r_passwordInputField.get() is not empty:
        print("* Fields are satisfied, checking user if exist...")

        path = "./database/users.db"
        try:
            connection = None
            connection = sqlite3.connect(path)
            
            cur = connection.cursor()
            cur.execute(f"SELECT * FROM Accounts WHERE Username='{r_usernameInputField.get()}';")
            results = cur.fetchone()

            if results != None:
                print("* User is already recorded, Please use the login...")
            else:
                print("* Registering user...")
                inserted_data = f"INSERT INTO Accounts(Username, Password)VALUES(?, ?);"

                cur.execute(inserted_data, (r_usernameInputField.get(), r_usernameInputField.get()))
                connection.commit()
                print("* Finished Registered user, Redirecting to Menu")

                menupage.show(panel, window, m_img)

            connection.close()
            
        except sqlite3.Error as err:
            print(f"An error occured when 'Registering user', cause: {err}")
    else:
        print("* Please fill in the fields")

def back(panel):
    print("* Closing registration page")
    
    panel.destroy()
    l_page.pack()

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
    login_button.place(x=409, y=358)

    register_button = tkinter.Button(
        l_page, text="REGISTER", font=("Roboto", 18), 
        borderwidth=0, highlightthickness=0, width=9,
        bg="white", command=show_register_page
    )
    register_button.place(x=575, y=358)
    
    # Window Properties
    window.geometry("800x620")
    window.config(background="white")
    window.title("Swab Taste!")
    window.mainloop()

except Exception as err:
    print(f"An error occured when running the App, cause: {err}")
import tkinter 
import sqlite3
from PIL import Image, ImageTk


window = tkinter.Tk()
import menupage
    
database_path = "./database/users.db"
empty = ""

# Register fields
register_usernameField = None
register_passwordField = None
register_image_path = "./img/registration.png"
register_image = ImageTk.PhotoImage(Image.open(register_image_path))

# Menu page
menu_img_path = "./img/menupage.png"
menu_image = ImageTk.PhotoImage(Image.open(menu_img_path))

##########################################
def login():
    print("* Logging user...")

    if login_usernameField.get() != empty and login_passwordField.get() != empty:
        print("* Fields are satisfied, checking user if exist...")
    
        try:
            connection = None
            connection = sqlite3.connect(database_path)
            
            cur = connection.cursor()
            cur.execute(f"SELECT * FROM Accounts WHERE Username='{login_usernameField.get()}' AND Password='{login_passwordField.get()}';")
            results = cur.fetchone()

            if results != None:
                print("* Authentication satisfied. Sending to Menu page...")
                menupage.show(login_page, window, menu_image)
            else:
                print("* User is not recorded! Please Register and try again.")

            connection.close()

        except sqlite3.Error as err:
            print(f"An error occured when 'Logging in', cause: {err}")
    else:
        print("* Please fill in the fields")

def show_register_page():
    print("* Registering...")

    login_page.pack_forget()

    # Frame
    register_page = tkinter.Frame(window, width=800, height=620, bg="black")
    register_page.pack()

    # Image Background
    register_img_holder = tkinter.Label(register_page, image=register_image)
    register_img_holder.pack()

    # Elements
    global register_usernameField
    register_usernameField = tkinter.Entry(register_page, font=("Roboto", 16), borderwidth=0, highlightthickness=0, width=37)
    register_usernameField.place(x=178, y=245)

    global register_passwordField
    register_passwordField = tkinter.Entry(register_page, font=("Roboto", 16), borderwidth=0, highlightthickness=0, width=37, show="•")
    register_passwordField.place(x=178, y=305)

    register_button = tkinter.Button(
        register_page, text="REGISTER", font=("Roboto", 16), 
        borderwidth=0, highlightthickness=0, width=11,
        bg="white", command=lambda: register(register_page)
    )
    register_button.place(x=495, y=363)

    back_button = tkinter.Button(
        register_page, text="<", font=("Roboto", 17), 
        borderwidth=0, highlightthickness=0, width=2,
        bg="white", command=lambda: back(register_page)
    )
    back_button.place(x=50, y=178)

def register(panel):
    print("* Checking into the database")

    if register_usernameField.get() != empty and register_passwordField.get() != empty:
        print("* Fields are satisfied, checking user if exist...")

        try:
            connection = None
            connection = sqlite3.connect(database_path)
            
            cur = connection.cursor()
            cur.execute(f"SELECT * FROM Accounts WHERE Username='{register_usernameField.get()}';")
            results = cur.fetchone()

            if results != None:
                print("* User is already recorded, Please use the login...")
            else:
                print("* Registering user...")
                inserted_data = f"INSERT INTO Accounts(Username, Password)VALUES(?, ?);"

                cur.execute(inserted_data, (register_usernameField.get(), register_passwordField.get()))
                connection.commit()
                print("* Finished Registered user, Redirecting to Menu")

                menupage.show(panel, window, menu_image)

            connection.close()
            
        except sqlite3.Error as err:
            print(f"An error occured when 'Registering user', cause: {err}")
    else:
        print("* Please fill in the fields")

def back(panel):
    print("* Closing registration page")
    
    panel.destroy()
    login_page.pack()

# Login fields
login_image_path = "./img/login.png"
login_image = ImageTk.PhotoImage(Image.open(login_image_path))

# Frame
login_page = tkinter.Frame(window, width=800, height=620)
login_page.pack()

# Image Background
login_img_holder = tkinter.Label(login_page, image=login_image)
login_img_holder.pack()

# Elements
login_usernameField = tkinter.Entry(login_page, font=("Roboto", 16), borderwidth=0, highlightthickness=0, width=37)
login_usernameField.place(x=180, y=248)

login_passwordField = tkinter.Entry(login_page, font=("Roboto", 16), borderwidth=0, highlightthickness=0, width=37, show="•")
login_passwordField.place(x=180, y=308)

# Buttons
login_button = tkinter.Button(
    login_page, text="LOGIN", font=("Roboto", 16), 
    borderwidth=0, highlightthickness=0, width=11,
    bg="white", command=login
)
login_button.place(x=420, y=360)

register_button = tkinter.Button(
    login_page, text="REGISTER", font=("Roboto", 16), 
    borderwidth=0, highlightthickness=0, width=11,
    bg="white", command=show_register_page
)
register_button.place(x=580, y=359)

try:
    print('Running...')

    # Window properties
    window.geometry("800x620")
    window.config(background="white")
    window.title("Swab Taste!")
    window.mainloop()

except Exception as err:
    print(f'An error occured while running the program. {err}')
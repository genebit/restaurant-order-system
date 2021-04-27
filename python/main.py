import tkinter
from PIL import ImageTk, Image

import loginpage

try:
    print("Running...")
    window = tkinter.Tk()

    path = "./img/login.png"
    loginImage = ImageTk.PhotoImage(Image.open(path))
    
    loginpage.show(window, loginImage)

    window.geometry("800x620")
    window.config(background="white")
    window.title("Swab Taste!")
    window.mainloop()

except Exception as err:
    print(f"An error occured while running the application. {err}")
import tkinter
from PIL import ImageTk, Image

import loginpage
import registerpage

try:
    print("Running...")
    window = tkinter.Tk()

    loginPathImg = "./img/login.png"
    img = ImageTk.PhotoImage(Image.open(loginPathImg))
    
    loginpage.show(window, img)
    
    window.geometry("800x620")
    window.config(background="white")
    window.title("Swab Taste!")
    window.mainloop()

except Exception as err:
    print(f"An error occured while running the application. {err}")
import tkinter
from PIL import Image

def display(panel, window):
    panel.pack_forget()
    
    menu_page = tkinter.Frame(window, bg="white", width=813, height=581)
    menu_page.pack()

    img = tkinter.PhotoImage(file="./img/menu.png")

    canvas = tkinter.Canvas(menu_page, width=813, height=581)      
    canvas.create_image(400, 300, image=img)   
    canvas.pack()    

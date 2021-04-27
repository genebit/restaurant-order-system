import tkinter
from PIL import Image

root = tkinter.Tk()

root.config(background="black")

frame = tkinter.Frame(root, bg="white", width=813, height=581)
frame.pack()

img = tkinter.PhotoImage(file="./img/menu.png")      

canvas = tkinter.Canvas(frame, width=813, height=581)      
canvas.create_image(400, 300, image=img)   
canvas.pack()      


root.geometry("813x581")
root.mainloop()
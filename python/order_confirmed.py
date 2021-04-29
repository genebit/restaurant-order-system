import tkinter
from tkinter import messagebox

root = tkinter.Tk()

def onClick():
    
    if messagebox.showinfo(message="PAYMENT SUCCESSFULL!"):
        # Clicked 'OK' button it closes the whole program
        # Do something...
        root.destroy()

tkinter.Label(root, text="ORDER CONFIRM?").pack()
tkinter.Button(root, text="Yes", command=onClick).pack()

root.geometry("200x100")
root.mainloop()
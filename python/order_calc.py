import tkinter

root = tkinter.Tk()

counter = tkinter.IntVar()
PRICE = 200
total = tkinter.IntVar()

def onClick():
    counter.set(counter.get() + 1)
    
    for item in range(counter.get()):
        total.set("TOTAL: {}".format(counter.get() * PRICE))
    
tkinter.Label(root, textvariable=counter).pack()
tkinter.Button(root, text="Increase", command=onClick).pack()
tkinter.Label(root, textvariable=total).pack()

root.geometry("200x200")
root.mainloop()
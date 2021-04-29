import tkinter

root = tkinter.Tk()

counter = tkinter.IntVar()

# Can be ordered at top or at bottom, 
# when on bottom, use command=lambda: function()
# when on top, use command=function

def onClick():
    counter.set(counter.get() + 1)

tkinter.Label(root, textvariable=counter).pack()
tkinter.Button(root, text="Increase", command=onClick).pack()

root.geometry("200x200")
root.mainloop()
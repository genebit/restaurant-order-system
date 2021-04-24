import tkinter
import loginpage

try:
        print("Running...")
        window = tkinter.Tk()
        
        loginpage.display(window)

        #-------------WINDOWS PROPERTIES--------/
        window.title("Restaurant Login and Registration System")
        window.geometry("800x600+250+50")
        window.resizable(True, True)
        window.mainloop()
except Exception as error:
        print(f"An error occured when running the program. cause: {error}")
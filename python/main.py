import tkinter
import loginpage

try:
    print("Running...")
    window = tkinter.Tk()

    loginpage.display(window)

    # Window Properties
    window.title("Restaurant Management")
    window.geometry("800x600+250+50")
    window.resizable(False, False)
    window.mainloop()
except Exception as error:
    print(f"An error occured when running the program. cause: {error}")

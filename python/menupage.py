import tkinter

def show(panel, window, img):
    print("Menu Page loaded.")

    panel.pack_forget()

    # Frame
    menu_page = tkinter.Frame(window, width=800, height=620, bg="black")
    menu_page.pack()

    # Image Background
    m_img_holder = tkinter.Label(menu_page, image=img)
    m_img_holder.pack()

    # Buttons
    premium_set_order_button = tkinter.Button(
        menu_page, text="Premium Set", font=("Roboto", 15), 
        borderwidth=0, highlightthickness=0, width=10,
        bg="white"
    )
    premium_set_order_button.place(x=62, y=210)

    emperor_set_order_button = tkinter.Button(
        menu_page, text="Emperor Set", font=("Roboto", 15), 
        borderwidth=0, highlightthickness=0, width=10,
        bg="white"
    )
    emperor_set_order_button.place(x=220, y=210)

    delete_order_button = tkinter.Button(
        menu_page, text="DELETE", font=("Roboto", 14), 
        borderwidth=0, highlightthickness=0, width=5,
        bg="white"
    )
    delete_order_button.place(x=430, y=510)

    confirm_order_button = tkinter.Button(
        menu_page, text="CONFIRM \nORDER", font=("Roboto", 12), 
        borderwidth=0, highlightthickness=0, width=7, height=2,
        bg="white"
    )
    confirm_order_button.place(x=540, y=500)

    logout_button = tkinter.Button(
        menu_page, text="LOGOUT", font=("Roboto", 14), 
        borderwidth=0, highlightthickness=0, width=5,
        bg="white"
    )
    logout_button.place(x=660, y=510)
import tkinter

p_quantity = 0
e_quantity = 0
total_amount = 0

def show(panel, window, img):
    print("Menu Page loaded.")

    panel.pack_forget()

    # Frame
    menu_page = tkinter.Frame(window, width=800, height=620, bg="black")
    menu_page.pack()

    # Image Background
    m_img_holder = tkinter.Label(menu_page, image=img)
    m_img_holder.pack()
    
    # Discount text 
    discount_text = tkinter.Label(menu_page, text="NO DISCOUNT AVAILABLE", font=("Roboto", 15), bg="white")
    discount_text.place(x=440, y=210)

    # Order Table
    premium_set_order_text = tkinter.Label(
        menu_page, text=f"PREMIUM SET \tx{p_quantity}", font=("Roboto", 14),
        borderwidth=0, highlightthickness=0, width=20, bg="white"
    )
    premium_set_order_text.place(x=440, y=310)

    emperor_set_order_text = tkinter.Label(
        menu_page, text=f"EMPEROR SET \tx{e_quantity}", font=("Roboto", 14),
        borderwidth=0, highlightthickness=0, width=20, bg="white"
    )
    emperor_set_order_text.place(x=440, y=350)

    total = tkinter.Label(
        menu_page, text=f"TOTAL: \t\t{total_amount}", font=("Roboto", 15),
        borderwidth=0, highlightthickness=0, bg="white"
    )
    total.place(x=450, y=400)

    # Buttons
    premium_set_order_button = tkinter.Button(
        menu_page, text="Premium Set", font=("Roboto", 15), 
        borderwidth=0, highlightthickness=0, width=10,
        bg="white", command=lambda: premium_set
    )
    premium_set_order_button.place(x=62, y=210)

    emperor_set_order_button = tkinter.Button(
        menu_page, text="Emperor Set", font=("Roboto", 15), 
        borderwidth=0, highlightthickness=0, width=10,
        bg="white", command=lambda: emperor_set
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
        bg="white", command=lambda: return_home(menu_page)
    )
    logout_button.place(x=660, y=510)

def premium_set():
    print("Ordered premium set")
    p_quantity += 1

def emperor_set():
    print("Ordered emperor set")
    e_quantity += 1

def confirm_order():
    print("Confirmed order")
    # Popup a message that order successfull

def delete_set():
    print("Delete set")

def return_home(current_panel):
    print("Returned home.")

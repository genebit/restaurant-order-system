import tkinter

quantity = tkinter.IntVar()
PREMIUM_SET_PRICE = 600
EMPEROR_SET_PRICE = 800

total = tkinter.IntVar()

def premium_set_clicked():
    counter.set(counter.get() + 1)
    
    for item in range(counter.get()):
        total.set("TOTAL: {}".format(counter.get() * PRICE))

def show(panel, window, img):
    print("Menu Page loaded.")

    panel.pack_forget()

    # Frame
    menu_page = tkinter.Frame(window, width=800, height=620, bg="black")
    menu_page.pack()

    # Image Background
    m_img_holder = tkinter.Label(menu_page, image=img)
    m_img_holder.pack()
    
    # Static texts
    premium_text = tkinter.Label(menu_page, text="PREMIUM SET", font=("Roboto", 13), bg="white")
    emperor_text = tkinter.Label(menu_page, text="EMPEROR SET", font=("Roboto", 13), bg="white")
    total_text = tkinter.Label(menu_page, text="TOTAL:", font=("Roboto", 15), bg="white")
    
    premium_text.place(x=440, y=310)
    emperor_text.place(x=440, y=340)
    total_text.place(x=440, y=400)
    
    # p_quantity_text = tkinter.Label(menu_page, textvariable=quantity, font=("Roboto", 13))
    # p_quantity_text.place(x=500, y=300) 
                                            
    # tkinter.Button(root, text="Increase", command=onClick).pack()
    # tkinter.Label(root, textvariable=total).pack()
    
    # Buttons
    premium_set_order_button = tkinter.Button(
        menu_page, text="Premium Set", font=("Roboto", 15), 
        borderwidth=0, highlightthickness=0, width=10, height=1,
        bg="white", #command=premium_set_clicked
    )
    premium_set_order_button.place(x=70, y=210)

    emperor_set_order_button = tkinter.Button(
        menu_page, text="Emperor Set", font=("Roboto", 15), 
        borderwidth=0, highlightthickness=0, width=10,
        bg="white"
    )
    emperor_set_order_button.place(x=227, y=210)

    delete_order_button = tkinter.Button(
        menu_page, text="DELETE", font=("Roboto", 14), 
        borderwidth=0, highlightthickness=0, width=6,
        bg="white"
    )
    delete_order_button.place(x=438, y=515)

    confirm_order_button = tkinter.Button(
        menu_page, text="CONFIRM \nORDER", font=("Roboto", 13), 
        borderwidth=0, highlightthickness=0, width=9, height=2,
        bg="white"
    )
    confirm_order_button.place(x=540, y=500)

    logout_button = tkinter.Button(
        menu_page, text="LOGOUT", font=("Roboto", 14), 
        borderwidth=0, highlightthickness=0, width=6,
        bg="white"
    )
    logout_button.place(x=663, y=515)
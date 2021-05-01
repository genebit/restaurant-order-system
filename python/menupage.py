import tkinter
import time
from tkinter import messagebox
from datetime import datetime

p_quantity = tkinter.IntVar()
PREMIUM_SET_PRICE = 600

e_quantity = tkinter.IntVar()
EMPEROR_SET_PRICE = 800

p_total_amount = tkinter.IntVar()
e_total_amount = tkinter.IntVar()
total_amount = tkinter.IntVar()

current_date_and_month = f"{datetime.now().day}-{datetime.now().month}"

CHRISTMAS_SALE_DATE = ["26-12", "27-12", "28-12"]
DISCOUNTED_PERCENTAGE = 0.30

discount_status = tkinter.StringVar()
discounted = tkinter.BooleanVar()

def premium_set_clicked():
    p_quantity.set(p_quantity.get() + 1)
    
    for item in range(p_quantity.get()):
        p_total_amount.set(p_quantity.get() * PREMIUM_SET_PRICE)
        total_amount.set(p_total_amount.get() + e_total_amount.get())

    if p_quantity.get() >= 1:
        if current_date_and_month == CHRISTMAS_SALE_DATE[0] or current_date_and_month == CHRISTMAS_SALE_DATE[1] or current_date_and_month == CHRISTMAS_SALE_DATE[2]:
            discounted.set(True)
            discount_status.set("DISCOUNT APPLIED, SAVED {}% OFF!".format(DISCOUNTED_PERCENTAGE * 100))
        else:
            discounted.set(False)
            discount_status.set("NO DISCOUNT APPLIED")

def emperor_set_clicked():
    e_quantity.set(e_quantity.get() + 1)
    
    for item in range(e_quantity.get()):
        e_total_amount.set(e_quantity.get() * EMPEROR_SET_PRICE)
        total_amount.set(p_total_amount.get() + e_total_amount.get())

    if e_quantity.get() >= 1:
        if current_date_and_month == CHRISTMAS_SALE_DATE[0] or current_date_and_month == CHRISTMAS_SALE_DATE[1] or current_date_and_month == CHRISTMAS_SALE_DATE[2]:
            discount_status.set("DISCOUNT APPLIED, SAVED {}% OFF!".format(DISCOUNTED_PERCENTAGE * 100))
            discounted.set(True)
        else:
            discount_status.set("NO DISCOUNT APPLIED")
            discounted.set(False)

def delete_orders():
    p_quantity.set(p_quantity.get() * 0)
    e_quantity.set(e_quantity.get() * 0)
    total_amount.set(total_amount.get() * 0)

def confirmed_order(window):
    if discounted.get() == True:
        x = total_amount.get() * DISCOUNTED_PERCENTAGE
        total_amount.set(total_amount.get() - x)
        
        if messagebox.showinfo(title="Payment Info", message="PAYMENT SUCCESSFULL! SAVED {} PESOS OFF!".format(x)):
            print("Message box closed")
            window.destroy()
    else:
        if messagebox.showinfo(title="Payment Info", message="PAYMENT SUCCESSFULL!"):
            print("Message box closed")
            window.destroy()

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
    
    # Discount
    discount_text = tkinter.Label(menu_page, textvariable=discount_status, font=("Roboto", 12), bg="white")
    discount_text.place(x=435, y=210)

    # Variables
    p_quantity_text = tkinter.Label(menu_page, textvariable=p_quantity, font=("Roboto", 14), bg="white")
    p_quantity_text.place(x=650, y=310) 
    
    e_quantity_text = tkinter.Label(menu_page, textvariable=e_quantity, font=("Roboto", 14), bg="white")
    e_quantity_text.place(x=650, y=340) 

    total_amount_text = tkinter.Label(menu_page, textvariable=total_amount, font=("Roboto", 14), bg="white")
    total_amount_text.place(x=650, y=400) 

    # Buttons
    premium_set_order_button = tkinter.Button(
        menu_page, text="Premium Set", font=("Roboto", 15), 
        borderwidth=0, highlightthickness=0, width=10, height=1,
        bg="white", command=premium_set_clicked
    )
    premium_set_order_button.place(x=70, y=210)

    emperor_set_order_button = tkinter.Button(
        menu_page, text="Emperor Set", font=("Roboto", 15), 
        borderwidth=0, highlightthickness=0, width=10,
        bg="white", command=emperor_set_clicked
    )
    emperor_set_order_button.place(x=227, y=210)

    delete_order_button = tkinter.Button(
        menu_page, text="DELETE", font=("Roboto", 14), 
        borderwidth=0, highlightthickness=0, width=6,
        bg="white", command=delete_orders
    )
    delete_order_button.place(x=438, y=515)

    confirm_order_button = tkinter.Button(
        menu_page, text="CONFIRM \nORDER", font=("Roboto", 13), 
        borderwidth=0, highlightthickness=0, width=9, height=2,
        bg="white", command=lambda : confirmed_order(window)
    )
    confirm_order_button.place(x=540, y=500)

    logout_button = tkinter.Button(
        menu_page, text="LOGOUT", font=("Roboto", 14), 
        borderwidth=0, highlightthickness=0, width=6,
        bg="white", command=lambda : window.destroy()
    )
    logout_button.place(x=663, y=515)
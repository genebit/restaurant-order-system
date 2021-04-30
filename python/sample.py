from datetime import datetime

# Get the current date
# Compare the current date to the sale's date

currentDay = datetime.now().day
currentMonth = datetime.now().month

# current_date_and_month = f"{currentDay}-{currentMonth}"
current_date_and_month = f"{currentDay}-{currentMonth}"

CHRISTMAS_SALE = ["26-12", "27-12", "28-12"]

def apply_discount(price, percentage):
    f = price * percentage
    result = price-f
    return result

if current_date_and_month == CHRISTMAS_SALE[0] or current_date_and_month == CHRISTMAS_SALE[1] or current_date_and_month == CHRISTMAS_SALE[2]:
    print("Discount Applied")
    apply_discount(500, 0.30)
else:
    print("It is not Christmas yet")

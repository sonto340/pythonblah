price = 1000000
good_credit = False

if good_credit:
    down_payment = (price * .1)
else:
    down_payment = (price * .2)

print(f"Your down payment is ${down_payment}")
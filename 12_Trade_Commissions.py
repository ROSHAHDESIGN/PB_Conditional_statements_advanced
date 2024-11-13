city = input()
sales_quantity = float(input())
commission = 0
error = False


if 0 <= sales_quantity <= 500:
    if city == "Sofia":
        commission = 0.05
    elif city == "Varna":
        commission = 0.045
    elif city == "Plovdiv":
        commission = 0.055
    else:
        error = True
elif 500 < sales_quantity <= 1000:
    if city == "Sofia":
        commission = 0.07
    elif city == "Varna":
        commission = 0.075
    elif city == "Plovdiv":
        commission = 0.08
    else:
        error = True
elif 1000 < sales_quantity <= 10_000:
    if city == "Sofia":
        commission = 0.08
    elif city == "Varna":
        commission = 0.10
    elif city == "Plovdiv":
        commission = 0.12
    else:
        error = True
elif sales_quantity > 10_000:
    if city == "Sofia":
        commission = 0.12
    elif city == "Varna":
        commission = 0.13
    elif city == "Plovdiv":
        commission = 0.145
    else:
        error = True
else:
    error = True

sales_commission = sales_quantity * commission
if error:
    print("error")
else:
    print(f"{sales_commission:.2f}")

fruit = input()
day_of_week = input()
quantity = float(input())

price = 0.0
is_error = False # vyvejdam Flag koyto e False

if (day_of_week == "Monday" or
    day_of_week == "Tuesday" or
    day_of_week =="Wednesday" or
    day_of_week == "Thursday" or
    day_of_week == "Friday"):
    if fruit == "banana":
       price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    else:
        is_error = True # is_error logicheski promenya izhoda
elif (day_of_week == "Saturday" or
    day_of_week == "Sunday" ):
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        is_error = True

else:
    is_error = True

final_price = quantity * price

if is_error: #ako e raven na True obratnata stoinost
    print("error")
else: #ako e ostanal na stoinostta koyato set-nah
    print(f"{final_price:.2f}")




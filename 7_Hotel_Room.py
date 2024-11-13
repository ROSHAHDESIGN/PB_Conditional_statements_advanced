month = input()
nights_number = float(input())

type_room = " "
cost_st = 0.0
cost_app = 0.0
discount = 0.0

if month == "May" or month == "October":
    type_room = "Studio"
    cost_st = 50
    if nights_number > 7:
        discount = 0.05
    elif nights_number > 14:
        discount = 0.30
    type_room = "Apartment"
    cost_app = 65
    if nights_number > 14:
        discount = 0.10
if month == "June" or month == "September":
    type_room = "Studio"
    cost_st = 75.20
    if nights_number > 14:
        discount = 0.20
    type_room = "Apartment"
    cost_app = 68.70
    if nights_number > 14:
        discount = 0.10
if month == "July" or month == "August":
    type_room = "Studio"
    cost_st = 76
    type_room = "Apartment"
    cost_app = 77
    if nights_number > 14:
        discount = 0.10

final_cost_st = (cost_st * discount)* nights_number
final_cost_app = (cost_app * discount)* nights_number

print(f"Apartment: {final_cost_app} lv.")
print(f"Studio: {final_cost_st} lv.")

month = input()
nights_quantity = int(input())

night_in_studio= 0
night_in_app = 0
# discount = 1


if month == "May" or month == "October":
    night_in_studio = 50
    night_in_app = 65
    if nights_quantity > 7 and nights_quantity < 14 :
        night_in_studio *= 0.95
    if nights_quantity > 14:
        night_in_studio *= 0.70

elif month == "June" or month == "September":
    night_in_studio = 75.20
    night_in_app = 68.70
    if nights_quantity > 14:
        night_in_studio *= 0.80

elif month == "July" or month == "August":
    night_in_studio = 76
    night_in_app = 77

if nights_quantity > 14:
    night_in_app *= 0.90

#ОТСТЪПКИ към вече избраната цена за нощувка
# (когато броят на нощувките надвишава определеното условие),

# if (month == "May" or month == "October"):
#     if nights_quantity > 7:
#         night_in_studio *= 0.95
#     elif nights_quantity > 14:
#         night_in_studio *= 0.70
#
# elif (month == "June" or month == "September"):
#     if nights_quantity > 14:
#         night_in_studio *= 0.80
# if nights_quantity > 14:
#     night_in_app *= 0.90


price_total_stay_app = nights_quantity * night_in_app
price_total_stay_studio = night_in_studio * nights_quantity

print(f"Apartment: {price_total_stay_app:.2f} lv.")
print(f"Studio: {price_total_stay_studio:.2f} lv.")

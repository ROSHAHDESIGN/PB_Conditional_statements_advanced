budget = float(input())
season = input()

booking_place = " "
type_accommodation = " "
money_spend = 0.0


if budget <= 100:
    if season == "summer":
        money_spend = 0.30
        type_accommodation = "Camp"
        booking_place = "Bulgaria"
    elif season == "winter":
        money_spend = 0.70
        type_accommodation = "Hotel"
        booking_place = "Bulgaria"
elif 100 < budget <= 1000:
    if season == "summer":
        money_spend = 0.40
        type_accommodation = "Camp"
        booking_place = "Balkans"
    elif season == "winter":
        money_spend = 0.80
        type_accommodation = "Hotel"
        booking_place = "Balkans"
elif budget > 1000:
    money_spend = 0.90
    type_accommodation = "Hotel"
    booking_place = "Europe"

final_cost = money_spend * budget

print(f"Somewhere in {booking_place}")
print(f"{type_accommodation} - {final_cost:.2f}")

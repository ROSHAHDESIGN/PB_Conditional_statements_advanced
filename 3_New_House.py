flowers_type = input()
flowers_count = int(input())
budget = float(input())

discount = 0.0
flowers_cost = 0.0


if flowers_type == "Roses":
    flowers_cost = flowers_count * 5
    if flowers_count > 80 :
        flowers_cost *= 0.10

elif flowers_type == "Dahlias":
    flowers_cost = flowers_count * 3.8
    if flowers_count > 90 :
        flowers_cost *= 0.15

elif flowers_type == "Tulips":
    flowers_cost = flowers_count * 2.8
    if flowers_count > 80 :
        flowers_cost *= 0.15

elif flowers_type == "Narcissus":
    flowers_cost = flowers_count * 3
    if flowers_count < 120:
        flowers_cost = flowers_cost + (flowers_cost * 0.15)
elif flowers_type == "Gladiolus":
    flowers_cost = flowers_count * 2.5
    if flowers_count < 80:
        flowers_cost = flowers_cost + (flowers_cost * 0.20)

if budget >= flowers_cost :
    money_left = budget - flowers_cost
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {money_left:.2f} leva left.")
else:
    money_needed = budget - flowers_cost
    print(f"Not enough money, you need {abs(money_needed):.2f} leva more.")




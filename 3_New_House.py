flower_type = input()
flower_num = int(input())
budget = int(input())

price_for_one = 0.0
price_change = 0.0

if flower_type == "Roses":
    price_for_one = 5.00
    if flower_num > 80:
        price_change = -10
elif flower_type == "Dahlias":
    price_for_one = 3.80
    if flower_num > 90:
        price_change = -15
elif flower_type == "Tulips":
    price_for_one = 2.80
    if flower_num > 80:
        price_change = -15
elif flower_type == "Narcissus":
    price_for_one = 3.00
    if flower_num < 120:
        price_change = 15
elif flower_type == "Gladiolus":
    price_for_one = 2.50
    if flower_num < 80:
        price_change = 20

end_total = (price_for_one * flower_num) + (price_for_one * flower_num * price_change / 100)
money_diff = abs(budget - end_total)

if budget >= end_total:
    print(f"Hey, you have a great garden with {flower_num} {flower_type} and {money_diff:.2f} leva left.")

elif budget < end_total:
    print(f"Not enough money, you need {money_diff:.2f} leva more.")
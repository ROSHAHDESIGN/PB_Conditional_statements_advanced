# Цената за наем на кораба през пролетта е  3000 лв.;
# Цената за наем на кораба през лятото и есента е  4200 лв.;
# Цената за наем на кораба през зимата е  2600 лв.

#INPUT
budget = int(input())#cyalo chislo
season = input()
fisher_mans = int(input())#cyalo chislo
rent = 0

if season == "Spring":
    rent = 3000

elif season == "Summer" or season == "Autumn":
    rent = 4200

elif season == "Winter":
    rent = 2600

# •	Ако групата е до 6 човека включително  -  отстъпка от 10%;
# •	Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# •	Ако групата е от 12 нагоре  -  отстъпка от 25%.

discount = 0.0
if fisher_mans <= 6: #(-inf, 6]
    discount = 0.10
elif fisher_mans <= 11: #(6, 11]
    discount = 0.15
else: #[12, inf)
    discount = 0.25

extra_discount = 0.0

if fisher_mans % 2 == 0 and season != "Autumn":
   extra_discount = 0.05

cost = rent * (1 -discount)* (1 -extra_discount)

if budget >= cost:
    left_money = budget - cost
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    money_needed = cost - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")


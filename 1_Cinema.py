movie_type = input()
rows_number = int(input())
columns_number = int(input())

# •	Premiere - премиерна прожекция, на цена 12.00 лева;
# •	Normal - стандартна прожекция, на цена 7.50 лева;
# •	Discount - прожекция за деца,от 5.00 лева.
profit = 0

cinema_capacity = rows_number * columns_number

if movie_type == "Premiere":
    profit = cinema_capacity * 12.0
elif movie_type == "Normal":
    profit = cinema_capacity * 7.5
elif movie_type == "Discount":
    profit = cinema_capacity * 5.0

print(f"{profit:.2f} leva")

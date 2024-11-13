hour = int(input())
day_of_week = input()
result = ""

if 10 <= hour <= 18 :
    if (day_of_week == "Monday" or
        day_of_week == "Tuesday" or
        day_of_week == "Wednesday" or
        day_of_week == "Thursday" or
        day_of_week == "Friday" or
        day_of_week == "Saturday"):
        result = "open"
    else:
        result = "closed"
else:
    result = "closed"
print(result)

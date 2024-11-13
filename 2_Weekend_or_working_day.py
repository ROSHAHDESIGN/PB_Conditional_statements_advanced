number = input()
result = ""
if number == "Monday":  # we can use operator OR for all days
    result = "Working day"
elif number == "Tuesday":
    result = "Working day"
elif number == "Wednesday":
    result = "Working day"
elif number == "Thursday":
    result = "Working day"
elif number == "Friday":
    result = "Working day"
elif number == "Saturday":
    result = "Weekend"
elif number == "Sunday":
    result = "Weekend"
else:
    result = "Error"
print(result)
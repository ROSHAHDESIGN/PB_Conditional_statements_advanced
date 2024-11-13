product = input()
kind = " "

if (product == "banana" or
    product == "apple" or
    product == "kiwi" or
    product == "cherry" or
    product == "lemon" or
    product == "grapes"):
    kind = "fruit"
elif (product == "tomato" or
    product == "cucumber" or
    product == "pepper" or
    product == "carrot"):
    kind = "vegetable"
else:
    kind = "unknown"

print(kind)

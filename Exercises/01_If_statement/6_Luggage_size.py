weight = int(input("weight(kg): "))
length = int(input("length(cm): "))
width = int(input("width(cm): "))
height = int(input("height(cm): "))

if weight <= 8:
    if length <= 55 and width <= 40 and height <= 23:
        print("luggage is allowed")
    else:
        print("dimensions exceed the limit")
else:
    print("weight exceeds the limit")
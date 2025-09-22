age = int(input("Age: "))
weight = int(input("Weight (kg): "))

if age <= 7:
    if weight <= 25:
        print("Take 1/2 pill")
    else:
        print("Take 1/2 - 1 pill")
elif age <= 12:
    if weight <= 40:
        print("Take 1/2 - 1 pill")
    else:
        print("Take 1 - 2 pills")
else:
    if age >12 and weight > 40:
        print("Take 1-2 pills")
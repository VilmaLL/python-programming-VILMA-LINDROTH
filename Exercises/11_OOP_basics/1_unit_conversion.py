
class Conversion:
    def __init__(self, value):
        self.value = value

    def inch_to_cm(self):
        length_in_cm = self.value * 2.54
        return length_in_cm

    def foot_to_cm(self):
        length_in_cm = self.value * 30.48
        return length_in_cm

    def pound_to_kg(self):
        weight_in_kg = self.value * 0.45359237
        return weight_in_kg

    def __repr__(self):
        return f"Conversion(value={self.value})"
    
while True:
    try:
        value_choice = input("What conversion do you wish to do? \n1: inch to cm \n2: foot to cm\n3: pound to kg\n")
        if value_choice not in ("1", "2", "3"):
            raise ValueError("You have to choose one of the three given options (1, 2, 3)")
        break
    except ValueError as err:
        print(err)

while True:
    try:
        value = float(input("Enter amount to convert: "))
        if value <= 0:
            raise ValueError("The number you wish to convert must be a positiv number")
        break
    except ValueError as err:
        print(err)

conv = Conversion(value)

if value_choice == "1":
    print(f"{value} inch = {conv.inch_to_cm()} cm")
elif value_choice == "2":
    print(f"{value} foot = {conv.foot_to_cm()} cm")
elif value_choice == "3":
    print(f"{value} pound = {conv.pound_to_kg()} kg")



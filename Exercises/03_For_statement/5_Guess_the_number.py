import random
Number = random.randint(1000, 9999)

for i in range(1000, 10000, 1):
    if i == Number:
        print(f"The final guess is {i}")
        print(f"The computer number is {Number}")
FoodItems = ["vegetarisk lasagne", "spaghetti", "fisk", "grönsakssoppa", "pannkakor"]
Weekdays = ["Mån", "Tis", "Ons", "Tor", "Fre"]

print("Food Menu")
      
for i in range(len(FoodItems)):
    print(f"{Weekdays[i]} : {FoodItems[i]}")
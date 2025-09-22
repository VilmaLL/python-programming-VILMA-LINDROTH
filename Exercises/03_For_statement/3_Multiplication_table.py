Product = 1
Product2 = 1

for i in range(0, 11, 1):
    print(6 * i, end=" ")

table = int(input("\nEnter the multiplication table you want: "))
start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))

for j in range(start, end, 1):
    print(table * j, end=" ")

print()


for n in range(0, 11, 1):
    for m in range(0, 11, 1):
        print(m*n, end="\t")
    print()
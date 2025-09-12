import math

sum = 1
n = 1

while (n < 100):
    sum += (1/(2**n))
    n +=1
    print(sum, end=" ")


sum2 = 1
m = 1
while (m < 200):
    sum2 += (((-1)**m)/(2*m +1))
    m +=1
    print(sum2, end=" ")

print(math.pi/4)

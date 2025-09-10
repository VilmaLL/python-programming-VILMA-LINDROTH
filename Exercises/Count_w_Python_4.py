import math
A = (4,4)
B = (0,1)

k = (B[1] - A[1]) / (B[0] - A[0])

m = B[1] - k*B[0]
print("k = ", k)
print("m = ", m)
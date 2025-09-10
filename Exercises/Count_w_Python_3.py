import math

TP = 2
FP = 2
FN = 11
TN = 985

Accuracy = (TP + TN) / (TP + TN + FP + FN)
print ("Accuracy: ", ((round(Accuracy, 3)) * 100), "%")
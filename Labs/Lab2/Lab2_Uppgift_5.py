import random
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

# definiera lista och importera datapoints från fil till lista
datapoints = []
pathData = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Labs\datapoints.txt"
with open(pathData, "r") as file:
    for line in file:
        DataParts = line.strip().split(",")
        if len(DataParts) == 3:
            WidthData = float(DataParts[0])
            HeightData = float(DataParts[1])
            Label = int(DataParts[2])
            datapoints.append((WidthData, HeightData, Label))


# Nearest neighbor funktion

def EuclideanDistance (p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)

def NearestNeighbor(TestData, ReferenceData, k=10):
    TrueLabelForTest = []
    PredictedLabelForTest = []

    for test in TestData:
        distances = []
        TestPoint = (test[0], test[1])
        TestLabel = test[2]
        TrueLabelForTest.append(TestLabel)

        for data in ReferenceData:
            DataPoint = (data[0], data[1])
            label = data[2]
            distance = EuclideanDistance(TestPoint, DataPoint)
            distances.append((distance, label))

        distances.sort(key = lambda x: x[0])

        k_neighbors = distances[:k]

        k_labels = [label for _, label in k_neighbors]

        most_common = Counter(k_labels).most_common(1) 

        predicted_label = most_common[0][0]

        PredictedLabelForTest.append(predicted_label)
        
    return TrueLabelForTest, PredictedLabelForTest


# Accuracy beräkningar
AccuracyList = []
for simulations in range(10):

    # separera datan i filen till två listor ref/test

    Datapoints_c0 = [d for d in datapoints if d[2] == 0]
    Datapoints_c1 = [d for d in datapoints if d[2] == 1]

    random.shuffle(Datapoints_c0) 
    random.shuffle(Datapoints_c1)

    ReferenceData = Datapoints_c0[:50] + Datapoints_c1[:50]
    TestData = Datapoints_c0[50:] + Datapoints_c1[50:]

    random.shuffle(TestData)

    # kalla på funktionen
    TrueLabelForTest, PredictedLabelForTest = NearestNeighbor(TestData, ReferenceData, k = 10)

    TruePrediction = 0
    FalsePrediction = 0

    for i in range (len(TrueLabelForTest)):
        if TrueLabelForTest[i] == PredictedLabelForTest[i]:
            TruePrediction += 1
        else:
            FalsePrediction += 1

    Accuracy = (TruePrediction)/(TruePrediction + FalsePrediction)
    AccuracyList.append(Accuracy)

print(f"Accuracy of predictions: {AccuracyList}")

AccuracySum = 0
for i in AccuracyList:
    AccuracySum += i

AccuracyAverage = AccuracySum/ len(AccuracyList)
print(f"{AccuracyAverage:.3f}")

# plotta accuracy
x = list(range(10))
y = AccuracyList

plt.figure(figsize = (10, 6))
plt.plot(x, y)
plt.axhline(y = AccuracyAverage, color = "red", label = f"Average Accuracy: {AccuracyAverage:.3f}")
plt.title("Accuracy of Nearest Neighbor prediction")
plt.xlabel("Simulation nr")
plt.ylabel("Accuracy")
plt.xlim(0, 9)
plt.ylim(0.85 , 1.0)
plt.grid(True)
plt.legend()
plt.show()

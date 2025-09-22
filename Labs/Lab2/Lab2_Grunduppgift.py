import matplotlib.pyplot as plt
import numpy as np

# Definiera lista och importera datapoints från fil
datapoints = []
pathData = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Labs\datapoints.txt"
pathTestData = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Labs\testpoints.txt"
with open(pathData, "r") as file:
    for line in file:
        DataParts = line.strip().split(",")
        if len(DataParts) == 3:
            WidthData = float(DataParts[0])
            HeightData = float(DataParts[1])
            Label = int(DataParts[2])
            datapoints.append((WidthData, HeightData, Label))

# separera datapunkter för pichu (0) och pikachu (1)
WidthsPichu = []
HeightsPichu = []
WidthsPikachu = []
HeightsPikachu = []

for width, height, label in datapoints:
    if label == 0:
        WidthsPichu.append(width)
        HeightsPichu.append(height)
    elif label == 1:
        WidthsPikachu.append(width)
        HeightsPikachu.append(height)


# definiera lista och läs in testpunkter från fil
testpoints = []
with open(pathTestData, "r") as file:
    for line in file:
        TestParts = line.strip().split(",")
        if len(TestParts) == 2:
            WidthTest = float(TestParts[0])
            HeightTest = float(TestParts[1])
            testpoints.append((WidthTest, HeightTest))

# Nearest Neighbor Funktion

def EuclideanDistance (p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)


def NearestNeighbor(testpoint, datapoints):
    MinDistance = float("inf")
    PredictedLabel = None

    for data in datapoints:
        DataPoint = (data[0], data[1])
        label = data[2]
        distance = EuclideanDistance(testpoint, DataPoint)
        if distance < MinDistance:
            MinDistance = distance
            PredictedLabel = label

    return PredictedLabel


# klassificera testpunkterna som Pichu eller Pikachu
ClassifiedTestpoints = []
for testpoint in testpoints:
    PredictedLabel = NearestNeighbor(testpoint, datapoints)
    ClassifiedTestpoints.append((testpoint[0], testpoint[1], PredictedLabel))


# plotta datapunkterna med olika färger för pichu och pikachu
plt.figure(figsize=(10, 6))
plt.scatter(WidthsPichu, HeightsPichu, color = "yellow", label = "Pichu")
plt.scatter(WidthsPikachu, HeightsPikachu, color = "orange", label = "Pikachu")

LabelDuplet = set()

for x, y, label in ClassifiedTestpoints:
    color = "green" if label == 0 else "red"
    LabelText = "Classified as Pichu" if label == 0 else "Classified as Pikachu"
    
    if LabelText not in LabelDuplet: # Källhantering: hantering av dubblering av labels förklarat med annat exempel av chatGPT 
        plt.scatter(x, y, color = color, label = LabelText)
        LabelDuplet.add(LabelText)
    else:
        plt.scatter(x, y, color = color)


plt.title('Pichu or Pikachu')
plt.xlabel('Width')
plt.ylabel('Height')
plt.xlim(15, 30)
plt.ylim(25, 45)
plt.grid(True)
plt.legend()
plt.show()

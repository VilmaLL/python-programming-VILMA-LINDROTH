import matplotlib.pyplot as plt
import numpy as np

# Läs in filen unlabelled_data.csv

path = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Labs\Lab3\unlabelled_data.csv"

with open(path, "r") as file:
    Data = []
    for line in file:
        DataParts = line.strip().split(",")
        if len(DataParts) == 2:
            X = float(DataParts[0])
            Y = float(DataParts[1])
            Data.append((X, Y))

# Dra en linje som separerar punkterna, y = kx + m
x_line = np.linspace(-5, 5)
k = -5/3
m = 0.25        
y_line = k*x_line + m

# func, vilken sida om linjen ligger punkten. for y = kx + m, if y_punkt > y punkt label = 1

def LabelledData(Data):

    Labelled_Data = []

    for X, Y in Data:
        y_at_X = k*X + m
        if Y <= y_at_X:
            Label = 0
        else:
            Label = 1
        Labelled_Data.append((X, Y, Label))
    return Labelled_Data

Labelled_Data = LabelledData(Data)

# skapa fil labelled_data.csv med kolumner x, y, label 0 eller 1

Path2 = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Labs\Lab3\labelled_data.csv"

with open(Path2, "w") as File:
    File.write("X, Y, Label \n")
    for data in Labelled_Data:
        File.write(f"{data}\n")

# skapa graf med punkterna, deras labels, och skiljelinjen
X_Bellow_Line = []
Y_Bellow_Line = []
X_Above_Line = []
Y_Above_Line = []

for X, Y, Label in Labelled_Data:
    if Label == 0:
        X_Bellow_Line.append(X)
        Y_Bellow_Line.append(Y)
    elif Label == 1:
        X_Above_Line.append(X)
        Y_Above_Line.append(Y)


plt.figure(figsize=(10, 6))
plt.scatter(X_Bellow_Line, Y_Bellow_Line, color = "blue", label = "Point bellow line")
plt.scatter(X_Above_Line, Y_Above_Line, color = "green", label = "Point above line")
plt.plot(x_line, y_line)
plt.grid()
plt.legend()
plt.show()
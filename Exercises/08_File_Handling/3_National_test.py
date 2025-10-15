# läs in filen
# etrahera rad för rad
# lägg in i en lista
import re
import matplotlib.pyplot as plt

ListOfGrades2A = []
ListOfGrades2C = []

path = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Exercises\08_File_Handling\NPvt19Ma2A.txt"
with open (path, "r") as f_read:
    for line in f_read:
        grade, percent = line.strip().split()
        percent = float(percent.strip("%"))
        ListOfGrades2A.append((grade, percent))


path = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Exercises\08_File_Handling\NPvt19Ma2C.txt"
with open (path, "r") as f_read:
    for line in f_read:
        grade, percent = line.strip().split()
        percent = float(percent.strip("%"))
        ListOfGrades2C.append((grade, percent))

grades2A = [grade for grade, percent in ListOfGrades2A]
percent2A = [percent for grade, percent in ListOfGrades2A]
grades2C = [grade for grade, percent in ListOfGrades2C]
percent2C = [percent for grade, percent in ListOfGrades2C]

fig, axs = plt.subplots(1, 2, figsize = (10, 5))

axs[0].pie(percent2A, labels = grades2A, autopct= "%1.1f%%")
axs[0].set_title("Grades in Ma2a")

axs[1].pie(percent2C, labels = grades2C, autopct= "%1.1f%%")
axs[1].set_title("Grades in Ma2C")

plt.tight_layout()
plt.show()

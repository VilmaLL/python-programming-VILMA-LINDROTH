
path = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Exercises\08_File_Handling\test_result.txt"
path2 = r"C:\Users\vilma\python-programming-VILMA-LINDROTH\Exercises\08_File_Handling\test_result_cleaned.txt"

# read file and print content
with open(path, "r") as File_read:
    text = File_read.read()
print(repr(text))

#Clean and sort
with open(path, "r") as File_read, open (path2, "w") as File_write:
    
    Names = [line.strip() for line in File_read if line.strip()]

    NamesSorted = sorted(Names)

    File_write.write("\n".join(NamesSorted))
    File_write.write("\n")


with open(path2, "r") as f_read, open (path2, "a") as f_append:
    Names = [name.strip() for name in f_read if name.strip()]
    Score = [int(name.split()[-1]) for name in Names]

    GradeF = []
    GradeE = []
    GradeD = []
    GradeC = []
    GradeB = []
    GradeA = []

    for name, score in zip(Names, Score):
        if score < 20:
            GradeF.append(name)
        elif score < 30:
            GradeE.append(name)
        elif score < 40:
            GradeD.append(name)
        elif score < 50:
            GradeC.append(name)
        elif score < 60:
            GradeB.append(name)
        else:
            GradeA.append(name)
        

    f_append.write("\nSorted results:\n")
    f_append.write("Grade: F\n")
    f_append.write("\n".join(GradeF) + "\n")
    f_append.write("Grade: E\n")
    f_append.write("\n".join(GradeE) + "\n")
    f_append.write("Grade: D\n")
    f_append.write("\n".join(GradeD) + "\n")
    f_append.write("Grade: C\n")
    f_append.write("\n".join(GradeC) + "\n")
    f_append.write("Grade: B\n")
    f_append.write("\n".join(GradeB) + "\n")
    f_append.write("Grade: A\n")
    f_append.write("\n".join(GradeA) + "\n")


    





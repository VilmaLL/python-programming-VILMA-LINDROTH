Angle1 = int(input("Enter 1st Angles: "))
Angle2 = int(input("Enter 2nd Angle: "))
Angle3 = int(input("Enter 3rd Angle: "))

if Angle1 + Angle2 + Angle3 == 180:
    if Angle1 == 90 or Angle2 == 90 or Angle3 == 90:
        print("The triangle has a right angle")
    else:
        print("The triangle does not have a right angle")
else:
    print("The angles do not form a triangle")  
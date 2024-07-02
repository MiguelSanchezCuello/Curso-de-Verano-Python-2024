# This weight converter program will receive a number and will ask what if it is in pounds or kg then it will
# convert it to the other unit
# The excercise was extracted from https://www.youtube.com/watch?v=kqtD5dpn9C8&t=1287s

weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit.upper() == "K":
    converted = weight / 0.45
    print(f"You are {converted} pounds")
else:
    print("Invalid input")

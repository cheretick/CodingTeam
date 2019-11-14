a, b, c = eval(input("Enter three side lengths: "))

def isGreater(side1, side2, side3):
    if side1 > side2 and side1 > side3:
        return True
    else:
        return False

if isGreater(a, b, c) and a ** 2 == b ** 2 + c ** 2:
    print("This is a triangle!")

elif isGreater(b, c, a) and b ** 2 == c ** 2 + a ** 2:
    print("This is a triangle!")

elif isGreater(c, b, a) and c ** 2 == b ** 2 + a ** 2:
    print("This is a triangle!")

else:
    print("This is NOT a triangle!")



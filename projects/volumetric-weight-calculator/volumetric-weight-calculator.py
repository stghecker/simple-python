width = 0.0
height = 0.0
length = 0.0
whl = 0.0
grams = 0.0
while True:
    while True:
        width = input("Width...:").replace(",", ".")
        try:
            width = float(width)
            break
        except ValueError:
            print("Please input a valid number.")
    while True:
        height = input("Height...:").replace(",", ".")
        try:
            height = float(height)
            break
        except ValueError:
            print("Please input a valid number.")
    while True:
        length = input("Length...:").replace(",", ".")
        try:
            length = float(length)
            break
        except ValueError:
            print("Please input a valid number.")
    while True:
        grams = input("Grams...:").replace(",", ".")
        try:
            grams = float(grams)
            break
        except ValueError:
            print("Please input a valid number.")

    


    whl = (width * height * length) / 5


    if whl >= grams:
        print(f"Your product is {whl:.2f} grams (Volumetric).")
        print(f"({width} * {height} * {length}) / 5")
    elif grams >= whl:
        print(f"Your product is {grams:.2f} grams (Actual).\n")   

#STGHECKER#

width = 0.0
height = 0.0
length = 0.0
whl = 0.0
grams = 0.0

width = float(input("Width...:").replace(",", "."))
height = float(input("Height...:").replace(",", "."))
length = float(input("Length...:").replace(",", "."))
grams = float(input("Grams...:").replace(",", "."))

whl = (width * height * length) / 5


if whl >= grams:
    print(f"Your product is {whl:.2f} grams (Volumetric).")
else:
    print(f"Your product is {grams:.2f} grams (Actual).")

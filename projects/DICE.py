import random

print("====")
print("DICE")
print("====")

vwrong = 1  

while vwrong != 0:
    sides = input("How many sides has the dice? ")
    try:
        sides = int(sides)
        vwrong = 0
    except ValueError:
        print("Please input a number.")
        vwrong = 1 

def fresult(sides):
    roll = random.randint(1, sides)
    print("-- RANDOM ROLL:", roll, "--")

fresult(sides)

#STGHECKER#

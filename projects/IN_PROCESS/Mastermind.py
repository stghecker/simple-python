import random #imports libraries needed

print("Mastermind")


secret = [random.randint(1, 9) for _ in range(3)] #gets 3 random numbers for user to guess

print("Guess 3 numbers between 1 and 9")

while True:
    guess = [int(input("Number 1: ")), int(input("Number 2: ")), int(input("Number 3: "))] #gets users guesses as 3 different imputs
    
    score = sum(1 for num in guess if num in secret) #calculates users score
    
    print(f"Score: {score}")
    
    if score == 3:
        print("You won!")
        break
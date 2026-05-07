from random import sample
score = 0
print("Mastermind")
num1, num2, num3 = sample(range(1, 10), 3)

guess1 = int(input("Guess the 1st number:"))
guess2 = int(input("Guess the 2nd number:"))
guess3 = int(input("Guess the 3rd number:"))
if guess1 == num1:
    score += 1
if guess1 == num2:
    score += 1
if guess1 == num3:
    score += 1
if guess2 == num1:
    score += 1
if guess2 == num2:
    score += 1
if guess2 == num3:
    score += 1
if guess3 == num1:
    score += 1
if guess3 == num2:
    score += 1
if guess3 == num3:
    score += 1
print(score)

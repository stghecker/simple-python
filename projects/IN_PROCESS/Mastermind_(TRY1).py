import random
score = 0
print("Mastermind")
num1 = 1
num2 = 1
num3 = 1
while True:
    if num1 == num2 or num3:
        num1 = random.randint(1,9)
    if num2 == num1 or num3:
        num2 = random.randint(1,9)
    if num1 or num2 or num3 is not num1 or num2 or num3:
        break
    else:
        continue

while True:
    guessnum1 = input("Guess the 1st number:")
    guessnum2 = input("Guess the 2nd number:")
    guessnum3 = input("Guess the 3rd number:")

    if guessnum1 or guessnum2 or guessnum3 == num1 or num2 or num3:
        if guessnum1 == num1:
            score += 1
        if guessnum1 == num2:
            score += 1
        if guessnum1 == num3:
            score += 1
        if guessnum2 == num1:
            score += 1
        if guessnum2 == num2:
            score += 1
        if guessnum2 == num3:
            score += 1
        if guessnum3 == num1:
            score += 1
        if guessnum3 == num2:
            score += 1
        if guessnum3 == num3:
            score += 1
        if score == "3":
            print("You won!")
            break
        else:
            print("You guessed" , score , "numbers, try again")
    else:
        print("Try again!")

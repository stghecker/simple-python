import time
check = 0
seconds = input("Give seconds: ")

while check == 0:
    try:
        seconds = int(seconds)
        check = 1
    except ValueError:
        seconds = input("Please input a number.")

for i in range(seconds, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print("Time's up!")

#STGHECKER#

import random

a = random.randint(500, 510)

b = int(input("Enter the number: "))

start = 1


flag = False

while (start < 6):
    if (a == b):
        print("You guessed the right value")
        flag = True
        break
    else:
        print("You guessed the wrong value. Try again......")
        print("Attempt left", 6 - start)
        
        if (b > a):
            print("Your guessed number is greater than the correct value")
        else:
            print("Your guessed number is less than the correct value")
        
        b = int(input("Enter the number: "))
        start += 1


if not flag:
    print("Game Over! The correct number was", a)

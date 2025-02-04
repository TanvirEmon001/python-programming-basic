import random

a = random.randint(500, 510)

b = int(input("Enter the number: "))

start = 1

while (start < 6):
    if (a == b):
        print("You guessed the right value")
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
        
if (start == 6 and a != b):
    print("Game Over! The correct number was", a)

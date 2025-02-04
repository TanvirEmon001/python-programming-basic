import random

a = random.randint(500,510)

b = int(input("Enter the number : "))

start = 1

while (start<6):
    if(a==b):
        print("You guessed the right value")
        break
    else:
        print("You guessed the wrong value. Try again......")
        print("Attempt left", 6-start)
        if(b>a):
            print("Your guessed number is grater than correct value")
        else:
            print("Your guessed number is less than correct")
        b = int(input("Enter the number: "))
        start +=1





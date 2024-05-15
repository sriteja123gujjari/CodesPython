import random

ran_num = int(input("Type a number : "))

r = random.randrange(0,ran_num)
guesess =0

while True:
    guesess+=1
    guess = int(input(f"Enter a number to guess correctly between {ran_num}: "))
    

    if(r==guess):
        print(f"Correct! {r} is the number :)")
        break
    elif guess > r:
        print("You're above the number!")
    else:
        print("Yoy're below the number!")

print("You got it in",guesess,"times")


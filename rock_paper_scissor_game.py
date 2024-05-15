import random

options = ["rock","paper","scissors"]

co_wins = 0
user_wins = 0

while True:
    user = input("Type rock/paper/scissors to play the game (RPS) and Type 'Q' to Exit : ").lower()

    if user == "q":
        break
    if user not in options:
        continue

    ran = random.randint(0,2)

    computer_pick = options[ran]
    print("computer picked",computer_pick)

    #same
    if user == "rock" and computer_pick =="rock":
        continue
    if user == "scissors" and computer_pick =="scissors":
        continue
    if user == "paper" and computer_pick =="paper":
        continue

    #different
    if user =="rock" and computer_pick == "scissors":
        print("You won rocked it!")
        user_wins+=1

    elif user =="paper" and computer_pick == "rock":
        print("you won scraped it!")
        user_wins+=1

    elif user =="scissors" and computer_pick =="paper":
        print("you won scissored it!")
        user_wins+=1

    else:
        print("you lost!")
        co_wins+=1
    
print("You won",user_wins,"times.")
print("Computer won",co_wins,"times.")
print("Thanks Wnat to play again :)")
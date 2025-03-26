import random

user_win=0
computer_win=0

options=["rock", "paper", "scissor"]

while True:
    user_input=input("Type Rock/Paper/Scissor or Q for quit: ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue

    rand_number= random.randint(0,2)
    computer_picks=options[rand_number]
    print("computer pick", computer_picks +".")

    if user_input== "rock" and computer_picks=="scissor":
        print("YOU WON !")
        user_win+=1

    elif user_input== "paper" and computer_picks=="rock":
        print("YOU WON !")
        user_win+=1

    elif user_input== "scissor" and computer_picks=="paper":
        print("YOU WON !")
        user_win+=1

    else:
        print("YOU LOOSE!")



print("you won",user_win,"times")
print("computer won", computer_win,"times")


print("Goodbye !")

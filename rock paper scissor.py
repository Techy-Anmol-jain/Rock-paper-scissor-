import random
print("Rock","Paper","Scissor Game")

item_list = ["rock","paper","scissor"]
user_choice = input("Enter your first move(rock,paper,scissor): ").lower()
if user_choice not in item_list:
    print("Invalid input.Result will not be shown.")
else:
    print("Continuing........")

comp_choice = random.choice(item_list)
print(f"User choice is {user_choice} and Computer choice is {comp_choice}")

if user_choice == comp_choice:
    print("The match is tie")
elif user_choice == "rock":
    if comp_choice == "paper":
        print("Paper covers the rock,Computer wins")
    else:
        print("Rock smashes the scissor,You win")

elif user_choice == "paper":
    if comp_choice == "rock":
        print("Paper covers the rock,You win")
    else:
        print("scissor cuts the paper,Computer wins")    
        
elif user_choice == "scissor":
    if comp_choice == "rock":
        print("Rock smashes the scissor,Computer wins")
    else:
        print("scissor cuts the paper, You win")
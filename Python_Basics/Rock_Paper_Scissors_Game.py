#This is a mini project - a Rock, Paper, Scissors Game.
import random
def get_choices():
    player_choice=input("Enter your choice(rock,paper,scissors):")
    options=["rock","paper","scissors"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices
def check_win(player,computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player==computer:
        return("It's a tie!")
    elif player=="rock":
        if computer=="paper":
            return("You Lose")
        else:
            return("YOU WIN!")
    elif player=="paper":
        if computer=="scissors":
            return("You Lose")
        else:
            return("YOU WIN!")
    elif player=="scissors":
        if computer=="rock":
            return("You Lose")
        else:
            return("YOU WIN!")

choices=get_choices()
result=check_win(choices["player"],choices["computer"])
print(result)
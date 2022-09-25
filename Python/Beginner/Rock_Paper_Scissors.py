import random

potential_choices = ["Rock", "Paper", "Scissors"]



player_choice = "rock"

#player_choice is a variable
#The string Rock is assigned to the player_choice variable

computer_choice = "paper"

#computer_choice is variable
#the string paper is assigned to the computer_choice variable

def get_choices():
    player_choice = input("Enter a choice (Rock, Paper, Scissors): ")
    computer_choice = random.choice(potential_choices)
    choices = {"Player": player_choice, "Computer": computer_choice}
    return choices

'''
def example_function():
    return "Hi"

response = example_function()

print(response)

choices = get_choices()

print(choices)

dict_example = {"name": "beau", "color" : "blue"}
'''
def check_win(player,computer):
    print(f"You chose {player}, the computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    
    elif player == "Rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose"
    
    elif player == "Paper":
        if computer == "Rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose"
    
    elif player == "Scissors":
        if computer == "Paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose"

choices = get_choices()


result = check_win(choices["Player"], choices["Computer"])

print(result)
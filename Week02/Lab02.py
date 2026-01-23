# Isaac Natera - Week 02
# Solution to Week 02 questions
# Open Terminal (CTRL + `)
# How to push to git hub
# 1. git add .
# 2. git commit -m "Commit Message"
# 3. git push
import random

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter your choice (1-Rock, 2-Paper, 3-Scissors) :")
playerChoice = int(playerChoice)

# Input always returns strings
if playerChoice < 1 or playerChoice > 3:
    print("Error: Input should be an integer between 1 and 3")
else:
    # Determinte the winner logic using if/elif/else statements
    computerChoice = random.randint(1,3)
    if playerChoice == computerChoice:
        print("It's a tie, you both lose.")
    elif playerChoice == 1 and computerChoice == 3:
        print("You win! Rock beats Scissors!")
    elif playerChoice == 2 and computerChoice == 1:
        print("You win! Paper beats Rock!")
    elif playerChoice == 3 and computerChoice == 2:
        print("You win! Scissors beats Paper!")
    else:
        print("You lose!")
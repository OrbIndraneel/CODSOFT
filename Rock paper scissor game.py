#Rock paper scissor game
import random

def game():
    cho1 = input("Enter your choice [rock, paper, scissor]: ").lower()
    cho2 = random.choice(["rock", "paper", "scissor"])
    if cho1 not in ["rock", "paper", "scissor"]:
        cho1 = input("Invalid input. Please enter rock, paper or scissor: ").lower
    if cho1 == cho2:
        print(f"Computer chose {cho2}.")
        print(f"Both players selected {cho1}. It's a tie!")
        game()
    elif cho1=="rock" and cho2=="paper":
        print(f"Computer chose {cho2}.")
        print(f"Paper covers rock. Computer wins!")
    elif cho1=="rock" and cho2=="scissor":
        print(f"Computer chose {cho2}.")
        print(f"Rock smashes scissors. You win!")
    elif cho1=="scissor" and cho2=="paper":
        print(f"Computer chose {cho2}.")
        print(f"Scissors cuts paper. You win!")
    elif cho1=="scissor" and cho2=="rock":
        print(f"Computer chose {cho2}.")
        print(f"Rock smashes scissors. Computer wins!")
    elif cho1=="paper" and cho2=="rock":
        print(f"Computer chose {cho2}.")
        print(f"Paper covers rock. You win!")
    elif cho1=="paper" and cho2=="scissor":
        print(f"Computer chose {cho2}.")
        print(f"Scissors cuts paper. Computer wins!")
    else:
        pass

game()
running= True
while running:
    re=input("Would you like to play again [Y/N] ?").lower()
    if re == "y":
        game()
    elif re == "n":
        print("Thanks for playing")
        running= False
    else:
        print("Invalid input. Please enter Y or N")


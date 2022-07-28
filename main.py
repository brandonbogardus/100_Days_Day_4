from Hands import rock, paper, scissors
import random

game_choice = random.randint(0, 2)

player_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, & 2 for scissors. "))

if game_choice == 0 and player_choice == 0:
    print(f"The game chose {rock}.")
    print(f"You chose {rock}.")
    print("It's a tie.")
elif game_choice == 0 and player_choice == 1:
    print(f"The game chose {rock}.")
    print(f"You chose {paper}.")
    print("You win!")
elif game_choice == 0 and player_choice == 2:
    print(f"The game chose {rock}.")
    print(f"You chose {scissors}.")
    print("You lose.")
elif game_choice == 1 and player_choice == 0:
    print(f"The game chose {paper}.")
    print(f"You chose {rock}.")
    print("You lose")
elif game_choice == 1 and player_choice == 1:
    print(f"The game chose {paper}.")
    print(f"You chose {paper}.")
    print("It's a tie")
elif game_choice == 1 and player_choice == 2:
    print(f"The game chose {paper}.")
    print(f"You chose {scissors}.")
    print("You win!")
elif game_choice == 2 and player_choice == 0:
    print(f"The game chose {scissors}.")
    print(f"You chose {rock}.")
    print("You win!")
elif game_choice == 2 and player_choice == 1:
    print(f"The game chose {scissors}.")
    print(f"You chose {paper}.")
    print("You lose.")
elif game_choice == 2 and player_choice == 2:
    print(f"The game chose {rock}.")
    print(f"You chose {rock}.")
    print("It's a tie.")
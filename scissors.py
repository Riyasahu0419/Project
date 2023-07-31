from random import randint


def get_computer_move():
    t = ["Rock", "Paper", "Scissors"]

    return t[randint(0, 2)]


def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "Draw"
    elif player_move == "Rock":
        return "Player" if computer_move == "Scissors" else "Computer"
    elif player_move == "Paper":
        return "Player" if computer_move == "Rock" else "Computer"
    elif player_move == "Scissors":
        return "Player" if computer_move == "Paper" else "Computer"
    else:
        return "Invalid"


def play_game():
    player_move = ""
    chances = 0
    max_chances = 5

    while player_move != "exit" and chances < max_chances:
        print(
            "\nChoose Option Type 'Rock', 'Paper', or 'Scissors'")
        player_move = input("\nRock, Paper, Scissors? : ").capitalize()

        if player_move in ["Rock", "Paper", "Scissors"]:
            computer_move = get_computer_move()
            print("Computer chose:",computer_move)

            winner = determine_winner(player_move, computer_move)
            if winner == "Draw":
                print("It's a Draw!")

            elif winner == "Player":
                print("You win! ")
    

            else:
                print("Computer wins! ")

            chances += 1
        elif player_move == "Exit":
            break
          
        else:
            print(
                "Invalid input. Please enter 'Rock', 'Paper', 'Scissors', or 'Exit'.")


    print("Game Over!")
   


play_game()

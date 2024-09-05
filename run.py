import random


def print_introduction():
    """print the introduction of the game"""
    print(f"""
The rules are:
1. Rock vs Paper ... Paper wins
2. Rock vs Scissors... Rock wins
3. Paper vs Scissors... Scissors wins
    """)


def main():
    print_introduction()

    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

    while True:
        # User's choice
        while True:
            try:
                choice_num = int(
                    input(
                        f"""
Please enter your choice (1-Rock, 2- Paper, 3- Scissors):"""
                    ).strip()
                )

                if choice_num in [1, 2, 3]:
                    choice_name = choices[choice_num]
                    break
                else:
                    print("Invalid choice, please enter 1, 2, or 3.")
            except ValueError:
                print(
                    "Invalid input. Please enter a number (1- R, 2- P, 3- S)."
                )

        print('Your choice is:', choice_name)

        # Computer's choice
        comp_choice_num = random.randint(1, 3)
        comp_choice_name = choices[comp_choice_num]
        print("Computer's choice is:", comp_choice_name)

        # Check for a draw
        if choice_num == comp_choice_num:
            print(f"Both chose {choice_name}. It's a draw!")
            result = 'Draw'
        else:
            # Check for win/loss
            if (choice_num == 1 and comp_choice_num == 3) or \
                            (choice_num == 2 and comp_choice_num == 1) or \
                            (choice_num == 3 and comp_choice_num == 2):
                print(f"{choice_name} beats {comp_choice_name}. You win!")
                result = 'User'
            else:
                print(
                    f"{comp_choice_name} beats {choice_name}. Computer wins!"
                )
                result = 'Computer'

        # Asking for another round
        play_again = input(
            "Would you like to play again?(Y/N):"
        ).strip().lower()
        if play_again != 'y':
            print("Hope you had fun! Goodbye!")
            break


if __name__ == "__main__":
    main()

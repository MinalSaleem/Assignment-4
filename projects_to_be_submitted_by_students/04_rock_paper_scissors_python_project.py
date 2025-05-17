import random

choices = ["rock","paper","scissor"]

def main():
    print("Welcome to Rock Paper Scissor Game: ✨")
    print('''Rules:
    Rock beats Scissors
    Scissors beats Paper
    Paper beats Rock''')
    print()

    while True:

        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if user_choice not in choices:
            print("Invalid choice! Try again.")

        computer_choice = random.choice(choices)
        print("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
            print("You win! 🎉")
        else:
            print("Computer wins!")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            break 

if __name__ == "__main__":
    main()
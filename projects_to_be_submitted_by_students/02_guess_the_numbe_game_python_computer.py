import random

def main():
    
    secret_number = random.randint(1, 100)
    attempt = 0

    while True:
        try:
            user_guess = int(input("Take a guess! Pick a number between 1 and 100: "))
            attempt += 1

            if user_guess > secret_number:
                print("Your Guess is too high!")
            elif user_guess < secret_number:
                print("Your Guess is too low!")
            else:
                print(f"You got it! The number {user_guess} was correct. Attempts: {attempt} ✨")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()
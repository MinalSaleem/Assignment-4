def main():
    print("Welcome to Guess the Number Game!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    print()
    
    low, high = 1, 100
    attempt = 0

    while low <= high:
        guess = (low + high) // 2
        attempt += 1
        print(f"My guess is: {guess}")

        feedback = input("Is it (h)high, (l)low, or (c)correct? : ").lower()
        print()

        if feedback == 'c':
            print(f"🎯 Got it! Your number {guess} was guessed in just {attempt} tries! 🎉")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input! Please enter 'h', 'l', or 'c'.")
    
if __name__ == "__main__":
    main()
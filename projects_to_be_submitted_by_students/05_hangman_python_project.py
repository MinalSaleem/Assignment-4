import random

word_list = ["typescript", "developer", "python", "frontend", "fullstack"]

def main():
    word = get_word()  
    guess_letter = set()
    attempts = 6

    print(" Hangman Game! Try to guess the word.")
    
    while attempts > 0:
        print("\nWord:", display_word(word, guess_letter))
        print(f"Remaining attempts: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue
        
        if guess in guess_letter:
            print("You already guess that letter!")
            continue

        guess_letter.add(guess)
        
        if guess in word:
            print("Good guess!")
            if all(letter in guess_letter for letter in word):
                print("\n🎉 Congratulations! You guess the word:", word)
                break
        else:
            print("Wrong guess!")
            attempts -= 1
    
    if attempts == 0:
        print("\n Game Over! The word is:", word)

def get_word():
    return random.choice(word_list).lower()

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

if __name__ == "__main__":
    main()
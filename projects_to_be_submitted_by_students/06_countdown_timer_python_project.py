import time

def main():
    print("Countdown Timer")
    try:
        user_input = int(input("Enter time in seconds: "))
        countdown_timer(user_input)
    except ValueError:
        print("Please enter a valid number.")

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(f"Time left: {time_format}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("\n Time's up!")


if __name__ == '__main__':
    main()
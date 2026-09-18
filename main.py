import random


def read_guess(low, high):
    while True:
        value = input(f"Enter a number from {low} to {high}: ").strip()
        try:
            guess = int(value)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if low <= guess <= high:
            return guess
        print("That number is outside the range.")


def play():
    low, high, attempts = 1, 100, 7
    secret = random.randint(low, high)
    print("\nI chose a number between 1 and 100.")

    for turn in range(1, attempts + 1):
        guess = read_guess(low, high)
        if guess == secret:
            print(f"Correct! You solved it in {turn} attempt(s).")
            return
        direction = "higher" if guess < secret else "lower"
        print(f"Try {direction}. Attempts left: {attempts - turn}")

    print(f"Game over. The number was {secret}.")


def main():
    while True:
        play()
        if input("Play again? (y/n): ").strip().lower() != "y":
            break


if __name__ == "__main__":
    main()

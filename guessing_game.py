import random


def guessing_game():
    """
    Guessing game's implementation
    """
    print("\nGuessing game instructions:\n\n1. Each user have 3 tries to guess the game.\n")
    while True:
        lower_limit_input = input("Select lower limit: ")
        try:
            lower_limit = int(lower_limit_input)
        except ValueError:
            print("[X] Provide an integer as lower limit.")
            continue
        upper_limit_input = input("Select upper limit: ")
        try:
            upper_limit = int(upper_limit_input)
        except ValueError:
            print("[X] Provide an integer as upper limit.")
            continue
        # Validate limits
        if lower_limit < 0:
            print("[X] Lower limit can't be less than zero. Please provide a new pair of limits.")
            continue
        elif lower_limit > upper_limit:
            print("[X] Lower limit can't be greater than upper limit. Please provide a new pair of limits.")
            continue
        elif lower_limit == upper_limit:
            print("[X] Limits can't be the same number. Please provide a new pair of limits.")
            continue
        print(f"\nYour limits are {lower_limit} - {upper_limit}\n\n")
        break

    # Calculate the answer
    answer = random.randint(lower_limit, upper_limit)

    # Get the guesses
    tries = 0
    while True:
        if tries == 3:
            print(f"\n3 fails. You lost! The answer was {answer}\n")
            break
        tries += 1
        user_guess = input("Your guess: ")
        try:
            guess = int(user_guess)
        except ValueError:
            print("[X] Provide an integer as guess.")
            continue
        if guess == answer:
            print("You're correct!")
            break
        elif guess > upper_limit:
            print(f"Really? Your upper limit is {upper_limit}. Try again.")
            continue
        elif guess < lower_limit:
            print(f"Really? Your lower limit is {lower_limit}. Try again.")
            continue
        elif guess < answer:
            print("Too low")
            continue
        elif guess > answer:
            print("Too high.")
            continue
        

def main():
    guessing_game()


if __name__ == "__main__":
    main()

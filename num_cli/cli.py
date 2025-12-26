import random

def generate_number(level):
    if level == 1:
        return random.randint(1, 10)
    elif level == 2:
        return random.randint(1, 50)
    elif level == 3:
        return random.randint(1, 100)
    else:
        raise ValueError("Invalid level. Must be 1, 2, or 3.")

def check_guess(guess, target):
    if guess == target:
        return "correct"
    elif guess > target:
        return "high"
    else:
        return "low"

if __name__ == "__main__":
    while True:
        try:
            print("Choose difficulty level:")
            print("1 - Easy (1 to 10)")
            print("2 - Medium (1 to 50)")
            print("3 - Hard (1 to 100)")
            level = int(input("Enter 1, 2, or 3: "))
            if level not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print("❌ Invalid input! Enter 1, 2, or 3.")

    num = generate_number(level)
    attempts = 0

    while True:
        while True:
            try:
                if level == 1:
                    guess = int(input("Guess a number from 1 to 10: "))
                elif level == 2:
                    guess = int(input("Guess a number from 1 to 50: "))
                else:
                    guess = int(input("Guess a number from 1 to 100: "))
                break
            except ValueError:
                print("❌ Please enter a valid number!")

        attempts += 1
        result = check_guess(guess, num)

        if result == "correct":
            print(f"🎉 Correct! You guessed the number in {attempts} tries.")
            break
        elif result == "high":
            print("📈 Too high! Try again.")
        else:
            print("📉 Too low! Try again.")

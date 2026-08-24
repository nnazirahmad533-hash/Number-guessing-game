import random

while True:
    print("\nWelcome to the Number Guessing Game!")

    # 1. Difficulty Validation & Configuration
    while True:
        print("\nChoose difficulty:")
        print("- Easy   (1-50, 10 attempts)")
        print("- Medium (1-100, 7 attempts)")
        print("- Hard   (1-500, 5 attempts)")
        
        choice = input("Type 'easy', 'medium', or 'hard': ").strip().lower()

        if choice == "easy":
            max_range = 50
            max_attempts = 10
            break
        elif choice == "medium":
            max_range = 100
            max_attempts = 7
            break
        elif choice == "hard":
            max_range = 500
            max_attempts = 5
            break
        else:
            print("❌ Invalid difficulty! Please choose easy, medium, or hard.")

    # 2. Game Setup
    secret_number = random.randint(1, max_range)
    attempts = 0
    guess = None

    print(f"\nI'm thinking of a number between 1 and {max_range}.")

    # 3. Game Loop
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue  # Doesn't consume an attempt

        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try higher.")
        elif guess > secret_number:
            print("Too high! Try lower.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempt(s)!")
            break

    if attempts == max_attempts and guess != secret_number:
        print(f"💀 Game over! The secret number was {secret_number}.")

    # 4. Replay Option (with .strip().lower())
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again not in ["yes", "y"]:
        print("Thanks for playing! Goodbye!")
        break

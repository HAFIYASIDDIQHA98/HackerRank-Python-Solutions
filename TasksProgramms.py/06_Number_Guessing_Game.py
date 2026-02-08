import random

def guess_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("--- 🎯 Number Guessing Game ---")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too Low! Try again.")
            elif guess > secret_number:
                print("Too High! Try again.")
            else:
                print(f"🎉 Correct! You found it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

guess_game()

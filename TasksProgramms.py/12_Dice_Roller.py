import random

def roll_dice():
    while True:
        choice = input("Roll the dice? (y/n): ").lower()
        if choice == 'y':
            number = random.randint(1, 6)
            print(f"🎲 You rolled a: {number}")
        elif choice == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'y' or 'n'")

roll_dice()

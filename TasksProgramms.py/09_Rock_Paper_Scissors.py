import random

def play_game():
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    user = input("Choose Rock, Paper, or Scissors: ").lower()

    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You Win!")
    else:
        print("💻 Computer Wins!")

play_game()

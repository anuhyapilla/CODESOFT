import random

def rps_game():
    print("------ Rock-Paper-Scissors Game ------")
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    comp_score = 0

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_choice == "quit":
            break
        if user_choice not in choices:
            print("❌ Invalid choice, try again!")
            continue

        comp_choice = random.choice(choices)
        print(f"Computer chose: {comp_choice}")

        if user_choice == comp_choice:
            print("🤝 It's a tie!")
        elif (user_choice == "rock" and comp_choice == "scissors") or \
             (user_choice == "paper" and comp_choice == "rock") or \
             (user_choice == "scissors" and comp_choice == "paper"):
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            comp_score += 1

        print(f"Score => You: {user_score} | Computer: {comp_score}\n")

    print("------ Game Over ------")
    print(f"Final Score => You: {user_score} | Computer: {comp_score}")
    print("Thanks for playing!")

# Run the game
rps_game()

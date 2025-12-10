# CODSOFT - Task 3: Password Generator
# Author: Anuhya Pilla

import random
import string

def generate_password():
    print("------ Password Generator ------")

    try:
        length = int(input("Enter desired password length: "))

        if length < 6:
            print("❌ Password too short. Minimum length is 6.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    # Ask user for complexity
    print("\nChoose password complexity:")
    print("1. Letters only")
    print("2. Letters + Numbers")
    print("3. Letters + Numbers + Symbols")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        characters = string.ascii_letters
    elif choice == "2":
        characters = string.ascii_letters + string.digits
    elif choice == "3":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("❌ Invalid choice.")
        return

    # Generate password
    password = "".join(random.choice(characters) for _ in range(length))

    print("\n✅ Your Secure Password is:")
    print(password)
    print("-------------------------------")


# Run the program
generate_password()

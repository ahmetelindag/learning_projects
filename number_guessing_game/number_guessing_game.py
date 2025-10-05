# Number Guessing Game
# Created by Ahmet 

import random

# Generate a random number between 1 and 30

secretNumber = random.randint(1, 30)
print("Welcome to the Number Guessing Game")
print("-----------------------------------")
print("I'm thinking of a number between 1 and 30.")
print("You have 5 attempts to guess the number.\n")

# Set the initial number of attempts
attempts = 5
while attempts > 0:
    # Get the player's guess
    guess = int(input("Enter your guess (1-30): "))
    if guess < 1 or guess > 30:
        print("Please guess a number within the range of 1 to 30.")
        continue
    if guess < secretNumber:
        print("Too low!")
    elif guess > secretNumber:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number in {5 - attempts + 1} attempts correctly!")
        break
    attempts -= 1
    print(f"You have {attempts} attempts left.\n")

# Check if all attempts are used
if attempts == 0:
    print(f"Sorry, you've used all your attempts. The number was {secretNumber}.")

print("\nThank you for playing the Number Guessing Game!")

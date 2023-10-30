import random

# Settings
range = 25
guesses = 5

# Get random number
random_number = random.randint(1, range)

# Initial guess
guess = int(input(f"Guess a number between 1 and {range}: "))

while guess != random_number:
    # If no more guesses
    if guesses == 1:
        print(f"You ran out of guesses! The number was {random_number}")
        exit()
    guesses = guesses - 1

    # Too high or too low
    if guess < random_number:
        print(f"Too Low!")
    if guess > random_number:
        print(f"Too High!")

    # Amount of guesses and do 'guess' instead of 'guesses' when 1 guess left
    if guesses == 1: print(f"1 guess left.") 
    else: print(f"{guesses} guesses left.")

    # New guess
    guess = int(input("Guess a number between 1 and 50: "))

print("Correct! You guessed it!!!!!!!!!!!")
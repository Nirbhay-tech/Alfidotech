import random
def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}: Enter your guess: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        attempts += 1
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            return
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
if __name__ == "__main__":
    number_guessing_game()
    print("Thank you for playing!")

import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    guess = int(input(f"Guess a number between 1 to {difficulty}: "))
    return guess


def compare_results(guess, secret_number):
    return guess == secret_number


def play_guess(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    if compare_results(guess, secret_number):
        print("Congrats you won!")
        return True
    else:
        print("You lost, try next time.")
        return False

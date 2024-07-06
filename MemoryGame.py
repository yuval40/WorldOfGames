import random
import time
import os


def generate_sequence(difficulty):
    lst = list(range(1, 102))
    sequence = random.sample(lst, k=difficulty)
    print(sequence)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    return sequence





def get_list_from_user():

    guess = input("Try to remember the numbers you saw: ")
    guess_list = list(map(int, guess.split()))
    return guess_list


def is_list_equal(guess, sequence):
    return guess == sequence


def play_memory(difficulty):
    sequence = generate_sequence(difficulty)
    guess = get_list_from_user()
    if is_list_equal(guess, sequence):
        print("Congrats you won!")
        return True
    else:
        print("Sorry you lost, try next time.")
        return False



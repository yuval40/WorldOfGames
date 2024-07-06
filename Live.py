from MemoryGame import play_memory
from GuessGame import play_guess
from CurrencyRouletteGame import play_roulette
from Score import add_score
from Utils import screen_cleaner


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n")


def load_game():
    new_score = 0
    game_number = input("""1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back.
2. Guess Game - guess a number and see if you chose like the computer.
3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\nPlease choose a game to play: """)

    if game_number not in ["1", "2", "3"]:
        print("Please choose a game from 1 to 3.")
        return

    game_won = False
    game_difficulty = None

    if game_number == "1":
        screen_cleaner()
        print("Welcome to Memory game!")
        game_difficulty = int(input("Please choose game difficulty from 1 to 5: "))
        game_won = play_memory(game_difficulty)
    elif game_number == "2":
        print("Welcome to Guess game!")
        game_difficulty = int(input("Please choose game difficulty from 1 to 5: "))
        game_won = play_guess(game_difficulty)
    elif game_number == "3":
        print("Welcome to Currency Roulette! - try and guess the value of a random amount of USD in ILS")
        game_difficulty = int(input("Please choose game difficulty from 1 to 5: "))
        game_won = play_roulette(game_difficulty)

    if game_won:
        add_score(game_difficulty)
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    name = input("Enter your name: ")
    welcome(name)
    load_game()


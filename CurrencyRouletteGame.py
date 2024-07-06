import random
import requests

API_KEY = "fca_live_qtInEATZDQZEFUhK7wtsDcHwQrwE6ypv1ncMbueJ"
BASE_CURRENCY = 'USD'
TARGET_CURRENCY = 'ILS'
URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"


def get_exchange_rate():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data['data'][TARGET_CURRENCY]
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")


def get_money_interval(difficulty, exchange_rate, random_amount):
    t = random_amount * exchange_rate
    interval = (t - (5 - difficulty), t + (5 - difficulty))
    return interval


def get_guess_from_user(random_amount):
    try:
        guess = float(input(f"How much is {random_amount} USD in ILS? Enter your guess: "))
        return guess
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_guess_from_user(random_amount)


def play_roulette(difficulty):
    exchange_rate = get_exchange_rate()
    random_amount = random.randint(1, 100)
    interval = get_money_interval(difficulty, exchange_rate, random_amount)
    guess = get_guess_from_user(random_amount)

    if interval[0] <= guess <= interval[1]:
        print(f"Congratulations! Your guess is correct.")
        return True
    else:
        print(f"Sorry, your guess is incorrect. The correct range was between {interval[0]} and {interval[1]}.")
        return False



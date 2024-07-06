import os
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read().strip()
            if not data:
                return BAD_RETURN_CODE
            return int(data)
    except (FileNotFoundError, ValueError):
        return BAD_RETURN_CODE


def screen_cleaner():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

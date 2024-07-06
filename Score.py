import os
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE


POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5


def read_score():
    if not os.path.exists(SCORES_FILE_NAME):
        return 0
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = int(file.read().strip())
            return score
    except Exception as e:
        print(f"Error reading the score file: {e}")
        return 0


def write_score(score):
    try:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(score))
    except Exception as e:
        print(f"Error writing to the score file: {e}")


def add_score(difficulty):
    current_score = read_score()
    if current_score == BAD_RETURN_CODE:
        print("Failed to read current score.")
        return BAD_RETURN_CODE

    new_points = POINTS_OF_WINNING(difficulty)
    new_score = current_score + new_points
    write_score(new_score)
    print(f"Added {new_points} points for difficulty {difficulty}. New score is {new_score}.")
    return new_score


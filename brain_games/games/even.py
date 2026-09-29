import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(number):
    return number % 2 == 0


def generate_round_data():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    if is_even(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return str(question), correct_answer
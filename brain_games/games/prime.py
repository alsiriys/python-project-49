import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divider = 3
    while divider * divider <= number:
        if number % divider == 0:
            return False
        divider += 2
    return True


def generate_round_data():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = "yes" if is_prime(question) else "no"
    return str(question), correct_answer
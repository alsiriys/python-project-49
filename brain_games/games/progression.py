import random

DESCRIPTION = "What number is missing in the progression?"
MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_START = 1
MAX_START = 50
MIN_STEP = 1
MAX_STEP = 10


def generate_round_data():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    progression = []
    
    for i in range(length):
        element = str(start + i * step)
        progression.append(element)

    hidden_index = random.randint(0, length - 1)
    
    correct_answer = progression[hidden_index]
    
    progression[hidden_index] = ".."
    
    question = " ".join(progression)

    return question, correct_answer
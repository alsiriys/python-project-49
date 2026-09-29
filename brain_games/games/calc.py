import random

DESCRIPTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 25
OPERATORS = ['+', '-', '*']


def generate_round_data():
    number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(OPERATORS)

    question = f"{number1} {operator} {number2}"

    match operator:
        case '+':
            correct_answer = number1 + number2
        case '-':
            correct_answer = number1 - number2
        case '*':
            correct_answer = number1 * number2
        
    return question, str(correct_answer)
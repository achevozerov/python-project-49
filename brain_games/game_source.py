import prompt
import math
import random


def greetings():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    return name


def make_even():
    q = random.randint(0, 100)
    answer = q % 2 == 0

    if answer:
        answer = 'yes'
    else:
        answer = 'no'

    return (q, answer)


def make_calc():
    q1 = random.randint(1, 25)
    q2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])

    q = f'{q1} {operator} {q2}'

    if operator == '+':
        answer = str(q1 + q2)
    elif operator == '-':
        answer = str(q1 - q2)
    else:
        answer = str(q1 * q2)

    return (q, answer)


def make_gcd():
    q1 = random.randint(1, 100)
    q2 = random.randint(1, 100)
    q = f'{q1} {q2}'

    answer = str(math.gcd(q1, q2))

    return (q, answer)


def make_progression():
    step = random.randint(1, 9)
    pos_index = random.randint(0, 9)
    progression_len = random.randint(5, 10)
    progression = [random.randint(1, 10)]

    for i in range(0, progression_len):
        progression.append(progression[i] + step)

    progression_chars = list(map(str, progression))
    progression_chars[pos_index] = "**"

    q = ' '.join(progression_chars)
    answer = str(progression[pos_index])
    return (q, answer)

def make_prime():
    num = random.randint(4, 100)
    answer = 'yes'

    for i in range(2, num):
        if num % i == 0:
            answer = 'no'

    q = str(num)

    return (q, answer)

def ask_question(q: str, answer: str):
    print(f'Question: {q}')
    user_answer = prompt.string('Your answer: ')

    if answer == user_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
        return False

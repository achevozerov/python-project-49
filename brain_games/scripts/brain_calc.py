from brain_games import game_source as gs


def main(difficult=3):
    name = gs.greetings()
    print('What is the result of the expression?')

    for i in range(0, difficult):

        q, answer = gs.make_calc()

        if not gs.ask_question(q, answer):
            break

        if i + 1 == difficult:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

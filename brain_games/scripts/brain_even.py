from brain_games import game_source as gs


def main(difficult=3):
    name = gs.greetings()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(0, difficult):

        q, answer = gs.make_even()

        if not gs.ask_question(q, answer):
            print(f'Let\'s try again, {name}!')
            break

        if i + 1 == difficult:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

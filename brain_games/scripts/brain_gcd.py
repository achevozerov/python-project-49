from brain_games import game_source as gs


def main(difficult=3):
    name = gs.greetings()
    print('Find the greatest common divisor of given numbers.')

    for i in range(0, difficult):

        q, answer = gs.make_gcd()

        if not gs.ask_question(q, answer):
            break

        if i + 1 == difficult:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

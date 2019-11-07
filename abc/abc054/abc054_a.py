'''
A - One Card Poker
https://atcoder.jp/contests/abc054/tasks/abc054_a

>>> main(8, 6)
Alice

>>> main(1, 1)
Draw

>>> main(13, 1)
Bob
'''


def main(a, b):
    def re_define(input_):
        '''強さ順にする'''
        if input_ == 1:
            return 13

        return input_ - 1

    a = re_define(a)
    b = re_define(b)

    if a > b:
        print('Alice')
    elif a < b:
        print('Bob')
    else:
        print('Draw')


if __name__ == "__main__":
    a, b = map(int, input().split(' '))

    main(a, b)

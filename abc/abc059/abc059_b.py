'''B - Comparison
https://atcoder.jp/contests/abc059/tasks/abc059_b

>>> main(36, 24)
GREATER
>>> main(850, 3777)
LESS
>>> main(9720246, 22516266)
LESS

'''


def main(a, b):
    if a > b:
        print('GREATER')
    elif a < b:
        print('LESS')
    else:
        print('EQUAL')


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    main(a, b)


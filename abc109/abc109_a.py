'''A - ABC333
https://atcoder.jp/contests/abc109/tasks/abc109_a

>>> main(3, 1)
Yes
>>> main(1, 2)
No
>>> main(2, 2)
No'''


def main(a, b):
    if a * b % 2 == 0:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    a, b = map(int, input().split(' '))

    main(a, b)


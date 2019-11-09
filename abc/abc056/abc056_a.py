'''A - HonestOrDishonest
https://atcoder.jp/contests/abc056/tasks/abc056_a

>>> main('H', 'H')
H
>>> main('D', 'H')
D
>>> main('D', 'D')
H

'''


def main(a, b):
    if a == b:
        print('H')
    else:
        print('D')


if __name__ == "__main__":
    a, b = input().split()

    main(a, b)

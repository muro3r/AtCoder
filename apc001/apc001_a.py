'''A - Two Integers
https://atcoder.jp/contests/apc001/tasks/apc001_a

>>> main(8, 6)
16
>>> main(3, 3)
-1

>>> main(120000000, 80000000)
120000000

'''


def main(x, y):
    if x / y == 0:
        print(-1)
    elif x >= 10**18:
        print(x)
    else:
        print(x * 2)


if __name__ == '__main__':
    x, y = map(int, input().split(' '))
    main(x, y)


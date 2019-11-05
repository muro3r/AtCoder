'''A - Cats and Dogs
https://atcoder.jp/contests/abc094/tasks/abc094_a

>>> main(3, 5, 4)
YES
>>> main(2, 2, 6)
NO
>>> main(5, 3, 2)
NO'''


def main(a, b, x):
    if a <= x <= a + b:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    a, b, x = map(int, input().split(' '))
    main(a, b, x)

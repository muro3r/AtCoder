'''B - TAKOYAKI FESTIVAL 2019
https://atcoder.jp/contests/abc143/tasks/abc143_b

>>> main(3, [3, 1, 2])
11
>>> main(7, [5, 0, 7, 8, 3, 3, 2])
312

'''

from itertools import combinations


def main(n, d):
    value = 0

    for p in combinations(d, 2):
        value += p[0] * p[1]

    print(value)


if __name__ == "__main__":
    n = int(input())
    d = list(map(int, input().split(' ')))

    main(n, d)

"""B - Traveling AtCoDeer Problem
https://atcoder.jp/contests/abc064/tasks/abc064_b

>>> main(4, [2, 3, 7, 9])
7
>>> main(8, [3, 1, 4, 1, 5, 9, 2, 6])
8

"""


def main(n, a):
    min_, max_ = min(a), max(a)

    print(max_ - min_)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split(" ")))

    main(n, a)

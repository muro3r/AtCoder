"""B - Shift only
https://atcoder.jp/contests/abc081/tasks/abc081_b
N
A_1 A_2 ... A_N

>>> main(3, [8, 12, 40])
2
>>> main(4, [5, 6, 8, 10])
0
>>> main(6, [382253568, 723152896, 37802240, 379425024, 404894720, 471526144])
8
"""


def main(n, a):
    count = 9 ** 10

    for a in a:
        c = 0
        while a % 2 == 0:
            a /= 2
            c += 1
        if c < count:
            count = c

    print(count)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    main(n, a)

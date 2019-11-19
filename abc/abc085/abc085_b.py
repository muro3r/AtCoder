"""B - Kagami Mochi
https://atcoder.jp/contests/abc085/tasks/abc085_b
N
d_1
:
d_N

>>> main(4, [10, 8, 8, 6])
3
>>> main(3, [15, 15, 15])
1
>>> main(7, [50, 30, 50, 100, 50, 80, 30])
4
"""


def main(n: int, d: list):
    d = set(d)
    print(len(d))


if __name__ == "__main__":
    n = int(input())
    d = [int(input()) for _ in range(n)]

    main(n, d)

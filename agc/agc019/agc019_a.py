"""A - Ice Tea Store
https://atcoder.jp/contests/agc019/tasks/agc019_a
Q H S D
N

>>> main(20, 30, 70, 90, 3)
150
>>> main(10000, 1000, 100, 10, 1)
100
>>> main(10, 100, 1000, 10000, 1)
40
>>> main(12345678, 87654321, 12345678, 87654321, 123456789)
1524157763907942
"""


def main(q: int, h: int, s: int, d: int, n: int):
    print((n // 2) * min(q * 8, h * 4, s * 2, d) + (n % 2) * min(q * 4, h * 2, s))


if __name__ == "__main__":
    q, h, s, d = map(int, input().split())
    n = int(input())

    main(q, h, s, d, n)

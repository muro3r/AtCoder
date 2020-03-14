"""C - Christmas Eve
https://atcoder.jp/contests/abc115/tasks/abc115_c
N K
h_1
h_2
:
h_N

>>> main(5, 3, [10, 15, 11, 14, 12])
2
>>> main(5, 3, [5, 7, 5, 7, 7])
0
"""


def main(n: int, k: int, h: list):
    h.sort()

    print(min([h[i + k - 1] - h[i] for i in range(n - k + 1)]))


if __name__ == "__main__":
    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]

    main(n, k, h)

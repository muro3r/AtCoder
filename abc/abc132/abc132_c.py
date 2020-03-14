"""C - Divide the Problems
https://atcoder.jp/contests/abc132/tasks/abc132_c
N
d_1 d_2 ... d_N

>>> main(6, [9, 1, 4, 4, 6, 7])
2
>>> main(8, [9, 1, 14, 5, 5, 4, 4, 14])
0
>>> main(14, [99592, 10342, 29105, 78532, 83018, 11639, 92015, 77204, 30914, 21912, 34519, 80835, 100000, 1])
42685
"""


def main(n, d):
    d.sort()

    middle = len(d) // 2
    print(d[(middle)] - d[(middle) - 1])


if __name__ == "__main__":
    n = int(input())
    d = list(map(int, input().split()))

    main(n, d)

"""C - Average Length
https://atcoder.jp/contests/abc145/tasks/abc145_c

N
x_1 y_1
:
x_N y_N

>>> main(3, [[0, 0], [1, 0], [0, 1]])
2.2761423749
>>> main(2, [[-879, 981], [-866, 890]])
91.9238815543

# >>> main(\
    8,\
    [\
        [-406, 10],\
        [512, 859],\
        [494, 362],\
        [-955, -475],\
        [128, 553],\
        [-986, -885],\
        [763, 77],\
        [449, 310],\
    ],\
)
7641.9817824387
"""
from itertools import permutations
from math import sqrt, factorial


def calc(prev: list, _next: list):
    return sqrt((prev[0] - _next[0]) ** 2 + (prev[1] - _next[1]) ** 2)


def main(n: int, x_y: list):
    length = []

    for p in permutations(range(n), n):
        # some tuple
        # (1,2,3)

        i = 0
        while i < len(p) - 1:
            length.append(calc(x_y[p[i]], x_y[p[i + 1]]))
            i += 1

    print("{:.10f}".format(sum(length) / factorial(n)))


if __name__ == "__main__":
    n = int(input())
    x_y = [list(map(int, input().split())) for _ in range(n)]

    main(n, x_y)

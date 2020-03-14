"""C - Traveling Plan
https://atcoder.jp/contests/arc093/tasks/arc093_a
N
A_1 A_2 ... A_N

>>> main(3, [3, 5, -1])
12
8
10
>>> main(5, [1, 1, 1, 2, 0])
4
4
4
2
4
>>> main(6, [-679, -2409, -3258, 3095, -3291, -4462])
21630
21630
19932
8924
21630
19288
"""


def main(n: int, a: list):
    for i in range(n):
        _a = a.copy()
        del _a[i]
        _a.insert(0, 0)
        _a.append(0)

        _sum = 0

        for j in range(n):
            _sum += abs(_a[j] - _a[j + 1])

        print(_sum)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    main(n, a)

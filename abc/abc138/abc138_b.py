"""B - Resistors in Parallel
https://atcoder.jp/contests/abc138/tasks/abc138_b
N
A_1 A_2 ... A_N
>>> main(2, [10, 30])
7.5
>>> main(3, [200, 200, 200])
66.66666666666667
>>> main(1, [1000])
1000.0
"""


def main(n: int, a: list):
    l = 0
    for _a in a:
        l += 1 / _a

    print(1 / l)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    main(n, a)

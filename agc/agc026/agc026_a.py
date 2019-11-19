"""A - Colorful Slimes 2
https://atcoder.jp/contests/agc026/tasks/agc026_a
N
a_1 a_2 ... a_N

>>> main(5, [1, 1, 2, 2, 2])
2
>>> main(3, [1, 2, 1])
0
>>> main(5, [1, 1, 1, 1, 1])
2
>>> main(14, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 1, 2, 3, 4])
4
"""


def main(n: int, a: list):
    prev = [0, 0]
    ans = 0

    for _a in a:
        if _a == prev[0]:
            if prev[1] % 2 == 0:
                ans += 1

            prev[1] += 1
        else:
            prev = [_a, 0]

    print(ans)


if __name__ == "__main__":
    n = int(input())
    a = map(int, input().split())

    main(n, a)

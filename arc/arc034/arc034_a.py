"""A - 首席
https://atcoder.jp/contests/arc034/tasks/arc034_1

N
a_1 b_1 c_1 d_1 e_1
a_2 b_2 c_2 d_2 e_2
:
a_N b_N c_N d_N e_N

>>> main(2, [[37, 54, 68, 66, 802], [58, 108, 106, 103, 871]])
481.4555555555555
>>> main(2, [[80, 120, 120, 120, 900], [0, 0, 0, 0, 731]])
550.0
"""


def main(n: int, caliculam: list):
    ans = 0

    for c in caliculam:
        _ans = sum(c[:-1]) + c[-1] * 110 / 900
        if _ans > ans:
            ans = _ans

    print(ans)


if __name__ == "__main__":
    n = int(input())
    caliculam = [list(map(int, input().split())) for _ in range(n)]

    main(n, caliculam)

"""B - Christmas Eve Eve
https://atcoder.jp/contests/abc115/tasks/abc115_b
N
p_1
p_2
:
p_N

>>> main(3, [4980, 7980, 6980])
15950
>>> main(4, [4320, 4320, 4320, 4320])
15120
"""


def main(n, p):
    p.sort()

    t = p.pop() // 2

    print(sum(p) + t)


if __name__ == "__main__":
    n = int(input())
    p = [int(input()) for _ in range(n)]

    main(n, p)

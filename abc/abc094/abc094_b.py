"""B - Toll Gates
https://atcoder.jp/contests/abc094/tasks/abc094_b
N M X
A_1 A_2 ... A_M

>>> main(5, 3, 3, [1, 2, 4])
1
>>> main(7, 3, 2, [4, 5, 6])
0
>>> main(10, 7, 5, [1, 2, 3, 4, 6, 8, 9])
3
"""


def main(n, m, x, a):
    line = [0 for _ in range(n)]

    for a in a:
        line[a - 1] = 1

    to_left = sum(line[x - 1 :])
    to_right = sum(line[x - 1 :: -1])

    print(min(to_left, to_right))


if __name__ == "__main__":
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))

    main(n, m, x, a)

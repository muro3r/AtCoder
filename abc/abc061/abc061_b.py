"""B - Counting Roads
https://atcoder.jp/contests/abc061/tasks/abc061_b
N M
a_1 b_1
:
a_M b_M

>>> main(4, 3, [[1, 2], [2, 3], [1, 4]])
2
2
1
1
>>> main(2, 5, [[1, 2], [2, 1], [1, 2], [2, 1], [1, 2]])
5
5
>>> main(8, 8, [[1, 2], [3, 4], [1, 5], [2, 8], [3, 7], [5, 2], [4, 1], [6, 8]\
])
3
3
2
2
2
1
1
2
"""


def main(n, m, a_b):
    road = [list() for n in range(n)]

    for a, b in a_b:
        road[a - 1].append(b)
        road[b - 1].append(a)

    for l in road:
        print(len(l))


if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    a_b = [list(map(int, input().split())) for _ in range(m)]

    main(n, m, a_b)

"""C - Candies
https://atcoder.jp/contests/abc087/tasks/arc090_a
N
A_{1, 1} A_{1, 2} ... A_{1, N}
A_{2, 1} A_{2, 2} ... A_{2, N}
>>> main(5, [3, 2, 2, 4, 1], [1, 2, 2, 2, 1])
14
>>> main(4, [1, 1, 1, 1], [1, 1, 1, 1])
5
>>> main(7, [3, 3, 4, 5, 4, 5, 3], [5, 3, 4, 4, 2, 3, 2])
29
>>> main(1, [2], [3])
5
"""


def main(n: int, a_1: list, a_2: list):
    ans = 0

    for i in range(n):
        res = sum(a_1[: i + 1]) + sum(a_2[i:])

        if ans < res:
            ans = res

    print(ans)


if __name__ == "__main__":
    n = int(input())
    a_1 = list(map(int, input().split()))
    a_2 = list(map(int, input().split()))

    main(n, a_1, a_2)

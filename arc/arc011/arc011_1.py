"""A - 鉛筆リサイクルの新技術
https://atcoder.jp/contests/arc011/tasks/arc011_1

m n N

>>> main(2, 1, 8)
15
>>> main(7, 4, 30)
62
>>> main(100, 99, 1000)
90199
"""


def main(m: int, n: int, N: int):
    ans = N
    salled = N
    collected = N
    remain = 0

    while collected >= m:
        salled = (collected // m) * n
        remain = collected % m
        ans += salled
        collected = salled + remain

    print(ans)


if __name__ == "__main__":
    m, n, N = map(int, input().split())

    main(m, n, N)

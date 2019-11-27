"""B - 心配性な富豪、ファミリーレストランに行く。
https://atcoder.jp/contests/abc009/tasks/abc009_2

N
A1
A2
:
AN

>>> main(4, [100, 200, 300, 300])
200
>>> main(5, [50, 370, 819, 433, 120])
433
>>> main(6, [100, 100, 100, 200, 200, 200])
100
"""


def main(n: int, a: list):
    a = sorted(set(a))
    print(a[-2])


if __name__ == "__main__":
    n = int(input())
    a = [int(input()) for _ in range(n)]

    main(n, a)

"""A - たこ焼き買えるかな？
https://atcoder.jp/contests/arc008/tasks/arc008_1
N

>>> main(2)
30
>>> main(5)
75
>>> main(7)
100
"""


def main(n: int):
    print(min(n * 15, ((n // 10) + 1) * 100))


if __name__ == "__main__":
    n = int(input())

    main(n)

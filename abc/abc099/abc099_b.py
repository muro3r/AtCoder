"""B - Stone Monument
https://atcoder.jp/contests/abc099/tasks/abc099_b
a b

>>> main(8, 13)
2
>>> main(54, 65)
1
"""


def main(a: int, b: int):
    print(int((b - a) * (b - a + 1) / 2 - b))


if __name__ == "__main__":
    a, b = map(int, input().split())

    main(a, b)

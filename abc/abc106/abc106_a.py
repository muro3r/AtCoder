"""A - Garden
https://atcoder.jp/contests/abc106/tasks/abc106_a

>>> main(2, 2)
1
>>> main(5, 7)
24"""


def main(a, b):
    print((a - 1) * (b - 1))


if __name__ == "__main__":
    a, b = map(int, input().split(" "))
    main(a, b)

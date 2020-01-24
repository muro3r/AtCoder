"""A - Remaining Time
https://atcoder.jp/contests/abc057/tasks/abc057_a

>>> main(9, 12)
21
>>> main(19, 0)
19
>>> main(23, 2)
1

"""


def main(a, b):
    print((a + b) % 24)


if __name__ == "__main__":
    a, b = map(int, input().split(" "))

    main(a, b)

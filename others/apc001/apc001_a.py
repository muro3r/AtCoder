"""A - Two Integers
https://atcoder.jp/contests/apc001/tasks/apc001_a

>>> main(8, 6)
8
>>> main(3, 3)
-1

"""


def main(x, y):
    if x % y == 0:
        print(-1)
    else:
        print(x)


if __name__ == "__main__":
    x, y = map(int, input().split(" "))

    main(x, y)

"""A - ABC/ARC
https://atcoder.jp/contests/abc053/tasks/abc053_a
x

>>> main(1000)
ABC
>>> main(2000)
ARC

"""


def main(x):
    if x < 1200:
        print("ABC")
    else:
        print("ARC")


if __name__ == "__main__":
    x = int(input())

    main(x)

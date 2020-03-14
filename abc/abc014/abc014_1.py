"""A - けんしょう先生のお菓子配り
https://atcoder.jp/contests/abc014/tasks/abc014_1
a
b

>>> main(7, 3)
2
>>> main(5, 5)
0
>>> main(1, 100)
99
>>> main(25, 12)
11
"""


def main(a: int, b: int):
    if a % b == 0:
        print(0)
    else:
        print(b - a % b)


if __name__ == "__main__":
    a, b = int(input()), int(input())

    main(a, b)

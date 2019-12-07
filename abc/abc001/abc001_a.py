"""A - 積雪深差
https://atcoder.jp/contests/abc001/tasks/abc001_1

>>> main(15, 10)
5
>>> main(0, 0)
0
>>> main(5, 20)
-15
"""


def main(H1, H2):
    print(H1 - H2)


if __name__ == "__main__":
    H1 = int(input())
    H2 = int(input())

    main(H1, H2)

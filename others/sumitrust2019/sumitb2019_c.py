"""C - 100 to 105
https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_c
X

>>> main(615)
1
>>> main(217)
0
"""


def main(x: int):
    c = x // 100

    if c * 100 <= x <= c * 105:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    x = int(input())

    main(x)

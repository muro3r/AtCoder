"""C - Rectangle Cutting
https://atcoder.jp/contests/abc130/tasks/abc130_c
W H x y

>>> main(2, 3, 1, 2)
3.000000 0
>>> main(2, 2, 1, 1)
2.000000 1
"""


def main(W: int, H: int, x: int, y: int):
    area = W * H
    count = 0

    if x * 2 == W and y * 2 == H:
        count = 1

    print("{:.6f}".format(area / 2), count)


if __name__ == "__main__":
    W, H, x, y = map(int, input().split())

    main(W, H, x, y)

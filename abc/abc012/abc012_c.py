"""C - 九九足し算
https://atcoder.jp/contests/abc012/tasks/abc012_3

N

>>> main(2013)
2 x 6
3 x 4
4 x 3
6 x 2

>>> main(2024)
1 x 1
"""


def main(n: int) -> None:
    v = 2025 - n

    for j in range(1, 10):
        for i in range(1, 10):
            if (j * i) == v:
                print("{} x {}".format(j, i))


if __name__ == "__main__":
    n = int(input())

    main(n)

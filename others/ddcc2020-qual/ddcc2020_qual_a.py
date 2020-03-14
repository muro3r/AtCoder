"""A - DDCC Finals
https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_a
X Y

>>> main(1, 1)
1000000
>>> main(3, 101)
100000
>>> main(4, 4)
0
"""


def main(x: int, y: int):
    award = 0

    if x == y == 1:
        award += 400000

    for i in [x, y]:
        if i == 1:
            award += 300000
        elif i == 2:
            award += 200000
        elif i == 3:
            award += 100000

    print(award)


if __name__ == "__main__":
    x, y = map(int, input().split())

    main(x, y)

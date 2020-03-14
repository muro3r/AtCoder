"""A - 長方形
https://atcoder.jp/contests/abc027/tasks/abc027_a

l_1 l_2 l_3

>>> main(1, 1, 2)
2
>>> main(4, 3, 4)
3
>>> main(5, 5, 5)
5
"""

from collections import Counter


def main(l_1, l_2, l_3):
    c = Counter([l_1, l_2, l_3])

    print(c.most_common()[-1][0])


if __name__ == "__main__":
    l_1, l_2, l_3 = map(int, input().split())

    main(l_1, l_2, l_3)

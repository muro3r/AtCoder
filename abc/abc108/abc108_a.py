"""A - Pair
https://atcoder.jp/contests/abc108/tasks/abc108_a

>>> main(3)
2
>>> main(6)
9
>>> main(11)
30
>>> main(50)
625"""

from itertools import permutations


def main(k):
    count = 0

    for p in permutations(range(1, k + 1), 2):
        if p[0] % 2 == 0 and p[1] % 2 != 0:
            count += 1

    print(count)


if __name__ == "__main__":
    k = int(input())
    main(k)

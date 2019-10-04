'''A - Airplane
https://atcoder.jp/contests/abc129/tasks/abc129_a

>>> main(1, 3, 4)
4
>>> main(3, 2, 3)
5

in5.txt
>>> main(99, 62, 92)
154'''

from itertools import permutations


def main(p, q, r):
    _max = 999

    for p in permutations([p, q, r], 2):
        if _max > sum(p):
            _max = sum(p)

    print(_max)


if __name__ == '__main__':
    p, q, r = map(int, input().split(' '))
    main(p, q, r)

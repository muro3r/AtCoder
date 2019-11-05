
'''A - Five Antennas
https://atcoder.jp/contests/abc123/tasks/abc123_a

>>> main([1, 2, 4, 8, 9], 15)
Yay!
>>> main([15, 18, 26, 35, 36], 18)
:(

in1.txt
>>> main([0, 7, 9, 52, 123], 123)
Yay!'''

from itertools import permutations


def main(_input, k):
    for p in permutations(_input, 2):
        if p[0] - p[1] > k:
            print(':(')
            return

    print('Yay!')


if __name__ == "__main__":
    _input = []

    for _ in range(5):
        _input.append(int(input()))

    k = int(input())

    main(_input, k)

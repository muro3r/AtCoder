'''A - Transfer
https://atcoder.jp/contests/abc136/tasks/abc136_a

>>> main(6, 4, 3)
1
>>> main(8, 3, 9)
4
>>> main(12, 3, 7)
0
'''


def main(a, b, c):
    print(max(c - (a - b), 0))


if __name__ == '__main__':
    a, b, c = map(int, input().split(' '))
    main(a, b, c)


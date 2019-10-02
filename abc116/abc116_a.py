'''
A - Right Triangle
https://atcoder.jp/contests/abc116/tasks/abc116_a

>>> main(3, 4, 5)
6
>>> main(5, 12, 13)
30
>>> main(45, 28, 53)
630
'''


def main(ab, bc, ca):
    print((ab * bc) // 2)


if __name__ == '__main__':
    ab, bc, ca = map(int, input().split(' '))

    main(ab, bc, ca)


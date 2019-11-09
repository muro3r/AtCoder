'''A - Round Up the Mean
https://atcoder.jp/contests/abc082/tasks/abc082_a
a b

>>> main(1, 3)
2
>>> main(7, 4)
6
>>> main(5, 5)
5

'''


def main(a: int, b: int):
    print((a + b + 1) // 2)


if __name__ == '__main__':
    a, b = map(int, input().split(' '))

    main(a, b)

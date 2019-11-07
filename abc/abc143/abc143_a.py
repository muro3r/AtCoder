'''A - Curtain
https://atcoder.jp/contests/abc143/tasks/abc143_a

>>> main(12, 4)
4
>>> main(20, 15)
0
>>> main(20, 30)
0

'''


def main(a, b):
    print(max(0, a - b * 2))


if __name__ == "__main__":
    a, b = map(int, input().split(' '))
    main(a, b)

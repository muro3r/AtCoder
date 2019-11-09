'''A - ringring
https://atcoder.jp/contests/abc066/tasks/abc066_a
a b c
>>> main(700, 600, 780)
1300
>>> main(10000, 10000, 10000)
20000

'''


def main(a, b, c):
    ls = [a, b]

    ls.sort()
    print(ls[0] + ls[1])
    pass


if __name__ == '__main__':
    a, b, c = map(int, input().split(' '))

    main(a, b, c)

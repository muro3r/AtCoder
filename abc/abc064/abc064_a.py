'''A - RGB Cards
https://atcoder.jp/contests/abc064/tasks/abc064_a

r g b
>>> main(4, 3, 2)
YES
>>> main(2, 3, 4)
NO

'''


def main(r, g, b):
    i = r * 100 + g * 10 + b

    if i % 4 == 0:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    r, g, b = map(int, input().split(' '))

    main(r, g, b)

'''A - タブの開きすぎ
https://atcoder.jp/contests/arc047/tasks/arc047_a

>>> main(6, 2, '+++-++')
2

>>> main(20, 20, '++-+-+++--+++++-++++')
0

'''


def main(n, l, s):
    count = 0
    clash = 0
    for s in s:
        if s == '+':
            count += 1
        elif count == 1 and s == '-':
            pass
        else:
            count -= 1

        if count > l:
            count = 1
            clash += 1

    print(clash)


if __name__ == '__main__':
    n, l = map(int, input().split(' '))
    s = input()

    main(n, l, s)


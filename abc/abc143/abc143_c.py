'''C - Slimes
https://atcoder.jp/contests/abc143/tasks/abc143_c

>>> main(10, 'aabbbbaaca')
5
>>> main(5, 'aaaaa')
1
>>> main(20, 'xxzaffeeeeddfkkkkllq')
10

'''


def main(n, s):
    i = 0
    tmp = ''

    for s in s:
        if s != tmp:
            i += 1

        tmp = s

    print(i)


if __name__ == "__main__":
    n = int(input())
    s = input()

    main(n, s)

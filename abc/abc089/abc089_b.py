'''B - Hina Arare
https://atcoder.jp/contests/abc089/tasks/abc089_b

>>> main(6, ['G', 'W', 'Y', 'P', 'Y', 'W'])
Four
>>> main(9, ['G', 'W', 'W', 'G', 'P', 'W', 'P', 'G', 'G'])
Three
>>> main(8, ['P', 'Y', 'W', 'G', 'Y', 'W', 'Y', 'Y'])
Four

'''


def main(n, s):
    a = set(s)

    if len(a) == 3:
        print('Three')
    elif len(a) == 4:
        print('Four')


if __name__ == "__main__":
    n = int(input())
    s = list(input().split())

    main(n, s)

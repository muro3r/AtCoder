'''B - Ordinary Number
https://atcoder.jp/contests/abc132/tasks/abc132_b

>>> main(5, [1, 3, 5, 4, 2])
2
>>> main(9, [9, 6, 3, 2, 5, 8, 7, 4, 1])
5

'''


def main(n, p):
    res = 0

    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1]:
            res += 1
        elif p[i - 1] > p[i] > p[i + 1]:
            res += 1

    print(res)


if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split(' ')))

    main(n, p)


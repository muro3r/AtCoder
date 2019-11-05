'''B - Balance
https://atcoder.jp/contests/abc129/tasks/abc129_b

>>> main(3, [1, 2, 3])
0

>>> main(4, [1, 3, 1, 1])
2

>>> main(8, [27, 23, 76, 2, 3, 5, 62, 52])
2
'''


def main(n, w):
    res = max(w)
    for i in range(1, n):
        s_1, s_2 = w[:i], w[i:]

        _min = abs(sum(s_1) - sum(s_2))
        if _min < res:
            res = _min

    print(res)


if __name__ == '__main__':
    n = int(input())
    w = list(map(int, input().split(' ')))

    main(n, w)


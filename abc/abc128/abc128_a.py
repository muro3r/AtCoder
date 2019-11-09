'''A - Apple Pie
https://atcoder.jp/contests/abc128/tasks/abc128_a
A P

>>> main(1, 3)
3
>>> main(0, 1)
0
>>> main(32, 21)
58

'''


def main(A, P):
    amount = A * 3 + P

    print(amount // 2)


if __name__ == "__main__":
    A, P = map(int, input().split(' '))

    main(A, P)

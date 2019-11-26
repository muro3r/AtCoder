"""C - Buy an Integer
https://atcoder.jp/contests/abc146/tasks/abc146_c
A B X

>>> main(10, 7, 100)
9
>>> main(2, 1, 100000000000)
1000000000
>>> main(1000000000, 1000000000, 100)
0
>>> main(1234, 56789, 314159265)
254309
"""


def main(a: int, b: int, x: int):
    if a * 10 ** 9 + b * 10 <= x:
        print(10 ** 9)
        return

    low = 0
    high = 10 ** 9

    while high - low > 1:
        n = (low + high) // 2
        i = (a * n) + (b * len(str(n)))

        if i < x:
            low = n
        elif x < i:
            high = n

    print(low)


if __name__ == "__main__":
    a, b, x = map(int(input().split()))

    main(a, b, x)

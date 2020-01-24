"""C - いっしょ / Be Together
https://atcoder.jp/contests/arc059/tasks/arc059_a

>>> main(2, [4, 8])
8
>>> main(3, [1, 1, 3])
3
>>> main(3, [4, 2, 5])
5
>>> main(4, [-100, -100, -100, -100])
0

"""


def main(n, a):
    base = (max(a) + min(a)) / 2
    ans = 0

    for n in a:
        ans += (n - base) ** 2

    print(round(ans))


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    main(n, a)

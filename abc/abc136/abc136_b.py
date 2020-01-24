"""B - Uneven Numbers
https://atcoder.jp/contests/abc136/tasks/abc136_b

>>> main(11)
9
>>> main(136)
46
>>> main(100000)
90909
"""


def main(n):
    count = 0

    for i in range(1, n + 1):
        if len(str(i)) % 2 == 1:
            count += 1

    print(count)


if __name__ == "__main__":
    n = int(input())

    main(n)

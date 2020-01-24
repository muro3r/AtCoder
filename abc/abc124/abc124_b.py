"""B - Great Ocean View
https://atcoder.jp/contests/abc124/tasks/abc124_b

>>> main(4, [6, 5, 6, 8])
3
>>> main(5, [4, 5, 3, 5, 4])
3
>>> main(5, [9, 5, 6, 8, 4])
1
"""


def main(n, h):
    base = 0
    count = 0

    for _h in h:
        if _h >= base:
            base = _h
            count += 1

    print(count)


if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().split(" ")))

    main(n, h)

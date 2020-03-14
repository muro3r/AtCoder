"""C - Build Stairs
https://atcoder.jp/contests/abc136/tasks/abc136_c
N
H_1 H_2 ... H_N
>>> main(5, [1, 2, 1, 1, 3])
Yes
>>> main(4, [1, 3, 2, 1])
No
>>> main(5, [1, 2, 3, 4, 5])
Yes
>>> main(1, [1000000000])
Yes
"""


def main(n: int, h: list):
    _max = h[0]

    for h in h:
        if _max == h:
            continue

        if (h - _max) == 1:
            _max = h
        elif (h - _max) >= 2:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().split()))

    main(n, h)

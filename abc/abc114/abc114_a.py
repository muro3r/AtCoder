"""A - 753
https://atcoder.jp/contests/abc114/tasks/abc114_a

>>> main(5)
YES

>>> main(6)
NO
"""


def main(x):
    if x in [7, 5, 3]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main(int(input()))

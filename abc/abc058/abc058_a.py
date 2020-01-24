"""A - ι⊥l
https://atcoder.jp/contests/abc058/tasks/abc058_a
>>> main(2, 4, 6)
YES

>>> main(2, 5, 6)
NO

>>> main(3, 2, 1)
YES

"""


def main(a, b, c):
    if b - a == c - b:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    a, b, c = map(int, input().split(" "))

    main(a, b, c)

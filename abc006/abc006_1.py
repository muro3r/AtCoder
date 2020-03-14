"""A - 世界のFizzBuzz
https://atcoder.jp/contests/abc006/tasks/abc006_1

N

>>> main(2)
NO
>>> main(9)
YES
>>> main(3)
YES
"""


def main(n: int):
    if n % 3 == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()

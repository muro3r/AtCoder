"""A - AtCoder Beginner Contest 999
https://atcoder.jp/contests/abc111/tasks/abc111_a

>>> main(119)
991
>>> main(999)
111
"""


def main(n):
    res = ""
    for _n in str(n):
        if _n == "1":
            res += "9"
        else:
            res += "1"

    print(res)


if __name__ == "__main__":
    n = int(input())

    main(n)

"""A - F
https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_a
a b

>>> main(4, 11)
+
>>> main(3, 5)
*
>>> main(1, 1)
x
"""


def main(a, b):
    if a + b == 15:
        print("+")
    elif a * b == 15:
        print("*")
    else:
        print("x")


if __name__ == "__main__":
    a, b = map(int, input().split(" "))

    main(a, b)

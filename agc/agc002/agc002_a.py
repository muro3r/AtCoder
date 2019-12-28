"""A - Range Product
https://atcoder.jp/contests/agc002/tasks/agc002_a
a b

>>> main(1, 3)
Positive
>>> main(-3, -1)
Negative
>>> main(-1, 1)
Zero
"""


def main(a, b):
    if 0 < a and 0 < b:
        print("Positive")
        return

    if a <= b < 0:
        print("Negative")
        return
    elif (a - b) % 3 == 0:
        print("Positive")
        return

    print("Zero")

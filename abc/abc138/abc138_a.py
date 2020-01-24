"""A - Red or Not
https://atcoder.jp/contests/abc138/tasks/abc138_a

>>> main(3200, 'pink')
pink
>>> main(3199, 'pink')
red
>>> main(4049, 'red')
red
"""


def main(a, s):
    if a >= 3200:
        print(s)
    else:
        print("red")


if __name__ == "__main__":
    a, s = int(input()), input()
    main(a, s)

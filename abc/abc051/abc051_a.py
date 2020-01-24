"""A - Haiku
https://atcoder.jp/contests/abc051/tasks/abc051_a

>>> main('happy,newyear,enjoy')
happy newyear enjoy
>>> main('haiku,atcoder,tasks')
haiku atcoder tasks
>>> main('abcde,fghihgf,edcba')
abcde fghihgf edcba
"""


def main(s):
    print(s.replace(",", " "))


if __name__ == "__main__":
    s = input()

    main(s)

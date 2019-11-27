"""B - Varied
https://atcoder.jp/contests/abc063/tasks/abc063_b
S

>>> main('uncopyrightable')
yes
>>> main('different')
no
>>> main('no')
yes
"""


def main(s: str):
    if len(set(s)) == len(s):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    s = input()

    main(s)

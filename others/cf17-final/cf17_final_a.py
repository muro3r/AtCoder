"""A - AKIBA
https://atcoder.jp/contests/cf17-final/tasks/cf17_final_a
S

>>> main('KIHBR')
YES
>>> main('AKIBAHARA')
NO
>>> main('AAKIAHBAARA')
NO
"""

import re


def main(s: str):
    if re.fullmatch(r"A?KIHA?BA?RA?", s):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    s = input()

    main(s)

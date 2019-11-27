"""B - ATCoder
https://atcoder.jp/contests/abc122/tasks/abc122_b
S

>>> main('ATCODER')
3
>>> main('HATAGAYA')
5
>>> main('SHINJUKU')
0
"""

import re


def main(s: str):
    length = [len(_s) for _s in re.findall(r"[ACGT]+", s)]

    if length == []:
        print(0)
        return

    print(max(length))


if __name__ == "__main__":
    s = input()

    main(s)

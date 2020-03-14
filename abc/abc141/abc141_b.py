"""B - Tap Dance
https://atcoder.jp/contests/abc141/tasks/abc141_b
S

>>> main('RUDLUDR')
Yes
>>> main('DULL')
No
>>> main('UUUUUUUUUUUUUUU')
Yes
>>> main('ULURU')
No
>>> main('RDULULDURURLRDULRLR')
Yes
"""

import re


def main(s: str):
    if re.match(r"^([^L][^R])*[^L]$", s):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    s = input()

    main(s)

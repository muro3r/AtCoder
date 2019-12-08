"""A - スーパーICT高校生
https://atcoder.jp/contests/arc022/tasks/arc022_1
S

>>> main('InformationAndCommunicationTechnology')
YES
>>> main('InformationTechnology')
NO
>>> main('SinCosTan')
YES
>>> main('Ticket')
YES
>>> main('InternetTrouble')
NO
"""

import re


def main(s: str):
    if re.match(".*[iI].*[cC].*[tT].*", s):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    s = input()

    main(s)

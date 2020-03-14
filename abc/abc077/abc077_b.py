"""B - Around Square
https://atcoder.jp/contests/abc077/tasks/abc077_b
N

>>> main(10)
9
>>> main(81)
81
>>> main(271828182)
271821169
"""

import math


def main(n: int):
    for i in range(n, 0, -1):
        if math.sqrt(i).is_integer():
            print(i)
            return


if __name__ == "__main__":
    n = int(input())

    main(n)

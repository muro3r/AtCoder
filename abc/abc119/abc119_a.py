'''A - Still TBD
https://atcoder.jp/contests/abc119/tasks/abc119_a

>>> main("2019/04/30")
Heisei
>>> main("2019/11/01")
TBD'''

from datetime import datetime


def main(s):
    base_data = datetime(2019, 4, 30)
    year, month, day = map(int, s.split('/'))

    if datetime(year, month, day) <= base_data:
        print('Heisei')
    else:
        print('TBD')


if __name__ == "__main__":
    s = input()
    main(s)

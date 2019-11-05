'''
>>> main(3661)
01:01:01

>>> main(86399)
23:59:59
'''

from datetime import datetime, timedelta


def main(n):
    s = n % 60
    m = (n // 60) % 60
    h = n // (60**2)

    print('{:02d}:{:02d}:{:02d}'.format(h, m, s))


if __name__ == '__main__':
    n = int(input())

    main(n)


'''

>>> main(2525)
Yes
>>> main(1881)
No

'''


def main(s):
    s = '{:04d}'.format(s)

    if s[0] == s[2] and s[1] == s[3]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    s = int(input())

    main(s)

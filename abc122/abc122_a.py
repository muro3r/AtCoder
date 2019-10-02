'''A - Double Helix
https://atcoder.jp/contests/abc122/tasks/abc122_a

>>> main('A')
T
>>> main('G')
C
'''


def main(b):
    if b == 'A':
        print('T')
    elif b =='T':
        print('A')
    elif b == 'G':
        print('C')
    elif b == 'C':
        print('G')


if __name__ == '__main__':
    main(input())


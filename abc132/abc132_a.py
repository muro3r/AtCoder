'''A - Fifty-Fifty
https://atcoder.jp/contests/abc132/tasks/abc132_a

>>> main('ASSA')
Yes
>>> main('STOP')
No
>>> main('FFEE')
Yes

06.txt
>>> main('YSKY')
No

07.txt
>>> main('JJKP')
No

'''


def main(s):
    for _s in s:
        if s.count(_s) != 2:
            print('No')
            return

    print('Yes')


if __name__ == "__main__":
    main(input())

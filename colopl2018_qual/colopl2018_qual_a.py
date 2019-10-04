'''A - すぬけそだて――登録――
https://atcoder.jp/contests/colopl2018-qual/tasks/colopl2018_qual_a

>>> main(4, 8, 'colopl')
YES
>>> main(2, 7, 'kitayuta')
NO
>>> main(7, 8, 'kyuri')
NO
'''


def main(a, b, s):
    if a <= len(s) <= b:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    a, b = map(int, input().split(' '))
    s = input()
    main(a, b, s)

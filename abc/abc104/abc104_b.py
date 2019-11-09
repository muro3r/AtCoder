'''
B - AcCepted
https://atcoder.jp/contests/abc104/tasks/abc104_b
S

>>> main('AtCoder')
AC
>>> main('ACoder')
WA
>>> main('AcycliC')
WA
>>> main('AtCoCo')
WA
>>> main('Atcoder')
WA

'''

import string


def main(S):
    if not S[0] == 'A' or S[1] == 'C':
        print('WA')
        return
    if S.endswith('C'):
        print('WA')
        return

    count_upper = 0
    for upper in string.ascii_uppercase:
        count_upper += S.count(upper)

    if count_upper != 2:
        print('WA')
        return

    count_C = 0

    for s in S[2:]:
        if s == 'C':
            if count_C == 1:
                print('WA')
                return
            else:
                count_C += 1
                continue
        elif not s.islower():
            print('WA')
            return

    if count_C == 0:
        print('WA')
        return

    print('AC')
    return


if __name__ == '__main__':
    S = input()

    print(main(S))

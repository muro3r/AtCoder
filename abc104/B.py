import string


def main(S):
    if not S[0] == 'A' or S[1] == 'C':
        return 'WA'
    if S.endswith('C'):
        return 'WA'

    count_upper = 0
    for upper in string.ascii_uppercase:
        count_upper += S.count(upper)

    if count_upper != 2:
        return 'WA'

    count_C = 0

    for s in S[2:]:
        if s == 'C':
            if count_C == 1:
                return 'WA'
            else:
                count_C += 1
                continue
        elif not s.islower():
            return 'WA'

    if count_C == 0:
        return 'WA'

    return 'AC'


if __name__ == '__main__':
    S = input()
    print(main(S))

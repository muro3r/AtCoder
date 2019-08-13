def main(S):
    if not S[0] == 'A':
        return 'WA'
    if not S[2] == 'C':
        return 'WA'
    if S.endswith('C'):
        return 'WA'

    count_c = 0
    count_c += S.count('C')
    count_c += S.count('c')

    if not count_c == 1:
        return 'WA'

    for s in S[1:]:
        if s == 'C':
            continue
        elif not s.islower():
            return 'WA'

    return 'AC'


if __name__ == '__main__':
    S = input()
    print(main(S))


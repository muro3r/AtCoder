def resolve():
    N, L = map(int, input().split(' '))

    S = []

    for x in range(0, N):
        S.append(input())

    S.sort()

    [print(S, end='') for S in S]


if __name__ == '__main__':
    resolve()

def main(T, A, B, C, D):
    if A + C <= T:
        return B + D

    if A + C > T:
        if C <= T:
            return D
        elif A <= T:
            return B

    return 0


if __name__ == '__main__':
    T, A, B, C, D = map(int, input().split(' '))
    print(main(T, A, B, C, D))


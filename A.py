def main(A: int, B: int, C: int, D: int):
    train, bus = 0, 0
    if A <= B:
        train += A
    else:
        train += B

    if C <= D:
        bus += C
    else:
        bus += D

    return train + bus


if __name__ == '__main__':
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    print(main(A, B, C, D))

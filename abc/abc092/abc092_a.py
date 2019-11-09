'''A - Traveling Budget
https://atcoder.jp/contests/abc092/tasks/abc092_a

>>> main(600, 300, 220, 420)
520
>>> main(555, 555, 400, 200)
755
>>> main(549, 817, 715, 603)
1152

'''


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

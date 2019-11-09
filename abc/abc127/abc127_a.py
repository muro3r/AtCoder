'''A - Ferris Wheel
https://atcoder.jp/contests/abc127/tasks/abc127_a
A B

>>> main(30, 100)
100
>>> main(12, 100)
50
>>> main(0, 100)
0

'''


def main(A, B):
    if A >= 13:
        print(B)
    elif 6 <= A and A <= 12:
        print(B // 2)
    elif A <= 5:
        print(0)


if __name__ == "__main__":
    A, B = map(int, input().split(' '))

    main(A, B)

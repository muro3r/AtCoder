'''A - Between Two Integers
https://atcoder.jp/contests/abc061/tasks/abc061_a
A B C
>>> main(1, 3, 2)
Yes
>>> main(6, 5, 4)
No
>>> main(2, 2, 2)
Yes

'''


def main(A, B, C):
    if A <= C and C <= B:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    A, B, C = map(int, input().split(' '))

    main(A, B, C)

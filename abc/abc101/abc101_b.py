'''B - Digit Sums
https://atcoder.jp/contests/abc101/tasks/abc101_b
N

>>> main(12)
Yes
>>> main(101)
No
>>> main(999999999)
Yes

'''


def main(N):
    i = 0

    for s in str(N):
        i += int(s)

    if N % i == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    N = int(input())

    main(N)

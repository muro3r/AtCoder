'''
C - Go to School
https://atcoder.jp/contests/abc142/tasks/abc142_c

>>> main(3, [2, 3, 1])
3 1 2

>>> main(5, [1, 2, 3, 4, 5])
1 2 3 4 5

>>> main(8, [8, 2, 7, 3, 4, 5, 6, 1])
8 2 4 5 6 7 3 1
'''


def main(n, a):
    ls = [0 for _ in range(n)]

    count = 1
    for i in a:
        ls[i - 1] = count
        count += 1

    print(' '.join(map(str, ls)))


if __name__ == '__main__':
    n = int(input())
    a = map(int, input().split(' '))

    main(n, a)

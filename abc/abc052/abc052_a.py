'''A - Two Rectangles
https://atcoder.jp/contests/abc052/tasks/abc052_a

>>> main(3, 5, 2, 7)
15

>>> main(100, 600, 200, 300)
60000

'''


def main(a, b, c, d):
    sum_a = a * b
    sum_b = c * d

    if sum_a > sum_b:
        print(sum_a)
    else:
        print(sum_b)


if __name__ == "__main__":
    a, b, c, d = map(int, input().split(' '))

    main(a, b, c, d)

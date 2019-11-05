'''A - 高橋君と青木君の好きな数
https://atcoder.jp/contests/abc032/tasks/abc032_a

>>> main(2, 3, 8)
12
>>> main(2, 2, 2)
2
>>> main(12, 8, 25)
48

>>> main(1, 100, 100)
100
'''


def main(a, b, n):
    while True:
        if n % a == 0 and n % b == 0:
            print(n)
            break

        n += 1


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    n = int(input())

    main(a, b, n)

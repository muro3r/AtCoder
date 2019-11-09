'''A - Restaurant
https://atcoder.jp/contests/abc055/tasks/abc055_a

>>> main(20)
15800
>>> main(60)
47200

'''


def main(n):
    print(n * 800 - (n // 15) * 200)


if __name__ == "__main__":
    n = int(input())

    main(n)

'''A - Celsius と Fahrenheit
https://atcoder.jp/contests/arc015/tasks/arc015_1

>>> main(10)
50
>>> main(33)
91.4
>>> main(-100)
-148

'''


def main(n):
    f = (9 / 5 * n) + 32
    if f.is_integer():
        print(int(f))
    else:
        print(f)


if __name__ == '__main__':
    n = int(input())

    main(n)


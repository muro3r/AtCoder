'''B - 1 21
https://atcoder.jp/contests/abc086/tasks/abc086_b
a b

>>> main(1, 21)
Yes
>>> main(100, 100)
No
>>> main(12, 10)
No

'''
import math


def main(a: str, b: str):
    num = int(str(a) + str(b))

    if math.sqrt(num) % 1 == 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    a, b = input().split()

    main(a, b)

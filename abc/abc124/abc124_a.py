'''A - Buttons
https://atcoder.jp/contests/abc124/tasks/abc124_a

>>> main(5,3)
9
>>> main(3,4)
7
>>> main(6,6)
12'''


def main(a, b):
    _max = max(a, b)
    _min = min(a, b)
    amount = 0

    amount += _max
    _max -= 1

    if _max > _min:
        amount += _max
    else:
        amount += _min

    print(amount)


if __name__ == "__main__":
    a, b = map(int, input().split(' '))

    main(a, b)

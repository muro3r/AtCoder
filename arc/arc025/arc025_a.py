'''
>>> main([4, 2, 0, 5, 6, 2, 5], [6, 1, 4, 3, 6, 4, 6])
33

'''


def main(d, j):
    amount = 0

    for di, ji in zip(d, j):
        amount += max(di, ji)

    print(amount)


if __name__ == '__main__':
    d = map(int, input().split())
    j = map(int, input().split())

    main(d, j)

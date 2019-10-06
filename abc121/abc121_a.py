'''A - White Cells
https://atcoder.jp/contests/abc121/tasks/abc121_a

>>> main([3, 2], [2, 1])
1
>>> main([5, 5], [2, 3])
6
>>> main([2, 4], [2, 4])
0'''


def main(amount, portion):
    print((amount[0] - portion[0]) * (amount[1] - portion[1]))


if __name__ == "__main__":
    amount = list(map(int, input().split(' ')))
    portion = list(map(int, input().split(' ')))

    main(amount, portion)

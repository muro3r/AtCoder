'''A - Probability of Participation
https://atcoder.jp/contests/code-festival-2018-qualb/tasks/code_festival_2018_qualb_a

>>> main(3)
67
>>> main(17)
95
>>> main(57)
99
'''


def main(n):
    print(100 - (100 // n))


if __name__ == '__main__':
    main(int(input()))

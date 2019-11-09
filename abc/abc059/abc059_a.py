'''A - Three-letter acronym
https://atcoder.jp/contests/abc059/tasks/abc059_a

>>> main('atcoder', 'beginner', 'contest')
ABC
>>> main('resident', 'register', 'number')
RRN
>>> main('k', 'nearest', 'neighbor')
KNN
>>> main('async', 'layered', 'coding')
ALC
'''


def main(s_1, s_2, s_3):
    print(''.join([s_1[0], s_2[0], s_3[0]]).upper())


if __name__ == "__main__":
    s_1, s_2, s_3 = input().split()

    main(s_1, s_2, s_3)

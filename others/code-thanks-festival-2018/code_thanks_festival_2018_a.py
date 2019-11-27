"""A - Two Problems
https://atcoder.jp/contests/code-thanks-festival-2018/tasks/code_thanks_festival_2018_a

T A B C D

>>> main(100, 20, 500, 40, 1000)
1500
>>> main(50, 100, 1500, 100, 1500)
0
>>> main(100, 100, 1000, 100, 1000)
1000
"""


def main(T, A, B, C, D):
    if A + C <= T:
        print(B + D)
        return

    if A + C > T:
        if C <= T:
            print(D)
            return
        elif A <= T:
            print(B)
            return

    print(0)
    return


if __name__ == "__main__":
    T, A, B, C, D = map(int, input().split(" "))

    main(T, A, B, C, D)

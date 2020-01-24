"""A - Restricted
https://atcoder.jp/contests/abc063/tasks/abc063_a
A B
>>> main(6, 3)
9
>>> main(6, 4)
error

"""


def main(A, B):
    if A + B < 10:
        print(A + B)
    else:
        print("error")


if __name__ == "__main__":
    A, B = map(int, input().split(" "))

    main(A, B)

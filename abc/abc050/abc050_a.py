'''A - Addition and Subtraction Easy
https://atcoder.jp/contests/abc050/tasks/abc050_a

>>> main('1 + 2')
3

>>> main('5 - 7')
-2
'''


def main(A_op_B):
    print(eval(A_op_B))


if __name__ == "__main__":
    A_op_B = input()

    main(A_op_B)

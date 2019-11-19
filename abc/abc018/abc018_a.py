"""A - 豆まき
https://atcoder.jp/contests/abc018/tasks/abc018_1
A
B
C

>>> main(12, 18, 11)
2
1
3
>>> main(10, 20, 30)
3
2
1

"""


def main(a, b, c):
    comp = [a, b, c]

    for i in comp:
        if i == max(comp):
            print(1)
        elif i == min(comp):
            print(3)
        else:
            print(2)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    main(a, b, c)

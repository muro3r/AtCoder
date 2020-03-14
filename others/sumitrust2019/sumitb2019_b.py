"""B - Tax Rate
https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b
N

>>> main(432)
400
>>> main(1079)
:(
>>> main(1001)
927
"""


def main(n: int):
    for i in range(n):
        if int(i * 1.08) == n:
            print(i)
            return

    print(":(")


if __name__ == "__main__":
    n = int(input())

    main(n)

'''B - Power Socket
https://atcoder.jp/contests/abc139/tasks/abc139_b

>>> main(4, 10)
3
>>> main(8, 9)
2
>>> main(8, 8)
1'''


def main(A, B):
    # A + N*(A-1)
    outlet = 1
    i = 0

    while outlet < B:
        outlet += A-1
        i += 1

    print(i)


if __name__ == "__main__":
    A, B = map(int, input().split(' '))
    print(main(A, B))

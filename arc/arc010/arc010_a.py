"""A - 名刺交換
https://atcoder.jp/contests/arc010/tasks/arc010_1
>>> main(100, 3, 0, 100, [10, 20, 30])
complete
>>> main(100, 4, 0, 100, [10, 20, 30, 40])
complete
>>> main(100, 4, 0, 100, [50, 40, 30, 20])
3
>>> main(100, 4, 10, 100, [50, 40, 30, 20])
complete
>>> main(5, 3, 20, 10, [15, 5, 20])
3

"""


def main(n, m, a, b, c):
    remain = n

    for i, day in enumerate(c):
        if remain <= a:
            remain += b

        if remain < day:
            print(i + 1)
            return

        remain -= day

    print("complete")


if __name__ == "__main__":
    n, m, a, b = map(int, input().split())
    c = [int(input()) for _ in range(m)]

    main(n, m, a, b, c)

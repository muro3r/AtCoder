"""B - 運動管理
https://atcoder.jp/contests/abc031/tasks/abc031_b

>>> main(300, 400, 3, [240, 350, 480])
60
0
-1
>>> main(50, 80, 5, [10000, 50, 81, 80, 0])
-1
0
-1
0
50

"""


def main(l: int, h: int, a: int, n: list):
    for i in n:
        if i > h:
            print(-1)
        elif l <= i <= h:
            print(0)
        elif i < l:
            print(l - i)


if __name__ == "__main__":
    l, h = map(int, input().split())
    a = int(input())
    n = [int(input()) for _ in range(a)]

    main(l, h, a, n)

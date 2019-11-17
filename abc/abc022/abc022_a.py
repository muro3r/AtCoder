"""A - Best Body
https://atcoder.jp/contests/abc022/tasks/abc022_a

N S T
W
A_2
A_3
:
A_N

>>> main(5, 60, 70, 50, [10, 10, 10, 10])
2

>>> main(5, 50, 100, 120, [-10, -20, -30, 70])
2

"""


def main(n: int, s: int, t: int, w: int, a: list):
    present_weight = w
    ans = 0

    if s <= present_weight <= t:
        ans += 1

    for _a in a:
        present_weight += _a

        if s <= present_weight <= t:
            ans += 1

    print(ans)


if __name__ == "__main__":
    n, s, t = map(int, input().split())
    w = int(input())
    a = [int(input()) for _ in range(n - 1)]

    main(n, s, t, w, a)

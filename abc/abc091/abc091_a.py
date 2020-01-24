"""A - Two Coins
https://atcoder.jp/contests/abc091/tasks/abc091_a

A B C
>>> main(50, 100, 120)
Yes
>>> main(500, 100, 1000)
No
>>> main(19, 123, 143)
No
>>> main(19, 123, 142)
Yes

"""


def main(A: int, B: int, C: int):
    if (A + B) >= C:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    A, B, C = map(int, input().split(" "))

    print(main(A, B, C))

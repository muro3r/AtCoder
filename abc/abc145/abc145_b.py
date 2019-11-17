"""B - Echo
https://atcoder.jp/contests/abc145/tasks/abc145_b
N
S

>>> main(6, 'abcabc')
Yes
>>> main(6, 'abcadc')
No
>>> main(1, 'z')
No
"""


def main(n: int, s: str):
    med = n // 2

    if s[:med] == s[med:]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    n = int(input())
    s = input()

    main(n, s)

"""B - String Rotation
https://atcoder.jp/contests/abc103/tasks/abc103_b
S
T

>>> main('kyoto', 'tokyo')
Yes
>>> main('abc', 'arc')
No
>>> main('aaaaaaaaaaaaaaab', 'aaaaaaaaaaaaaaab')
Yes
"""


def main(s, t):
    for i in range(len(s)):
        if (s[i:] + s[:i]) == t:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    s = input()
    t = input()

    main(s, t)

"""
>>> main(2 , 'ABCXYZ')
CDEZAB
>>> main(0, 'ABCXYZ')
ABCXYZ
>>> main(13, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
NOPQRSTUVWXYZABCDEFGHIJKLM
"""

from string import ascii_uppercase as ascii


def main(n: int, s: str):
    ans = ""
    for _s in s:
        ans += ascii[(ascii.index(_s) + n) % 26]

    print(ans)


if __name__ == "__main__":
    n = int(input())
    s = input()

    main(n, s)

"""B - 文字数カウント
https://atcoder.jp/contests/abc028/tasks/abc028_b

S

>>> main('BEAF')
1 1 0 0 1 1
>>> main('DECADE')
1 0 1 2 2 0
>>> main('ABBCCCDDDDEEEEEFFFFFF')
1 2 3 4 5 6

>>> main('A')
1 0 0 0 0 0
"""

from collections import Counter


def main(s):
    c = Counter(s)
    ans = []
    for a in "ABCDEF":
        ans.append(str(c[a]))

    print(" ".join(ans))


if __name__ == "__main__":
    s = input()

    main(s)

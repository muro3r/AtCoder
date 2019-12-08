"""A - 名前
https://atcoder.jp/contests/arc031/tasks/arc031_1

Name

>>> main("awawa")
YES
>>> main("chokudai")
NO
"""


def main(n: str):
    l = len(n)

    i = 0
    ans = True

    while i < l // 2:
        if n[i] != n[-i - 1]:
            ans = False

        i += 1

    if ans:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    n = input()

    main(n)

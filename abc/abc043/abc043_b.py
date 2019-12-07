"""B - バイナリハックイージー / Unhappy Hacking (ABC Edit)
https://atcoder.jp/contests/abc043/tasks/abc043_b
s

>>> main('01B0')
00
>>> main('0BB1')
1

"""


def main(s):
    s_l = []

    for i in range(0, len(s)):
        if s[i] == "B" and len(s_l) > 0:
            s_l.pop()
        elif s[i] != "B":
            s_l.append(s[i])

    print("".join(s_l))


if __name__ == "__main__":
    s = input()

    main(s)

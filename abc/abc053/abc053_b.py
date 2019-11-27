"""B - A to Z String
https://atcoder.jp/contests/abc053/tasks/abc053_b
s

>>> main("QWERTYASDFZXCV")
5
>>> main("ZABCZ")
4
>>> main("HASFJGHOGAKZZFEGA")
12
"""


def main(s):
    head, tail = 0, 0

    for _s in s:
        if _s == "A":
            break

        head += 1

    for _s in s[::-1]:
        if _s == "Z":
            break

        tail += 1

    print(len(s) - (head + tail))


if __name__ == "__main__":
    s = input()

    main(s)

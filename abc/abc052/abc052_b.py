"""B - Increment Decrement
https://atcoder.jp/contests/abc052/tasks/abc052_b
N
S

>>> main(5, 'IIDID')
2
>>> main(7, 'DDIDDII')
0
"""


def main(n: int, s: str):
    i = 0
    ans = [0]

    for s in s:
        if s == "I":
            i += 1
        else:
            i -= 1

        ans.append(i)

    print(max(ans))


if __name__ == "__main__":
    n = int(input())
    s = input()

    main(n, s)

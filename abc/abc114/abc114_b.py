"""B - 754
https://atcoder.jp/contests/abc114/tasks/abc114_b
S
>>> main('1234567876')
34
>>> main('35753')
0
>>> main('1111111111')
642
"""


def main(s: str):
    ans = 999

    for i in range(len(s) - 2):
        calc = abs(int(s[i : i + 3]) - 753)

        if calc < ans:
            ans = calc

    print(ans)


if __name__ == "__main__":
    s = input()
    main(s)

"""B - 文字列大好きいろはちゃんイージー / Iroha Loves Strings (ABC Edition)
https://abc042.contest.atcoder.jp/tasks/abc042_b
N L S

>>> main(3, 3, ["dxx", "axx", "cxx"])
axxcxxdxx
"""


def main(N: int, L: int, S: list):
    S.sort()

    [print(S, end="") for S in S]


if __name__ == "__main__":
    N, L = map(int, input().split(" "))
    S = [input() for _ in range(N)]

    main(N, L, S)

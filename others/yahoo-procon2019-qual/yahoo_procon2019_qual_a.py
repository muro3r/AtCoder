"""A - Anti-Adjacency
https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_a
N K

>>> main(3, 2)
YES
>>> main(5, 5)
NO
>>> main(31, 10)
YES
>>> main(10, 90)
NO
"""


def main(N, K):
    if K * 2 - 1 <= N:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    N, K = map(int, input().split(" "))

    main(N, K)

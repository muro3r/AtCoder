"""B - Addition and Multiplication
https://atcoder.jp/contests/abc076/tasks/abc076_b
N
K

>>> main(4, 3)
10
>>> main(10, 10)
76

"""


def main(n, k):
    ans = 2

    for _ in range(n - 1):
        if (ans * 2) < ans + k:
            ans *= 2  # A
        else:
            ans += k  # B

    print(ans)


if __name__ == "__main__":
    n = int(input())
    k = int(input())

    main(n, k)

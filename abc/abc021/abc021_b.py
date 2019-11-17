"""B - 嘘つきの高橋くん
https://atcoder.jp/contests/abc021/tasks/abc021_b

N
a b
K
P_1 P_2 … P_K

>>> main(5, 1, 5, 3, [3, 4, 2])
YES

>>> main(7, 1, 3, 4, [2, 4, 2, 7])
NO

>>> main(4, 1, 4, 3, [2, 1, 3])
NO

>>> main(4, 1, 4, 3, [2, 4, 3])
NO

>>> main(20, 1, 4, 12, [2, 3, 5, 7, 8, 9, 10, 11, 12, 15, 13, 14])
YES
"""


def main(n: int, a: int, b: int, k: int, p: list):
    # 途中で到着した
    if a in p or b in p:
        print("NO")
        return

    # 寄り道
    elif len(p) != len(set(p)):
        print("NO")
        return

    print("YES")


if __name__ == "__main__":
    n = int(input())
    a, b = map(int, input().split())
    k = int(input())
    p = list(map(int, input().split()))

    main(n, a, b, k, p)

"""B - Snake Toy
https://atcoder.jp/contests/abc067/tasks/abc067_b
N K
l_1 l_2 l_3 ... l_{N}

>>> main(5, 3, [1, 2, 3, 4, 5])
12
>>> main(15, 14, [50, 26, 27, 21, 41, 7, 42, 35, 7, 5, 5, 36, 39, 1, 45])
386

"""


def main(n: int, k: int, l: list):
    print(sum(sorted(l, reverse=True)[:k]))


if __name__ == "__main__":
    n, k = map(int, input().split())
    l = list(map(int, input().split()))

    main(n, k, l)

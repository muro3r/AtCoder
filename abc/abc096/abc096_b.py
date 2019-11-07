'''B - Maximum Sum
https://atcoder.jp/contests/abc096/tasks/abc096_b

>>> main(5, 3, 11, 1)
30
>>> main(3, 3, 4, 2)
22

'''


def main(a, b, c, k):
    ls = [a, b, c]
    for _ in range(k):
        ls[ls.index(max(ls))] = max(ls) * 2

    print(sum(ls))


if __name__ == "__main__":
    a, b, c = map(int, input().split(' '))
    k = int(input())

    main(a, b, c, k)

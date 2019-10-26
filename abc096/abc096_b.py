'''B - Maximum Sum
https://atcoder.jp/contests/abc096/tasks/abc096_b

>>> main(5, 3, 11, 1)
30
>>> main(3, 3, 4, 2)
22

'''


def main(a, b, c, k):
    l = [a, b, c]
    for _ in range(k):
        l[l.index(max(l))] = max(l)*2

    print(sum(l))


if __name__ == "__main__":
    a, b, c = map(int, input().split(' '))
    k = int(input())

    main(a, b, c, k)

'''B - Time Limit Exceeded
https://atcoder.jp/contests/abc112/tasks/abc112_b

>>> main(3, 70, [[7, 60], [1, 80], [4, 50]])
4
>>> main(4, 3, [[1, 1000], [2, 4], [3, 1000], [4, 500]])
TLE
>>> main(5, 9, [[25, 8], [5, 9], [4, 10], [1000, 1000], [6, 1]])
5

>>> main(1, 375, [[1000, 1]])
1000

'''


def main(n, t, c_t):
    cost = 10000

    for c, _t in c_t:
        if t >= _t:
            if c < cost:
                cost = c

    if cost == 10000:
        print('TLE')
        return

    print(cost)


if __name__ == "__main__":
    n, t = map(int, input().split(' '))
    c_t = list()
    for _ in range(n):
        c_t.append(map(int, input().split(' ')))

    main(n, t, c_t)

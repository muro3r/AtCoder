'''B - Good Distance
https://atcoder.jp/contests/abc133/tasks/abc133_b

>>> main(3, 2, [[1, 2], [5, 5], [-2, 8]])
1
>>> main(3, 4, [[-3, 7, 8, 2], [-12, 1, 10, 2], [-2, 8, 9, 3]])
2
>>> main(5, 1, [[1], [2], [3], [4], [5]])
10

'''

from math import sqrt
from itertools import combinations


def main(n, d, x):
    ans = 0
    for a, b in combinations(x, 2):
        r = 0
        for c, d in zip(a, b):
            r += abs(c - d)**2

        if sqrt(r).is_integer():
            ans += 1

    print(ans)


if __name__ == '__main__':
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]

    main(n, d, x)


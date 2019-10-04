'''A - Biscuit Generator
https://atcoder.jp/contests/abc125/tasks/abc125_a

>>> main(3,5,7)
10
>>> main(3,2,9)
6
>>> main(20,20,19)
0'''


def main(a: int, b: int, t: int):
    print(t//a * b)


if __name__ == "__main__":
    a, b, t = map(int, input().split(' '))
    main(a, b, t)

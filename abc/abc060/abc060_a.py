"""A - Shiritori
https://atcoder.jp/contests/abc060/tasks/abc060_a

>>> main('rng', 'gorilla', 'apple')
YES
>>> main('yakiniku', 'unagi', 'sushi')
NO
>>> main('a', 'a', 'a')
YES
>>> main('aaaaaaaaab', 'aaaaaaaaaa', 'aaaaaaaaab')
NO

"""


def main(a, b, c):
    if a[-1] == b[0] and b[-1] == c[0]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    a, b, c = input().split(" ")

    main(a, b, c)

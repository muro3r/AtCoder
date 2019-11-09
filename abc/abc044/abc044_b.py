'''B - 美しい文字列 / Beautiful Strings
https://atcoder.jp/contests/abc044/tasks/abc044_b
w
>>> main('abaccaba')
Yes
>>> main('hthth')
No

'''


def main(w):
    w_sets = set()

    [w_sets.add(w[x]) for x in range(0, len(w))]

    for x in w_sets:
        if w.count(x) % 2 != 0:
            print('No')
            return

    print('Yes')


if __name__ == "__main__":
    w = input()

    main(w)

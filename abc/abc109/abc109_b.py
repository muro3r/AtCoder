"""B - Shiritori
https://atcoder.jp/contests/abc109/tasks/abc109_b
N
W_1
W_2
:
W_N

>>> main(4, ["hoge", "english", "hoge", "enigma"])
No
>>> main(9, ["basic", "c", "cpp", "php", "python", "nadesico", "ocaml", "lua",\
     "assembly"])
Yes
>>> main(8, ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaa", "aaaaaaa"])
No
>>> main(3, ["abc", "arc", "agc"])
No
"""


def main(n: int, w: list) -> None:
    if len(set(w)) != n:
        print("No")
        return

    last_letter = ""

    for w_n in w:
        if last_letter == "":
            last_letter = w_n[-1]
            continue

        if last_letter != w_n[0]:
            print("No")
            return

        last_letter = w_n[-1]

    print("Yes")


if __name__ == "__main__":
    n = int(input())
    w = [input() for _ in range(n)]

    main(n, w)

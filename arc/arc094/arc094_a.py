"""
>>> main('MinnnahaNakayoshi', 0, 6, 8, 17)
"Minnna"ha"Nakayoshi"

>>> main('Niwawo_Kakemeguru_Chokudai', 11, 17, 18, 26)
Niwawo_Kake"meguru"_"Chokudai"
"""


def main(s, a, b, c, d):
    s = list(s)

    for i in [a, b + 1, c + 2, d + 3]:
        s.insert(i, '"')

    print("".join(s))


if __name__ == "__main__":
    s = input()
    a, b, c, d = map(int, input().split())

    main(s, a, b, c, d)

"""A - 居合を終え、青い絵を覆う / UOIAUAI
https://atcoder.jp/contests/abc049/tasks/abc049_a

>>> main('a')
vowel
>>> main('z')
consonant
>>> main('s')
consonant

"""


def main(s):

    vowel = ["a", "i", "u", "e", "o"]

    for ob in vowel:
        if s.startswith(ob):
            print("vowel")
            return

    print("consonant")


if __name__ == "__main__":
    s = input()

    main(s)

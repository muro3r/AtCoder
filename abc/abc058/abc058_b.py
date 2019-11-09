'''B - ∵∴∵
https://atcoder.jp/contests/abc058/tasks/abc058_b

>>> main('xyz', 'abc')
xaybzc
>>> main('atcoderbeginnercontest', 'atcoderregularcontest')
aattccooddeerrbreeggiunlnaerrccoonntteesstt

'''


def main(o, e):
    for _o, _e in zip(o, e):
        print(_o + _e, end='')

    if len(o) != len(e):
        print(o[-1], end='')


if __name__ == "__main__":
    o = input()
    e = input()

    main(o, e)

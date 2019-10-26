'''B - Picture Frame

>>> main(2, 3,  ['abc', 'arc'])
#####
#abc#
#arc#
#####

>>> main(1, 1, ['z'])
###
#z#
###
'''


def main(h, w, a):
    print('#' * (w + 2))

    for s in a:
        print('#{}#'.format(s))

    print('#' * (w + 2))


if __name__ == '__main__':
    h, w = map(int, input().split(' '))
    a = []

    for _ in range(h):
        a.append(input())

    main(h, w, a)


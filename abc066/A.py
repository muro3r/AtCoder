def resolve():
    ls = []

    for s in map(int, input().split(' ')):
        ls.append(s)

    ls.sort()
    print(ls[0] + ls[1])
    pass


if __name__ == '__main__':
    resolve()


def resolve():
    w = input()
    w_sets = set()

    [w_sets.add(w[x]) for x in range(0, len(w))]

    for x in w_sets:
        if w.count(x) % 2 != 0:
            print('No')
            return

    print('Yes')


resolve()

def resolve(head, tail):
    if head <= 0 or tail <= 0:
        print('NA')
    elif head > 12 and tail > 12:
        print('NA')
    elif head > 12 and tail <= 12:
        print('YYMM')
    elif head <= 12 and tail > 12:
        print('MMYY')
    elif head <= 12 and tail <= 12:
        print('AMBIGUOUS')


if __name__ == "__main__":
    S = input()
    head = int(S[:2])
    tail = int(S[2:])

    resolve(head, tail)

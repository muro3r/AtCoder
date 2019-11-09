def resolve(s):
    head = int(s[:2])
    tail = int(s[2:])

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
    s = input()

    resolve(s)

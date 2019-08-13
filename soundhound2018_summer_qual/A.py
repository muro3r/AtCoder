def main(a, b):
    if a + b == 15:
        return '+'
    elif a * b == 15:
        return '*'

    return 'x'


if __name__ == '__main__':
    a, b = map(int, input().split(' '))

    print(main(a, b))

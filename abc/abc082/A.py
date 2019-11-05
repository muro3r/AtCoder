def main(a: int, b: int):
    return ((a + b + 1) // 2)


if __name__ == '__main__':
    a, b = map(int, input().split(' '))
    print(main(a, b))

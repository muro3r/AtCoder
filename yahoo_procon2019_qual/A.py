def main(N, K):
    if N - 1 >= K:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    N, K = map(int, input().split(' '))
    print(main(N, K))


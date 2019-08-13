def main(N):
    i = 0
    for s in str(N):
        i += int(s)

    if N % i == 0:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    N = int(input())
    print(main(N))


A, B = map(int, input().split(' '))

if A >= 13:
    print(B)
elif 6 <= A and A <= 12:
    print(B // 2)
elif A <= 5:
    print(0)


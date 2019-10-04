# https://atcoder.jp/contests/abc052/tasks/abc052_a

A, B, C, D = map(int, input().split(' '))

sum_A = A * B
sum_B = C * D

if sum_A > sum_B:
    print(sum_A)
else:
    print(sum_B)

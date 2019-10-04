import math

num = int(input().replace(' ', ''))

if math.sqrt(num) % 1 == 0:
    print('Yes')
else:
    print('No')

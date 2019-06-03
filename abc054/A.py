A, B = map(int, input().split(' '))

def re_define(input_):
    '''強さ順にする'''
    if input_ == 1:
        return 13
    
    return input_ - 1

A = re_define(A)
B = re_define(B)

if A > B:
    print('Alice')
elif A < B:
    print('Bob')
else:
    print('Draw')
p

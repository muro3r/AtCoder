'''A - Maximize the Formula
https://atcoder.jp/contests/abc110/tasks/abc110_a

>>> main([1,5,2])
53
>>> main([9,9,9])
108
>>> main([6,6,7])
82'''

def main(i):
    _i = sorted(i)
    print(int(''.join(_i[:1])) + _i[2])
    
if __name__ == '__main__':
    i = [i for i in map(int, input().split(' '))]
    main(i)

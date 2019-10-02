'''
A - Christmas Eve Eve Eve
https://atcoder.jp/contests/abc115/tasks/abc115_a

>>> main(25)
Christmas

>>> main(22)
Christmas Eve Eve Eve
'''

def main(d):
    day = 25
    _d = day - d
    
    out = ['Christmas']
    
    for _ in range(_d):
        out.append('Eve')
    
    print(' '.join(out))
    
if __name__ == '__main__':
    main(int(input()))

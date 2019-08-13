import A
def test_case_1():
    expect = '+'
    
    a,b = 4,11
    result = A.main(a,b)
    
    assert expect == result
    
def test_case_2():
    expect = '*'
    
    a,b = 3, 5
    result = A.main(a,b)
    
    assert expect == result
    
def test_case_3():
    expect = 'x'
    
    a,b = 1,1
    result = A.main(a,b)
    
    assert expect == result

import A


def test_case1():
    assert 'YES' == A.main(3, 2)


def test_case2():
    assert 'NO' == A.main(5, 5)


def test_case3():
    assert 'YES' == A.main(31, 10)


def test_case4():
    assert 'NO' == A.main(10, 90)

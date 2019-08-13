import A


def test_case_1():
    expect = 1500
    result = A.main(100, 20, 500, 40, 1000)

    assert expect == result


def test_case_2():
    expect = 0
    result = A.main(50, 100, 1500, 100, 1500)

    assert expect == result


def test_case_3():
    expect = 1000
    result = A.main(100, 100, 1000, 100, 1000)

    assert expect == result


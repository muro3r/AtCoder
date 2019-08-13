from abc104 import B


def test_case_1():
    S = 'AtCoder'

    expect = 'AC'
    result = B.main(S)

    assert expect == result


def test_case_2():
    S = 'ACoder'

    expect = 'WA'
    result = B.main(S)

    assert expect == result


def test_case_3():
    S = 'AcycliC'

    expect = 'WA'
    result = B.main(S)

    assert expect == result


def test_case_4():
    S = 'AtCoCo'

    expect = 'WA'
    result = B.main(S)

    assert expect == result


def test_case_5():
    S = 'Atcoder'

    expect = 'WA'
    result = B.main(S)

    assert expect == result

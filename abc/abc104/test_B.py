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


def test_case_b07():
    assert 'AC' == B.main('ApproaCh')


def test_case_b09():
    assert 'AC' == B.main('AccccCcccc')


def test_case_b12():
    assert 'WA' == B.main('ATCoder')

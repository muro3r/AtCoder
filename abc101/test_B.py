import B


def test_case_1():
    _input = 12
    expect = 'Yes'

    assert expect == B.main(_input)


def test_case_2():
    _input = 101
    expect = 'No'

    assert expect == B.main(_input)


def test_case_3():
    _input = 999999999
    expect = 'Yes'

    assert expect == B.main(_input)

from abc091.A import main


def test_case_1():
    assert 'Yes' == main(50, 100, 120)


def test_case_2():
    assert 'No' == main(500, 100, 1000)


def test_case_3():
    assert 'No' == main(19, 123, 143)


def test_case_4():
    assert 'Yes' == main(19, 123, 142)

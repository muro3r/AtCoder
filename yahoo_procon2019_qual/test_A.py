from yahoo_procon2019_qual.A import main


def test_case_1():
    assert 'YES' == main(3, 2)


def test_case_2():
    assert 'NO' == main(5, 5)


def test_case_3():
    assert 'YES' == main(31, 10)


def test_case_4():
    assert 'NO' == main(10, 90)

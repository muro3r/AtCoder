from abc082.A import main


def test_case_1():
    assert int(2) == main(1, 3)


def test_case_2():
    assert int(6) == main(7, 4)


def test_case_3():
    assert int(5) == main(5, 5)

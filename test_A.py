from A import main


def test_case_1():
    assert 520 == main(600, 300, 220, 420)


def test_case_2():
    assert 755 == main(555, 555, 400, 200)


def test_case_3():
    assert 1152 == main(549, 817, 715, 603)


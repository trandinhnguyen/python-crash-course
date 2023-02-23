from name_function import get_name


def test_get_name():
    full_name = get_name('nguyen', 'tran')
    assert full_name == 'Nguyen Tran'


def test_gets_name():
    full_name = get_name('nguyen', 'tran')
    assert full_name == 'Nguyen Tran'

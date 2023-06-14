import pytest
import src.phone
import src.item


@pytest.fixture
def get_phone_for_test():
    return src.phone.Phone("iPhone 14", 120_000, 5, 2)


def test_repr(get_phone_for_test):
    assert repr(get_phone_for_test) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(get_phone_for_test):
    assert get_phone_for_test.number_of_sim == 2

    get_phone_for_test.number_of_sim = 1

    assert get_phone_for_test.number_of_sim == 1

    with pytest.raises(ValueError):
        get_phone_for_test.number_of_sim = 0


def test_add():
    item1 = src.item.Item("Смартфон", 10000, 20)
    phone1 = src.phone.Phone("iPhone 14", 120_000, 5, 2)

    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert phone1 + item1 == 25

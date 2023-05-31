import pytest
import src.item


@pytest.fixture
def get_item_for_test():
    return src.item.Item('Book', 200.0, 173)


def test_calculate_total_price(get_item_for_test):
    assert get_item_for_test.calculate_total_price() == 34600.0
    assert isinstance(get_item_for_test.calculate_total_price(), float) is True


def test_apply_discount(get_item_for_test):
    get_item_for_test.pay_rate = 0.7
    get_item_for_test.apply_discount()

    assert get_item_for_test.price == 140.0
    assert isinstance(get_item_for_test.price, float) is True

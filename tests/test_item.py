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


def test_instantiate_from_csv():
    src.item.Item.instantiate_from_csv()
    item1 = src.item.Item.all[0]

    assert len(src.item.Item.all) == 5
    assert item1.name == 'Смартфон'
    assert item1.price == 100
    assert item1.quantity == 1

    with pytest.raises(FileNotFoundError):
        src.item.Item.instantiate_from_csv('../tests/items.csv')

    with pytest.raises(src.instantiate_csv_error.InstantiateCSVError):
        src.item.Item.instantiate_from_csv('../tests/test_items.csv')


def test_string_to_number():
    assert src.item.Item.string_to_number('5') == 5
    assert src.item.Item.string_to_number('5.0') == 5
    assert src.item.Item.string_to_number('5.5') == 5


def test_repr(get_item_for_test):
    assert repr(get_item_for_test) == 'Item(\'Book\', 200.0, 173)'


def test_str(get_item_for_test):
    assert str(get_item_for_test) == 'Book'

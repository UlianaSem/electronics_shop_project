import pytest

import src.keyboard


@pytest.fixture
def get_object_for_test():
    return src.keyboard.Keyboard('Dark Project KD87A', 9600, 5)


def test_init(get_object_for_test):
    assert str(get_object_for_test) == "Dark Project KD87A"
    assert str(get_object_for_test.language) == "EN"


def test_language(get_object_for_test):
    with pytest.raises(AttributeError):
        get_object_for_test.language = 'CH'


def test_change_lang(get_object_for_test):
    get_object_for_test.change_lang()
    assert str(get_object_for_test.language) == "RU"

    get_object_for_test.change_lang().change_lang()
    assert str(get_object_for_test.language) == "RU"

"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_router():
    return Item("роутер", 1000, 10)


def test_calculate_total_price(item_router):
    assert item_router.calculate_total_price() == 10000


def test_apply_discount(item_router):
    Item.pay_rate = 0.5
    item_router.apply_discount()
    assert item_router.price == 500


def test_name_setter(item_router):
    Item.name = "router"
    assert Item.name == "router"


def test_string_to_number():
    assert Item.string_to_number('5.55') == 5


def test_magic_method():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
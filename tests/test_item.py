"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from pytest import fixture

from src.item import Item

from src.phone import Phone


@fixture
def item():
    return Item("Смартфон", 10000, 20)

def test_total_price(item):
    assert item.calculate_total_price() == 200000


def test_discount(item):
    item.apply_discount()
    assert item.price == 10000.0


def test_string_to_number(item):
    item.string_to_number('2')
    assert item.string_to_number(2) == 2


def test_instantiate_from_csv(item):
    item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_name(item):
    with pytest.raises(Exception):
        item.name = "knbknknelnblenwblnbl"

def test_repr_(item):
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str_(item):
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'

def test_add__(item):
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
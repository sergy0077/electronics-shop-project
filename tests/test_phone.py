from src.phone import Phone
from src.item import Item

import pytest


def test_phone_name():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert phone.name == "iPhone 14"


def test_phone_price():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert phone.price == 120000


def test_phone_quantity():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert phone.quantity == 5


def test_phone_number_of_sim():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert phone.number_of_sim == 2


def test_phone_str():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert str(phone) == "iPhone 14"


def test_phone_repr():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_addition():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("Samsung Galaxy S21", 80_000, 3, 1)

    result = phone1 + phone2
    assert result == 8


def test_phone_addition_with_non_phone_object():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    item = Item("Smartwatch", 30_000, 10)


if __name__ == "__main__":
    pytest.main()

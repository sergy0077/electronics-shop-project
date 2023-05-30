from src.item import Item
import pytest


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    Item.pay_rate = 0.8
    item1.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 20000
    assert item1.price == 10000 * Item.pay_rate


def test_all_items(monkeypatch):
    # Создаем объекты Item
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    # Monkey patching - временно изменяем атрибут all класса Item
    monkeypatch.setattr(Item, 'all', [item1, item2])

    # Проверяем, что список all содержит два элемента
    assert len(Item.all) == 2

    # Проверяем, что элементы в списке all соответствуют созданным объектам Item
    assert Item.all[0] == item1
    assert Item.all[1] == item2


def test_item_name_getter():
    item = Item("Smartphone", 1000.0, 5)
    assert item.name == "Smartphone"


def test_item_name_setter_valid_length():
    item = Item("Smartphone", 1000.0, 5)
    item.name = "Phone"
    assert item.name == "Phone"


def test_item_name_setter_invalid_length():
    item = Item("Smartphone", 1000.0, 5)
    with pytest.raises(ValueError) as e:
        item.name = "VeryLongProductName"
    assert str(e.value) == "Длина наименования товара не должна превышать 10 символов."


def test_repr():
    item_r = Item("Смартфон", 10000, 20)
    assert repr(item_r) == "Item('Смартфон', 10000, 20)"


def test_str():
    item_s = Item("Смартфон", 10000, 20)
    assert str(item_s) == "Смартфон"


def test_class_attributes():
    Item.pay_rate = 1.0
    item = Item("Smartphone", 1000.0, 5)
    assert item.pay_rate == 1.0
    assert Item.pay_rate == 1.0

    Item.pay_rate = 0.9
    assert item.pay_rate == 0.9
    assert Item.pay_rate == 0.9


def test_clear_all():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    Item.clear_all()

    assert len(Item.all) == 0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()

    assert len(Item.all) > 0


def test_string_to_number():
    string_num = "10.5"

    assert Item.string_to_number(string_num) == 10.0


if __name__ == "__main__":
    pytest.main()

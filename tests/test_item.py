"""Здесь надо написать тесты с использованием pytest для модуля item."""
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

def test_name_getter_and_setter():
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    try:
        item.name = 'СуперСмартфон'
    except Exception as e:
        assert str(e) == 'Длина наименования товара превышает 10 символов.'
    else:
        assert True, 'Ожидалось возникновение исключения'

test_name_getter_and_setter()

if __name__ == "__main__":
    pytest.main()
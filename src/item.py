import csv

class Item:
    """
    Класс для представления товара в магазине.
    """

    @property
    def name(self):
        return self.__name

    pay_rate = 1.0
    all = []

    @classmethod
    def clear_all(cls):
        """
        Очищает список всех товаров.
        """
        cls.all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def get_name(self) -> str:
        """
        Геттер для получения названия товара.
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """
        Сеттер для установки названия товара.
        Проверяет, что длина наименования товара не больше 10 символов.
        """
        if len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[:10]

    def __repr__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса Item.
        """
        return f"Item(name='{self.__name}', price={self.price}, quantity={self.quantity})"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        if self.__name == "Смартфон":
            self.price = self.price * self.pay_rate
        else:
            self.price = self.price

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv.
        """
        cls.all = []  # Очистка списка перед добавлением данных
        with open('C:/Users/Sergy007/PycharmProjects/electronics-shop-project/src/items.csv', 'r', encoding='utf-8') \
                as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = Item(name, price, quantity)
                cls.all.append(item)

    @staticmethod
    def string_to_number(string: str) -> float:
        """
        Возвращает число из числа-строки.
        :param string: Число-строка.
        :return: Число.
        """
        return int(float(string))

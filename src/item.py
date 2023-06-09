import csv

import src.instantiate_csv_error


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

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

        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__) or isinstance(self, self.__class__):
            return self.quantity + other.quantity
        else:
            raise TypeError('Объекты должны принадлежать классам Item и Phone')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 11:
            self.__name = new_name
        else:
            raise Exception('Длина наименования товара превышает 10 символов.')

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
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path='../src/items.csv'):
        """Метод,инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        cls.all.clear()

        try:
            with open(path, 'r', encoding='Windows-1251') as csv_file:
                reader = csv.DictReader(csv_file)

                if reader.fieldnames != ['name', 'price', 'quantity']:
                    raise src.instantiate_csv_error.InstantiateCSVError

                for line in reader:
                    cls(line['name'], float(line['price']), int(line['quantity']))

        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(string):
        """
        Возвращает число из числа-строки.
        :param string: число в str
        :return: число в int
        """
        return int(float(string))

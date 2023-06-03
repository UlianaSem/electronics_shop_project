import csv


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
    def instantiate_from_csv(cls):
        """Метод,инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        cls.all.clear()

        with open('../src/items.csv', 'r', encoding='Windows-1251') as csv_file:
            reader = csv.DictReader(csv_file)

            for line in reader:
                cls(line['name'], float(line['price']), int(line['quantity']))

    @staticmethod
    def string_to_number(string):
        """
        Возвращает число из числа-строки.
        :param string: число в str
        :return: число в int
        """
        return int(float(string))

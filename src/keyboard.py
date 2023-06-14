import src.item


class Mixing:
    """
    Класс-миксин для реализации функционала по хранению и изменению раскладки клавиатуры.
    """
    def __init__(self, language: str = 'EN'):
        """
        Создание экземпляра класса Mixing.
        :param language: Язык раскладки (по умолчанию, EN)
        """
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Изменение раскладки клавиатуры
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'

        return self


class Keyboard(src.item.Item, Mixing):
    """
    Класс для представления товара 'клавиатура' в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса Keyboard.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__(name, price, quantity)
        Mixing.__init__(self)

import src.item


class Phone(src.item.Item):
    """
    Класс для представления смартфона в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество сим-карт в смартфоне.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim_number):
        if isinstance(sim_number, int) and sim_number > 0:
            self.__number_of_sim = sim_number
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

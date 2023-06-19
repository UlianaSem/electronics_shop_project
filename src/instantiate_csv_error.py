class InstantiateCSVError(Exception):
    """Класс-исключение для проверки колонок в файле items.csv"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'

    def __str__(self):
        return self.message

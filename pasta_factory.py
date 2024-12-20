# Базовый класс для пасты
class Pasta:
    def type_of_pasta(self):
        pass

    def sauce(self):
        pass

    def filling(self):
        pass

    def toppings(self):
        pass

# Конкретные классы пасты
class Spaghetti(Pasta):
    def type_of_pasta(self):
        return "Спагетти"

    def sauce(self):
        return "Томатный соус"

    def filling(self):
        return "Нет начинки"

    def toppings(self):
        return "Пармезан"

class Penne(Pasta):
    def type_of_pasta(self):
        return "Пенне"

    def sauce(self):
        return "Сливочный соус"

    def filling(self):
        return "Курица"

    def toppings(self):
        return "Базилик"

class Fettuccine(Pasta):
    def type_of_pasta(self):
        return "Феттучини"

    def sauce(self):
        return "Алфредо соус"

    def filling(self):
        return "Грибы"

    def toppings(self):
        return "Петрушка"

# Фабрика пасты
class PastaFactory:
    @staticmethod
    def create_pasta(pasta_type):
        if pasta_type == "spaghetti":
            return Spaghetti()
        elif pasta_type == "penne":
            return Penne()
        elif pasta_type == "fettuccine":
            return Fettuccine()
        else:
            raise ValueError("Unknown pasta type")

# Пример использования
pasta1 = PastaFactory.create_pasta("spaghetti")
print(pasta1.type_of_pasta())
print(pasta1.sauce())
print(pasta1.filling())
print(pasta1.toppings())

pasta2 = PastaFactory.create_pasta("penne")
print(pasta2.type_of_pasta())
print(pasta2.sauce())
print(pasta2.filling())
print(pasta2.toppings())
# Строитель
class Builder:
    def prepare_floor(self):
        pass

    def lay_tiles(self):
        pass

    def apply_putty(self):
        pass

    def plaster_walls(self):
        pass

    def prime_wall(self):
        pass

    def paint_wall(self):
        pass

# Конкретные строители
class Tiler(Builder):
    def prepare_floor(self):
        return "Подготовка пола завершена."

    def lay_tiles(self):
        return "Плитка уложена."

class Finisher(Builder):
    def apply_putty(self):
        return "Шпаклевка нанесена."

    def plaster_walls(self):
        return "Стены оштукатурены."

class Painter(Builder):
    def prime_wall(self):
        return "Стена загрунтована."

    def paint_wall(self):
        return "Стена покрашена."

# Прораб (директор)
class Foreman:
    def __init__(self):
        self.tiler = Tiler()
        self.finisher = Finisher()
        self.painter = Painter()

    def make_floors(self):
        return self.tiler.prepare_floor() + " " + self.tiler.lay_tiles()

    def level_walls(self):
        return self.finisher.apply_putty() + " " + self.finisher.plaster_walls()

    def paint_walls(self):
        return self.painter.prime_wall() + " " + self.painter.paint_wall()

    def complete_work(self):
        return "Работы под ключ завершены."

# Пример использования
foreman = Foreman()
print(foreman.make_floors())
print(foreman.level_walls())
print(foreman.paint_walls())
print(foreman.complete_work())
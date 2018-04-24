import random

class Dish:
    def __init__(self, name, time):
        self.dishes_list = name
        self.calc_time = time
    def calc_time():
        return random.randint(1, 100)
    def dots(self):
        return self.ljust(40, '.')
    def to_print(self):
        return Dish.dots(self) + ' ' + str(Dish.calc_time()) + ' min'

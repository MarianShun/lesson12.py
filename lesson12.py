import random
dishes_string = input('What would you like? (comma required)\n') 
dishes_list = dishes_string.title().split(',')

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
stripped_dishes_list = [i.strip() for i in dishes_list]
unique_dishes_list = list(set(stripped_dishes_list))
for unique_dishes in unique_dishes_list:
    if unique_dishes != '':
	print(Dish.to_print(unique_dishes))

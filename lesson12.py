import random
dishes_string = input('What would you like? (comma required)\n')  # This is a string
dishes_list = dishes_string.title().split(',')
stripped_dishes_list = [i.strip() for i in dishes_list]
unique_dishes_list = list(set(stripped_dishes_list))
def empty_line():
    empty_line = ''
    return empty_line
for unique_dishes in unique_dishes_list:
    if unique_dishes != empty_line(): print(unique_dishes.ljust(40, '.'), random.randint(1,60), 'min')


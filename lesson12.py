import random
dishes_string = input('What would you like? (comma required)\n')  # This is a string
dishes_list = dishes_string.title().split(',')
stripped_dishes_list = [i.strip() for i in dishes_list]
unique_dishes_list = list(set(stripped_dishes_list))
def time():
    return random.randint(1, 60)
for unique_dishes in unique_dishes_list:
    if unique_dishes != '':
	    print(unique_dishes.ljust(40, '.'), time(), 'min')

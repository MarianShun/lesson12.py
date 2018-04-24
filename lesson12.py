from dish import Dish

dishes_string = input('What would you like? (comma required)\n') 
dishes_list = dishes_string.title().split(',')
stripped_dishes_list = [i.strip() for i in dishes_list]
unique_dishes_list = list(set(stripped_dishes_list))

for unique_dishes in unique_dishes_list:
    if unique_dishes != '':
	print(Dish.to_print(unique_dishes))

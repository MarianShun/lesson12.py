import random
dishes_string = input('What would you like?\n')  # This is a string
dishes_list = dishes_string.title().split(',')
stripped_dishes_list = [i.strip() for i in dishes_list]
unique_dishes_list = list(set(stripped_dishes_list))
# put your program here
random_integer = random.randint(0, 1000)
# your program’s end
for unique_dishes_list in unique_dishes_list:
    print(unique_dishes_list.ljust(40, '.'), random.randint(0,60), 'min')
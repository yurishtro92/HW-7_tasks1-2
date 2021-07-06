from pprint import pprint
from collections import defaultdict

def get_cook_book():
    cook_book = defaultdict(list)
    list_1 = []
    with open("recipes.txt", encoding="utf-8") as file:
         for line in file:
             cook_name = line.strip()
             ingredients_quantity = int(file.readline().strip())
             for ingredient in range(ingredients_quantity):
                 words = file.readline().split()
                 d = defaultdict(list)
                 if len(words) == 5:
                     d['ingredient_name'] = words[0]
                     d['quantity'] = words[2]
                     d['measure'] = words[4]
                     list_1.append(dict(d))
                 else:
                     d['ingredient_name'] = words[0] + ' ' + words[1]
                     d['quantity'] = words[3]
                     d['measure'] = words[5]
                     list_1.append(dict(d))
             cook_book[cook_name] += list_1
             list_1.clear()
             file.readline()
    return dict(cook_book)
# pprint(get_cook_book(), sort_dicts=False)

person_count = 2
dishes = list(get_cook_book().keys())

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in get_cook_book().values():
        for ingredient in dish:
            key = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = int(ingredient['quantity']) * person_count
            dict_1 = defaultdict(list)
            dict_1['measure'] = measure
            dict_1['quantity'] = quantity
            shop_list[key] = dict(dict_1)
    return shop_list
pprint(get_shop_list_by_dishes(dishes, person_count))

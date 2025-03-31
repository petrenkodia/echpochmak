from collections import OrderedDict

print('Множества - set')

print('ЗАДАНИЕ 1')
a = (3, 7) # кортеж
list1 = [3, 2, 4.5, a, 2, "а", (3, 7), (7, 3), 7, (2, "а")] # список (д.б. с неизм. данными)
set1 = set(list1)
print('Преобразованное из списка множество №1: ')
print(set1) # Каждый раз дает разный порядок

print('ЗАДАНИЕ 2')
set2 = {3, 4, a, "б", (2, "а")}
union12 = set1.union(set2) # объединение, оператор |
# метод set1.update(set2), изм. исх. мн-во ( оператор |= )
intersection12 = set1.intersection(set2) # пересечение, оператор &
# метод set1.intersection_update(set2), изм. исх. мн-во ( оператор &= )
print('Множество №2:')
print(set2)
print('Объединение множеств:')
print(union12)
print('Пересечение множеств:')
print(intersection12)

print('ЗАДАНИЕ 3')
difference12 = set1.difference(set2) # разность, оператор -
# set1.difference_update(set2) удаляет из мн-ва элем., кот. есть во втором мн-ве или кортеже ( -= )
print('Разность множеств:')
print(difference12)

print('ЗАДАНИЕ 4')
sym_dif12 = set1.symmetric_difference(set2) # оператор ^
# symmetric_difference_update() — изм. исх. мн-во ( ^= )
print('Симметрическая разность множеств (противоп. пересечению):')
print(sym_dif12)

print('ЗАДАНИЕ 5')
set3 = {3, 4}
print("Множество №3:", set3)
print('Проверка на подмножество (мн-во 2 для мн-ва 1):', set2.issubset(set1))
print('Проверка на подмножество (мн-во 3 для мн-ва 2):', set3 <= set2)

print('ЗАДАНИЕ 6')
set3.add(a) # добавляет кортеж a = (3, 7)
set3.update(a) # добавляет именно элементы из кортежа
print("Добавили кортеж 'а' (3, 7) и его элементы:", set3)
set3.remove(a) # удаляет кортеж a = (3, 7)
set3.discard(404) # пытается удалить, но если элемента нет - ошибку не выдаст
print("Удалили кортеж 'а':", set3) #Чтобы убрать его элементы, наверное нужно циклом for
set3.discard(7)
set3.difference_update(a) # одного элемента не было - ошибку не выдал
print("Удалили элементы кортежа 'а':", set3)

print('ЗАДАНИЕ 7')
b = tuple(set3)
set4 = {0, 1, "два", (3, b), 5} # кортеж b из множества {4} внутри другого кортежа
for elem in set4:
    print(elem) # печатает без порядка

print('ЗАДАНИЕ 8')
list2 = [2, 3, 4, "а", 3, (4,), 5, "а"] # без [] это считается кортеж ()
set4.update(list2) # добавил уникальные элементы списка в мн-во set4
print(set4)

print('ЗАДАНИЕ 9')

# Используем OrderedDict из collections
print("Вариант с OrderedDict: ", list(OrderedDict.fromkeys(list2)))
""" OrderedDict — это СЛОВАРЬ, который СОХРАНЯЕТ ПОРЯДОК добавления элементов. Вроде сейчас уже все сохраняют.
Юзаем его для УДАЛЕНИЯЯ ДУБЛИКАТОВ из list2, т.к. ключи в словаре уникальны.
OrderedDict ожидает список пар "ключ-значение". Например: OrderedDict([(3, "значение1"), (5, "значение2")])
Для удаления дубликатов из СПИСКА нужно использовать метод fromkeys() """

 # Пробуем обойтись без доп. модулей с помощью вспомог. мн-ва:
unique_list = [] # Список уник. элем. в исх. порядке, будем добавлять в него
set_for_help = set() # Вспомогательное мн-во {} в помощь мне
for elem in list2:
    if elem not in set_for_help:
        unique_list.append(elem)
        set_for_help.add(elem)
print("Вариант с вспомог. множеством: ", unique_list)

# Еще в инете нашла интересный вариант с жутким генератором списков:
set_for_help2 = set()
unique_list2 = [x for x in list2 if not (x in set_for_help2 or set_for_help2.add(x))]
# set_for_help2.add(x) - возвращает None и добавляет х в set, если его там нет (сложно, но интересно)
print("Вариант с генератором списка: ", unique_list2)

print('ЗАДАНИЕ 10')
set2.add(6.0) # четное float
print("Возьмем объединение set1:", set1,"и set2:", set2)
union_set = set1 | set2

chetnye_in_union = [elem for elem in union_set if isinstance(elem, (int, float)) and elem % 2 == 0] # делаю список, чтобы сохранить порядок
print("Выведем только четные числа (список):", chetnye_in_union)

tuples_in_union = {elem for elem in union_set if type(elem) == tuple} # сразу мн-во без порядка элементов
print("Теперь выведем только те, что являются кортежами (множество):", tuples_in_union)

""" Функция isinstance(elem, (tuple, int)) - проверяет, является ли объект экземпляром указанного типа.
Можно нескольких типов и поддерживает наследование (но я не поняла, что это такое :) 
Если только один тип проверить - можно через type"""


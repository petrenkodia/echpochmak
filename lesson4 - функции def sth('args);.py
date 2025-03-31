from functools import reduce

print('Функции')

print("ЗАДАНИЕ 1")
def greet(name):
    print(f"Привет, {name}! Как твои дела?")
# greet(input("Как тебя зовут? "))
# Ввод имени выше работает, проверила
greet("Руслан")

print("ЗАДАНИЕ 2")
def square(number):
    return number ** 2
result = square(4)
print(result)

print("ЗАДАНИЕ 3")
def multiply(a, b):
    return a * b
result = multiply(3, 5)
print(result)

print("ЗАДАНИЕ 4")
def power(base, exp = 2):
    return base ** exp
print(power(3))
print(power(3, 3))

print("ЗАДАНИЕ 5")
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40))

print("ЗАДАНИЕ 6")
def min_max(numbers):
    return min(numbers), max(numbers)
min_val, max_val = min_max([10, 20, 5, 30, 15])
print(min_val, max_val)

print("ЗАДАНИЕ 7")
# Рекурсия — это когда функция вызывает саму себя. Жесть
def factorial(n):
    if n == 0 | n == 1:
        return 1
    elif n > 1:
        return n * factorial(n - 1)
print(factorial(5))  # Вывод: 120

print("ЗАДАНИЕ 8")
def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    else:
        return a / b
print(divide(10, 2))
print(divide(10, 0))

print("ЗАДАНИЕ 9.1")
def filter_even(numbers):
    list1 = []
    for elem in numbers: # Способ 1: Цикл for
        if elem % 2 == 0:
            list1.append(elem)
    return list1
print(filter_even([1, 2, 3, 4, 5, 6]))

print("ЗАДАНИЕ 9.2")
def filter_even(numbers):
    # Способ 2: генератор списка
    return [elem for elem in numbers if elem % 2 ==0]
print(filter_even([1, 2, 3, 4, 5, 6]))

print("ЗАДАНИЕ 11")
def square_list(numbers):
    return [num ** 2 for num in numbers]
print(square_list([1, 2, 3, 4]))

print("ЗАДАНИЕ 12")
"""Функция filter() в Python используется для фильтрации элементов итерируемого объекта 
(например, списка, кортежа) на основе условия. Она возвращает итератор, содержащий только те элементы, 
для которых условие выполняется (т.е. функция-фильтр возвращает True)."""
def filter_positive(numbers):
    return list(filter(lambda x: x > 0, numbers)) # 2 арг.: (безым. ф-ия с усл., пул знач.)
print(filter_positive([-1, 2, -3, 4, 0, 5]))

print("ЗАДАНИЕ 13")
"""Функция reduce() используется для последовательного применения функции
 к элементам итерируемого объекта (например, списка), сводя их к одному значению. 
 Можно заменить на цикл или генератор. Можно задать начальное значение (3 место, после пула знач.)"""
def product(numbers):
    return reduce(lambda x, y: x * y, numbers) # 2 арг.: (безым. ф-ия для 2 перем., пул знач.)
print(product([1, 2, 3, 4]))

print("ЗАДАНИЕ 14")
def count_vowels(text):
    num = 0
    vowels = ["a", "e", "i", "o", "u"]
    for elem in text:
        if elem in vowels:
            num += 1
    return num
print(count_vowels("Hello, World!"))

print("ЗАДАНИЕ 15")
"""Замыкание (closure) — это функция, которая запоминает значения из окружающего её контекста 
(например, переменные из внешней функции) и может использовать их даже после завершения работы внешней функции.
Ф-ия create_multiplier(n) принимает число n. Возвр. другую ф-ию, кот. принимает число x и возвр. рез-т умн. x на n."""
def create_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

# Создаём ФУНКЦИЮ, которая умножает на какое-то число (например, 2)
double = create_multiplier(2)
# Используем созданную функцию
print(double(5))  # Вывод: 10

# Создаём ФУНКЦИЮ, которая умножает на 3
triple = create_multiplier(3)
print(triple(10))  # Вывод: 30

print("ЗАДАНИЕ 16")
def print_info(**kwargs): # именнованные аргументы, неизв. сколько
    for key, value in kwargs.items():
        print(f"Ключ: {key}, Значение: {value}")
print_info(имя = "Диана", возраст = 27, город = "СПб")

print("ЗАДАНИЕ 17")
def create_profile(name, **kwargs): # name задается строкой, остальное по парам
    profile = {"name" : name}
    profile.update(kwargs)
    return profile
print(create_profile("Diana", age = 27, city = "SPb"))

print("ЗАДАНИЕ 18")
def process_data(*args, **kwargs):
                return list(args), list(kwargs), list(kwargs.values())
args_list, args_keys, args_val = process_data(1, 2, 3, имя = "Ди", age = 27)
print(args_list)
print(args_keys)
print(args_val) # добавила вывод значений

print("ЗАДАНИЕ 19")
def filter_kwargs(**kwargs):
    filt_dict = {}
    for key, value in kwargs.items():
        if type(value) is str: # isinstance(value, str) - вариант от нейронки
            filt_dict[key] = value # добавили значение в словарь
    return filt_dict
filtered = filter_kwargs(name="Alice", age=25, city="New York")
print("Способ 1:", filtered)

def filter_kwargs2(**kwargs):
    return {key : value for key, value in kwargs.items() if isinstance(value, str)} # Способ 2 - генератор словаря
filtered = filter_kwargs2(name="Alice", age=25, city="New York")
print("Способ 2:", filtered)

print("ЗАДАНИЕ 20")
def merge_dicts(**kwargs):
    new_mer_dict = {}
    for key, value in kwargs.items():
        new_mer_dict.update(value)
    return new_mer_dict
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
result = merge_dicts(first=dict1, second=dict2)
print(result)

# выше делала сама (я - молодец!), а ниже вариант нейронки:

def merge_dicts2(**kwargs):
    return {k: v for d in kwargs.values() for k, v in d.items()}
""" kwargs.values() возвращает список значений, т.е. список словарей: [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
1) Внешний цикл for d in kwargs.values():
Проходит по каждому словарю d в списке значений kwargs.values().
Например: Первая итерация: d = {'a': 1, 'b': 2}, Вторая итерация: d = {'c': 3, 'd': 4}.
2) Внутренний цикл for k, v in d.items():
Проходит по каждой паре "ключ-значение" в текущем словаре d"""
dict1 = {"e": 5, "f": 6}
dict2 = {"f": 7} # update перезапишет по ключу f
result = merge_dicts2(first=dict1, second=dict2)
print(result)

print("ЗАДАНИЕ 21")
def check_keys(**kwargs):
    return 'name' in kwargs.keys() and 'age' in kwargs.keys() # .keys() можно убрать, но пусть для наглядности
print(check_keys(name="Alice", age=25))
print(check_keys(name="Bob"))

print("ЗАДАНИЕ 22")
def create_person(**kwargs):
    if 'name' not in kwargs.keys() or 'age' not in kwargs.keys():
        raise ValueError("Обязательные ключи 'name' и 'age' отсутствуют.")
    else:
        return kwargs
person = create_person(name="Alice", age=25, city="New York")
print(person)

print("ЗАДАНИЕ 23")
def process_kwargs(**kwargs):
    for k, v in kwargs.items():
        if type(v) is str:
           kwargs[k] = v.upper()
        if isinstance(v, (int, float)):
            kwargs[k] = v * 2
    return kwargs
result = process_kwargs(a=21, b="hello", c=True, d=15.02)
print(result)

print("ЗАДАНИЕ 24. Мое любимое число, а задачи нет, ну лан")

print("ЗАДАНИЕ 25")
def filter_by_type(**kwargs):
    kwargs_new = {k: v for k, v in kwargs.items() if type(v) is int} # isinstance(v,int) считает bool подтипом int (1)
    return kwargs_new
filtered = filter_by_type(a=10, b="hello", c=3.14, d=True)
print(filtered)

print("ЗАДАНИЕ 26")
def sum_values(**kwargs):
    summa = 0
    for v in kwargs.values():
        if type(v) is float or type(v) is int:
            summa += v
    return summa
result = sum_values(a=10, b=20, c=30, d="40", e=True, f=0.66)
print(result)

print("ЗАДАНИЕ 27")
def create_config(**kwargs):
    for k,v in kwargs.items():
        if k == "debug":
            if isinstance(v, str):
                kwargs[k] = v.upper() == "TRUE" # сравнение строки в нижнем регистре со строкой "true". (вернет T/F)
            else:
                kwargs[k] = bool(v)
            return kwargs
config = create_config(debug="True", log_level="INFO", max_connections=100)
print(config)

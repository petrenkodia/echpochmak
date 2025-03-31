print('Совместное использование структур данных') # Делала с нейронкой, сложно

print('ЗАДАНИЕ 1')
list_students = [
    ("Аня", "Математика", 90), ("Аня", "Физика", 85), ("Аня", "Русский язык", 80),
    ("Диана", "Математика", 92), ("Диана", "Физика", 89), ("Диана", "Русский язык", 95),
    ("Ксюша", "Математика", 70), ("Ксюша", "Физика", 60), ("Ксюша", "Русский язык", 80)
] # Список из кортежей, поэтому [].

dict_name_grades = {} # Словарь, где key — имя, value — СПИСОК оценок
for name, subject, grade in list_students:
    if name not in dict_name_grades:
        dict_name_grades[name] = []  # Если имя (key) новое, то создаем пустой СПИСОК в качестве value
    dict_name_grades[name].append(grade)  # Добавляем оценку в СПИСОК values к соответствующему имени (key)
print("1) Словарь со всеми оценками:", dict_name_grades)

dict_aver_grade = {} # Словарь, где key — имя, value — средняя оценка
for name, grade in dict_name_grades.items(): # созданный ранее
    dict_aver_grade[name] = sum(grade) / len(grade)

porog = float(input("Введите пороговое значение для сред. оценки: ")) # Заданный порог
top_students = [name for name, avg in dict_aver_grade.items() if avg >= porog] # Список подходящих учеников
print("2) Словарь со сред. баллом:", dict_aver_grade)
print("3) Список имен хороших студентов: ", top_students)

print('ЗАДАНИЕ 2')
products = [
    {"товар": "яблоки", "цена": 50, "количество": 10},
    {"товар": "бананы", "цена": 30, "количество": 5},
    {"товар": "яблоки", "цена": 50, "количество": 8},
    {"товар": "апельсины", "цена": 70, "количество": 12},
] # Список словарей

uniq_prod = set() # МН-ВО для уник. товаров
dict_revenue = {} # СЛОВАРЬ для суммарной выручки

for prod in products: # Для каждого СЛОВАРЯ из списка (конкрет. словарь товара)

    product = prod["товар"] # Т.е. конкретно продукт АПЕЛЬСИН или БАНАН
    uniq_prod.add(product) # Доб. назв. товара в мн-во

    price = prod["цена"]
    quantity = prod["количество"]

    revenue = price * quantity # Вычисляем выручку для текущего слвоаря товара

    # Если такой товар уже есть в словаре как key, добавляем выручку к существующему значению
    if product in dict_revenue:
        dict_revenue[product] += revenue
    else:
        # Если товара нет в словаре, создаем новую запись key - зазв. продукта
        dict_revenue[product] = revenue

print("1) Мн-во уникальных товаров:", uniq_prod)
print("2) Новый словарь, где ключ — назв. товара, а знач. — суммарная выручка:\n", dict_revenue)
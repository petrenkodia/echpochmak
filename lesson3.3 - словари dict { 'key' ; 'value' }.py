from operator import itemgetter

print('Словари - dict')

print('Задание 1')
slovar = {
    "имя": "Дианочка",
    "фамилия": "Петренко",
    "возраст": 27
}
slovar["зз"] = "телец" # добавила
slovar["возраст"] = 21 # поменяла
del slovar["фамилия"] # удалила
print(slovar)

print('Задание 2')
slovar2 = {
    "возраст": 28,
    "университет": "Политех",
    "исполнитель": "Эминем"
}
slovar.update(slovar2)
print(slovar)

print('Задание 3')
for key, value in slovar.items():
    print(f"{key}: {value}")

print('Задание 4')
slovar_new = {
    "Дан Балан": 150,
    "Крыса Лариса": 5,
    "Капучин": 666,
    "Эрик Пэнисов": 33
}
name = input("Введите имя (например, Капучин): ")
if name in slovar_new:
    print(f"Возраст героя {name} равен {slovar_new[name]} годиков")
else:
    print("Нет такого значения")

print('Задание 5') #Перевернем предыдущий словарь
slovar_rev = {}
for key, value in slovar_new.items():
    slovar_rev[value] = key  # добавила
print("Перевернуты словарь:")
for key, value in slovar_rev.items():
    print(f"{key}: {value}")

print('Задание 6')
stroka = input("Введите строку для подсчета символов: ")
slovar_str = {}
for elem in stroka:
    if elem != " ": #отсекли пробелы
        if elem in slovar_str: #
            slovar_str[elem] += 1
        else:
            slovar_str[elem] = 1
print("Словарь с количеством вхождений символов:")
print(slovar_str)

print('Задание 7') # чет намутила, что сама запуталась, но вроде работает
slovar_stud = {
    "БРБшка": 5,
    "Гудков": 3,
    "Варнава": 4,
    "Кукушкин": 2,
    "Бреганов": 5
}
chislo = int(input("Введите минимальную оценку: "))
slovar_good_stud = {}
for elem in slovar_stud:
    if slovar_stud[elem] >= chislo:
        slovar_good_stud[elem] = slovar_stud[elem]
print(f"Ученики с оценкой не ниже {chislo}:")
for key, value in slovar_good_stud.items():
    print(f"{key}: {value}")

print('Задание 8. Сортируем словарь по ключу (превращая в список кортежей)') # Берем словарь студентов и оценок
not_slovar_yet_sort = sorted(slovar_stud.items()) # items возвращает пары в виде перечня КОРТЕЖЕЙ !
print("Отсортированный (по алфавиту ключа) словарь:")
for key, value in not_slovar_yet_sort:
    print(f"{key}: {value}")
print("Который на самом деле - перечень кортежей (не является списком):")
print(not_slovar_yet_sort)
print("Но если сделать списком (list) - выглядит также:")
print(list(not_slovar_yet_sort))

print('Задание 9. Сортируем словарь по значению (по возрастанию)') # Это пипец как долго я искала решение
print("ВАРИАНТ 1. Отсортированные пары (модуль operator, ф-ия itemgetter):")
sorted_pairs = sorted(slovar_stud.items(), key=itemgetter(1))
for key, value in sorted_pairs:
    print(f"{key} - {value}")
print("ВАРИАНТ 2. Отсортированные пары (делаем аноним. функцию, чтобы выбрать значение):")
sorted_pairs2 = sorted(slovar_stud.items(), key=lambda x: x[1])
for key, value in sorted_pairs2:
    print(f"{key} - {value}")

print('Задание 10')
students = {
    "Чрездевиц": {"математика": 91, "физика": 87, "химия": 42},
    "Талала": {"математика": 88, "физика": 92, "химия": 95},
    "Ворон Барон": {"математика": 75, "физика": 80, "химия": 85}
}
for name, elem in students.items():
    aver = sum(elem.values()) / len(elem) #Сумма оценок делим на кол-во предметов
    print(f"{name}: средний балл = {aver:.2f}")

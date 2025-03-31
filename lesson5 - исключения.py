print('5.1 Исключения')
"""
print("ЗАДАНИЕ 1")
def delenie():
    while True:  # Бесконечный цикл для повторного ввода в случае ошибки
        try:
            x = float(input("Введите делимое: "))
            y = float(input("Введите делитель: "))
            resultat = x / y
            print("Результат деления:", resultat)
            break
        except ValueError:
            print("Все фигня, Руслан, давай по-новой (не введено число)")
        except ZeroDivisionError:
            print("На ноль делить нельзя!")
delenie()

print("ЗАДАНИЕ 2")
spisok = ["zero", 1,2,"3", 2+2, True]
while True:
    try:
        index = int(input("Введите индекс (от 0 до 4): "))
        if index < 0: # либо raise IndexError
            print("Все фигня, Руслан, давай по-новой (отрицательный индекс)")
            continue
        print("Элемент списка по индексу:", spisok[index])
        break
    except ValueError:
        print("Все фигня, Руслан, давай по-новой (не целое число)")
    except IndexError:
        print("Все фигня, Руслан, давай по-новой (выход за границы списка)")

print("ЗАДАНИЕ 3")
def del_srez():
    while True:  # Бесконечный цикл (пока не получим правильный ввод)try:
        try:
            n = float(input("Введите целое число: "))
            d = 100 / n
            result = str(d)[:3]
            print("Ответ:", result)
            break
        except ZeroDivisionError:
            print("Ошибка: на ноль делить нельзя!")
        except ValueError as e:
            print("Ошибка значения (например, буквы или пустая строка)")
            print(e)  # Выведет сообщение из ValueError
        except TypeError: # Здесь не возникнет, т.к. input всегда передает строку !!!
            print("Ошибка типа данных (например, передан список или None)!")
del_srez()
"""
print("ЗАДАНИЕ 4")
while True:  # Бесконечный цикл (пока не получим правильный ввод)try:
    i = input("Введите ЦЕЛОЕ число (или 'выход'): ")
    if i == "выход":
        print("Покасики!:)")
        break

    try:
        n = int(i)
        print("Результат деления:", str(10 / n)[:5]) # результат становится float, округлила до 5
        break
    except ZeroDivisionError:
        print("Ошибка: на ноль делить нельзя!")
    except ValueError as e:
        print("Ошибка значения (например, буквы или дробное число)")
        print(e)  # Выведет сообщение из ValueError
    except TypeError:  # Здесь не возникнет, т.к. input всегда передает строку !!!
        print("Ошибка типа данных (например, передан список или None)!")

print("ЗАДАНИЕ 5")
def check_age(age):



Генерирует ValueError при попытке передать отрицательный возраст (меньше 0).
Генерирует TypeError, если переданный аргумент не является числом.

try:
    a = int(age)
    if a <= 0:
        raise ValueError
check_age(input("Введите возраст (натуральное число):"))
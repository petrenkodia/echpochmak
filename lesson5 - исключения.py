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
def check_age(age): #Проверяет возраст, выдаст ошибку, как по условию задачи, если что (!)
    try:
        age = float(age) # Пробуем преобразовать в число
    except (TypeError, ValueError):  # Ловим оба типа ошибок, но тут будет только Value (т.к. str) !!!
        raise TypeError("Возраст должен быть числом, а не магическим символом!") # Но выводим в любом случае TypeError !
    # Далее уже преобразованное число, проверяем на отрицательность и адекватность (уже будет ValueError, если что)
    if age < 0:
        raise ValueError("Даже призраки не имеют отрицательного возраста!") 
    elif age == 0:
        raise ValueError("Вы только что родились с классом 'Младенец-воин'! Ваши текущие статы: Кричать +3, Спать +2")
    elif age >120:
        print("С такими годами вам пора в класс 'Древний Артефакт'!") # Попросила DeepSeek придумать подписи

try:
    age = input("Введите ваш возраст (число): ")
    check_age(age)
    print(f"Возраст {age} принят! Добро пожаловать в Ларчию!")
except TypeError as te:
    print(f"Ошибка типа: {te}")
except ValueError as ve:
    print(f"Ошибка значения: {ve}")

print("ЗАДАНИЕ 6")
count_line = 0 # Счетчик строк
try:
    with open('data.txt', encoding='utf-8') as file:
        for line in file:
            count_line += 1
            # print(f"{count_line}) {line.strip()}")
        print(f"Всего в файле {count_line} строк")
except FileNotFoundError:
    print("Файл не найден!")
except Exception as e:
    print("Неизвестная ошибка:", e)
"""

""" Режимы открытия файлов:
'r'	Чтение (по умолчанию) //вроде должен просто читать, если не указано иное
'w'	Запись (перезаписывает файл)
'a'	Дозапись в конец файла
'x'	Создание файла (ошибка, если уже существует)
'b'	Бинарный режим (например, 'rb' для чтения изображений)
't'	Текстовый режим (по умолчанию)
'+'	Чтение + запись (например, 'r+')"""

print("ЗАДАНИЕ 7")















#print("Тестирую комит и пуш")


print('5.2 Модули')

print('Задание 1')
#Импорт модуля:
import mymodule
result = mymodule.hello("Диана")  # Вызываем функцию из модуля
print(result)  # Выводим результат

#Импорт конкретной функции:
from mymodule import hello
print(hello("Руслан"))

#Импорт с псевдонимом:
import mymodule as mm
print(mm.hello("Аннушка"))

print("Ура! Мой первый модуль!")
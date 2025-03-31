print('Картежи - tuple')
# Это неизм. набор элементов (неизм. тип данных). Сами элементы могут изменяться. Еще можно превратить его в список)

print('Задание 1')
cortej = (1,2,3,"four","five")
print(cortej[1],cortej[3])

print('Задание 2')
#cortej[1] = 3
print("При попытке поменять выдает: 'tuple' object does not support item assignment")

print('Задание 3')
list_vsp = list(cortej)
list_vsp.append(6)
print(tuple(list_vsp))

print('Задание 4')
cortej2 = "six",7,"eight"
cor = cortej + cortej2
print(cor)

print('Задание 5')
cor3 = cortej * 3
print(cor3)

print('Задание 6')
cort3 = 1, 2, 3
a, b, c = cort3
print("Три переменные:", a, b, c)


print('Задание 7')
cortej1 = 0,10,"20",30,40,50,"20"
elem = int(input("Введите элемент: "))
try:
    print(cortej1.index(elem))
except ValueError:
    print("Элемент не найден")
#Задача сложнее, чем кажется. Нужно понимать строки или числа ищем ("20" не найдет, а если убрать int - остальное мимо)

print('Задание 8')
znach = "20"
print("Заданный элемент встречается",cortej1.count(znach),"раз(-а)")

print('Задание 9')
new_list = [] # Сначала он лист
i = 0
while i < 4:
    new_list.append(cortej1[i])
    i += 1
new_cort = tuple(new_list)
print("Новый кортеж из первых 4 элементов:",new_cort)

print('Задание 10')
slovo = input("Введите строку (лучше слово): ")
my_tuple = tuple(slovo)
print("Теперь каждый символ строки стал элементом кортежа:",my_tuple)
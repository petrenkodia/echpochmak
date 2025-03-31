print('Списки - list') # Список - элементы какого-то типа (разных тоже) вместе. Это изменяемый тип данных.

print('Задание 1')
chetnye_elements = [elem for elem in range(1,11) if elem % 2 == 0]
print(chetnye_elements)
'''Списковые включения (list comprehensions) – это  синтаксис для создания списков в Python. 
Они позволяют создавать новые списки, применяя выражение к каждому элементу итерируемого объекта, и, при необходимости, 
фильтровать элементы с помощью условий. новый_список = [«операция» for «элемент списка» in «список» if "условие!"].'''
list1 = [elem for elem in range(1,11)]
list2 = []
for elem in list1:
   if elem % 2 == 0:
       list2.append(elem)
print(list2)

print('Задание 2')
list3 = [elem for elem in range(3,11)]
list4 = [elem for elem in range(6,15)]
#Способ 1 - множество (set) удаляет повторения, обозн. {}
print(list(set(list3+list4)))
#Способ 2 - поломать голову над циклом
list_sum = list3 + list4
list_new = []
for elem in list_sum:
    if elem not in list_new:
        list_new.append(elem)
print(list_new)

print('Задание 3')
#Пробуем функцией max
list_start = [elem for elem in range(3,11)]
maximum = max(list_start)
print("Максимальное число:",maximum,"Оно",list_start.index(maximum),"-е по порядку")
#Пробуем сортировкой (встроенная функция) и срезом (указали порядок элемента)
list_sort = sorted(list_start)
print('Максимальное число:',list_sort[-1],"Его порядковый номер:",list_start.index(list_sort[-1]))

print('Задание 4') #По аналогии переворот циклом, как с буквами в строке
list_str = [elem for elem in range(3,7)]
list_rev = []
for elem in list_str:
    i = [elem]
    list_rev = i + list_rev
print(list_rev)
# теперь срез и reverse()
print(list_str[::-1])
list_str.reverse()  # метод в самой переменной переворачивает порядок!!!
print(list_str)

print('Задание 5')
n = int(input("Введите целое число: "))
list_quad = [elem*elem for elem in range(1,(n+1))]
print(list_quad)

print('Задание 6')
sp_strok = ["Банан","Кукуруза","Морковь","Учпочмак","банан","Учпочмак"]
n = input("Введите искомую строку (например, Банан или Учпочмак): ")
num = sp_strok.count(n)
print("Строка встречается",num,"раз(а) - метод .count()")
#А теперь с помощью цикла, игнорируя регистр
numnum = 0
for elem in sp_strok:
    if elem.upper() == n.upper():
        numnum += 1
print("Без учета регистра строка встречается",numnum,"раз(а) - цикл for")

print('Задание 7')
sp_povt = ["Морковь","Банан","Морковь","Учпочмак","Учпочмак"]
sp_uniq = []
for elem in sp_povt:
    if elem not in sp_uniq:
        sp_uniq.append(elem)
print("Дан лист (список):",sp_povt,"\nТолько уникальные значения:",sp_uniq)

print('Задание 8')
svoy_spisok = [elem+1.7 for elem in range(3,11)] #Захотела такой список
new_spisok = []
for elem in svoy_spisok:
    new_spisok.append(round(elem/2,2))
print("Исходный список:",svoy_spisok)
print("Новый список:",new_spisok)
#но .round() не дает вывести 2 знака, если они оба 0 (типа .00). Нашла такое ("{:.2f}".format(), но это дичь):
new_spisok2 = []
for elem in new_spisok:
    new_spisok2.append("{:.2f}".format(float(elem)))
print("Новый список:",new_spisok2)
print("Тип элементов второго списка:",type(new_spisok2[1])) # почему-то вывел строку, хотя float (?)

print('Задание 9')
sp2 = ["Морковь","Банан","Кола","Учпочмак","Кефир"] #Да, я люблю еду
sp1 = [elem for elem in range(1,6)]
print("Попарный список кортежей (элементы с одним индексом из двух списков):",list(zip(sp1,sp2)))

print('Задание 10')
spisok_chisel = [int(elem-5) for elem in range(1,11)]
print("Исходный список:",spisok_chisel)

"""
Пыталась через цикл for и метод .remove, но при удалении элемента он пропускает проверку следующего((
Поэтому будем через while и метод .pop
for elem in spisok_chisel:
    if elem < 0:
        spisok_chisel.remove(elem)
print("Список без отрицат. чисел (ну, почти):",spisok_chisel)"""

i = 0 # нумерация с нуля
while i < len(spisok_chisel): # строго меньше из-за начала отсчета от нуля
    if spisok_chisel[i] < 0:
        spisok_chisel.pop(i) # "попаем" i-тый элемент, на его место встает другой
    else:
        i += 1 # если элемент удалять не надо - переходим к следующему
print("Скорректированный список без отрицат. чисел (через while и .pop):",spisok_chisel)

# В условии задачи нужно удалить из исходного, но проще создать новый список (вместо range был бы исходный)
print([elem for elem in range(-5,6) if elem >= 0])
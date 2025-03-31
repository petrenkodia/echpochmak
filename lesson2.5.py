print('Задание 1')
slovo = "Python"
first_tri = slovo[:3]
last_tri = slovo[-3:]
not_first_not_last_kek = slovo[1:-1]
print('Итог:',first_tri,last_tri,not_first_not_last_kek)

print('Задание 2')
slovo1 = "Programming"
reverse = slovo1[::-1]
print('Итог:',reverse)

print('Задание 3')
sentence = "Hello, world!"
every_second = sentence[::2]
print('Итог:',every_second)

print('Задание 4')
sentence1 = "Python is awesome!"
print('Итог:',sentence1[2:-2]) #Удалила 2 перв. (нумер. с 0) и 2 послед. симв. (-2 т.к. не вкл.)

print('Задание 5')
sent1 = "Python is awesome!"
print('Итог: '+sent1[0]+sent1[-1])

print('Задание 6')
sent2 = "Python"
print(sent2[0]+sent2[1:].upper()) #Первая буква отдельно

print('Задание 7')
sent3 = "code"
print(sent3*3) #Не поняла, как тут применить срезы (?)

print('Задание 8')
sent4 = "Learning Python is fun!"
print(sent4.find("Python")) #Индекс первого вхождения, считает с 0

#есть еще метод replace(old, new, num): параметр num показывает, сколько вхождений подстроки old требуется заменить на new.
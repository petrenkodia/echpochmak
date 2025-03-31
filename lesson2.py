import random

print('Задание 1.1')
number = input("Введите число: ")
if(float(number) > 0):
    print('Число положительное')
elif(float(number) < 0):
    print('Число отрицательное')
else:
    print('Число равно нулю')

print('Задание 1.2')
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
if(number1 > number2):
    print('Вот наибольшее число: ',number1)
elif(number1 < number2):
    print('Вот наибольшее число: ',number2)
else:
    print('Числа равны')

print('Задание 1.3')
num = int(input("Введите натуральнео число: "))
if(num % 2 == 0):
    print('Число четное') #Т.к. остаток равен нулю
else:
    print('Число нечетное')

print('Задание 2.1')
for i in range(1, 11): #Сделала только до 10
    print(i)
    i += 1

print('Задание 2.2')
j = 1
while j <= 50:
    if(j%11==0): #Сделала кратно 11
        print(j)
    j += 1

print('Задание 2.3')
digit = input("Введите целое число для создания таблицы: ")
k = 1
while k <= 10:
    print(f"{digit} * {k} = {int(digit) * k}")
    k += 1

print('Задание 3.1')
""" Вариант, как сделать без функции с помощью циклов и чтобы я поняла: """

chislo = int(input("Введите целое число (для проверки): "))
eazypeazy = "- простое число"
ochen_slozhna = "- не простое число"
if(chislo <= 0):
    print(chislo, ochen_slozhna)
elif(chislo >= 1 and chislo <= 3):
    print(chislo, eazypeazy)
else:
    status = eazypeazy #Пока не найдены делители - простое
    for i in range(2,chislo): #Ищем делители от 2 до пред. числа (можно до корня+1, но там нужна библиотека math)
        if chislo % i == 0:
            status = ochen_slozhna
            break #Если нашли делитель - вышли из цикла, но мы все еще в else
    print(chislo, status)

print('Задание 3.2') #Изи, надеюсь, верно
numnum = int(input("Введите натуральное число (для вычисления факториала): "))
fucktorial = 1 #Если 0 (или вдруг отриц. число)
for i in range(1,numnum + 1):
    fucktorial = fucktorial * i
print(fucktorial)

print('Задание 3.3')
stroka = input("Введите строку, плиз: ")
akorts = stroka[::-1]
print("Перевернутая строка:",akorts)

stroka1 = input("А теперь снова для переворота циклом: ")
akorts1 = ""
for symbol in stroka1:
    akorts1 = symbol + akorts1
print("Перевернутая циклом строка:",akorts1)

print('Задание 4')
rand_num = random.randint(1,100) #Тут целое число с 1 по 100 включительно
user_num = int(input("Попробуй угадать натуральное число от 1 до 100: "))
while (rand_num != user_num):
    if (rand_num > user_num):
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
    user_num = int(input("Попробуй снова угадать или нажми ноль, чтобы выйти: ")) #Добавила выход
    if (user_num == 0):
        print("Ответ:",rand_num,'\nНичего, в следующий раз угадаешь!')
        break
if (user_num != 0):
    print("Поздравляю! Ты - медиум экстрасекс!!")
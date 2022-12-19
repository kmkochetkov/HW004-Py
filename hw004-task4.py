# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл (или вывести в терминал) многочлен степени k.
#
# Пример:
#
# - k = 2  => 2*x² + 4*x + 5
# - k = 3  => 41*x^3 + 6*x² + 2*x + 98

# Использование метода "randint" из модуля "random"
from random import randint
k = int(input('Введите степень к: '))

# Файл с результатом выполнения открывается для добавления
file = open('hw004-task4_1.txt','a+')

# Формирование многочлена с убыванием коэффициентов от "k" до 0
for i in range (k, 0, -1):
    member = randint(1, 100)
    if member == 0:
        continue
    elif member ==1:
        member = ''
    else:
        member = f'{member}*x^{i}+' if i != 1 else f'{member}*x+'
    print(member, end='',file=file)
# Запись последнего элемента и элементов равенства
print(f'{randint(1,101)}=0',file=file)
file.close()


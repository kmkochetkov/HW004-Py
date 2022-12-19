# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.(Вывод тех элементов, которые были без повторов)
#
# Ввод: 1 2 3 2 4 4
# Вывод: 1 3

# Начальные данные
sequence = [1, 2, 3, 2, 4, 4]
result = []

# Вложенные циклы для поиска повторяющихся элементов
for i in range(len(sequence)):
    tempSum = 0
    for j in range(len(sequence)):
        if sequence[i] == sequence[j]:
            tempSum +=1
    if tempSum == 1:
        result.append(sequence[i])
print("Начальная последовательность:",sequence)
print("Неповторяющиеся элементы",result)

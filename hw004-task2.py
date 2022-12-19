# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#
# 24
# 2 2 2 3


number = int(input("Введите число: "))

# Функция factor факторизует введённное число
def factor (n):
    fact = list()
    divider = 2
    while (divider <= n):
        if (n% divider) == 0:
            fact.append(divider)
            n = n/divider
        else:
            divider += 1
    return fact

print(factor(number))
# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))


def recSum(a, b):
    if b == 0:
        return a
    return 1 + recSum(a, b - 1)


print(recSum(a, b))

"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75 # -0.375

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть  без создания массива!
"""


def series_numbers(n, count=0, beginning=-0.5, res=0):
    res += beginning
    count += 1
    if n == count:
        return res
    else:
        return series_numbers(n, count, beginning / 2 * -1, res)


print(series_numbers(3))

"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Нужно обойтисть без создания массива!
"""


def recurs_row_sum(count, summ=1.0):
    if count <= 1:
        return summ
    summ += recurs_row_sum(count - 1, -summ / 2)
    return summ


print(f'{recurs_row_sum(3)=}')

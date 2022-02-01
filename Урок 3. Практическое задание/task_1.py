"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""


from time import time


def time_check(func):
    """Функция-декоратор для замера времени выполенения функции"""

    def wrapper(*args):
        start_t = time()
        func(*args)
        end_t = time()
        return end_t - start_t

    return wrapper


my_lst = []
my_dict = dict()


# a)

@time_check
def complete_the_list(n):
    for i in range(n):  # O(n)
        my_lst.append(i)  # O(1)


@time_check
def complete_the_dict(n):
    for i in range(n):  # O(n)
        my_dict[i] = i  # O(1)


print('Время на заполнение списка -', complete_the_list(10000000))
print('Время на заполнение словаря -', complete_the_dict(10000000))

"""
Время на заполнение списка - 0.9687204360961914
Время на заполнение словаря - 1.0312185287475586
Словарь реализуеться дольше так как использует хэш-таблицы(Ключ-значение)
Но если запускать несколько раз , время меняеться и иногда словарь быстрее
"""


# b)
@time_check
def dict_del(n):
    return my_dict.pop(n)           # O(1)


@time_check
def lst_del(n):
    return my_lst.pop(n)            # O(n)


@time_check
def lst_change():
    for i in range(len(my_lst)):    # O(n)
        my_lst[i] = 100             # O(n)
    return


@time_check
def dict_change():
    for i in my_dict.keys():        # O(n)
        my_dict[i] = 100            # O(1)
    return


print('Время на удаление элемента из списка -', lst_del(9999999))
print('Время на удаление элемента из словаря -', dict_del(999999))
print('Время на изменение элемента из списка -', lst_change())
print('Время на изменение элемента из словаря -', dict_change())


"""
Время на удаление элемента из списка - 0.0
Время на удаление элемента из словаря - 0.0
Время на изменение элемента из списка - 0.6249809265136719
Время на изменение элемента из словаря - 0.6249828338623047
По сути ,изменение в словаре должно быть быстрее , так как поиск идет по хэшу. 
Но у меня почему то наоборот.
"""
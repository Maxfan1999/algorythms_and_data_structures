"""
Знайдіть кількість входжень заданого числа x до впорядкованого за неспаданням масиву цілих чисел array
"""


def bsearch_leftmost(array, x):
    """ кількість входжень заданого числа.
    :param array: Масив цілих чисел впорядкований за неспаданням
    :param x:     Шуканий елемент
    :return:      Кількість входжень
    """
    # TODO: Реалізуйте алгоритм тут.
    l, r = 0, len(array)
    while l < r:
        m = l + (r - l) // 2
        if x > array[m]:
            l = m + 1
        else:
            r = m
    return l
            
def bsearch_rightmost(array, x):
    """ кількість входжень заданого числа.
    :param array: Масив цілих чисел впорядкований за неспаданням
    :param x:     Шуканий елемент
    :return:      Кількість входжень
    """
    # TODO: Реалізуйте алгоритм тут.
    l, r = 0, len(array)
    while l < r:
        m = l + (r - l) // 2
        if x >= array[m]:
            l = m + 1
        else:
            r = m
    return l - 1

def counter(array, x):
    left = bsearch_leftmost(array, x)
    if left == -1:
        return left
    else:
        return bsearch_rightmost(array, x) - left + 1

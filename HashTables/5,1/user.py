"""
Реалізуйте інтерфей асоційованого масиву, ключами якого є цілі числа, а значеннями - рядки.
"""
from hashtable import HashTable

table = None


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global table
    table = HashTable(size=3571)


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    global table
    #print(table.data)
    table.put(key, value)


def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """
    global table
    #print(table.data)
    table.get(key)


def delete(key: int) -> None:
    """ Видаляє пару ключ-значення за заданим ключем.
    Якщо ключ у структурі відсутній - нічого не робить.
    :param key: Ключ
    """
    global table
    #print(table.data)
    table.delete(key)

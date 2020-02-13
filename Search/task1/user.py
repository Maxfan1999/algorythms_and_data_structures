"""
Реалізуйте інтерфейс для роботи з англійсько-українським словником та швидким пошуком перекладу.
"""
dictionary = []

def addTranslation(eng, translation):
    """ Додає до словника англійське слово та його переклад.
    Пари (eng, translation) приходяться у порядку, що відповідає лексикографічному порядку.

    :param eng: англійське слово
    :param translation: переклад
    """
    dictionary.append((eng, translation))
    return True


def find(eng):
    """ Повертає переклад слова зі словника.
    :param eng: англійське слово
    :return: переклад слова, якщо воно міститься у словнику, або порожній рядок у іншому разі.
    """
    l, r = 0, len(dictionary) - 1
    while l < r:
        m = l + (r - l) // 2
        if eng == dictionary[m][0]:
            return dictionary[m][1]
        elif eng > dictionary[m][0]:
            l = m + 1
        else:
            r = m - 1
    if eng == dictionary[l][0]:
        return dictionary[l][1]
    else:
        return ""
    


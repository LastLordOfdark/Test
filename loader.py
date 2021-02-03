"""
Загрузка данных
"""


def load_from_input() -> list:
    """Получение данных через input
    :return: список несортированных данных
    """

    while True:
        try:
            raw_list = input('ВВедите числа разделенные пробелом:')
            result = _str_to_int_list(raw_list)
        except ValueError:
            print('Вы ввели неправильное число')
        else:
            return result


def _str_to_int_list(raw_list):
    return [int(i) for i in raw_list.split()]


def load_from_file(filename: str) -> list:
    """
    Получение данных через из файлов
    :param filename: имя файла
    :return список несортированных данных
    """
    with open(filename) as file:
        raw_list = file.read()
    result = _str_to_int_list(raw_list)
    return result

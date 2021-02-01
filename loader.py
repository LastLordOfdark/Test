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
            result = [int(i) for i in raw_list.split()]
        except ValueError:
            print('Вы ввели неправильное число')
        else:
            return result



def  load_from_file() -> list:
    """Получение данных через input
    :return: список несортированных данных
    """

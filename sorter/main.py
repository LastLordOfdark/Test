"""
Главный модуль программы
Точка старта
"""
from sorter import loader, sorting
import click


BUBBLE = 'b'
INSERT = 'i'
SELECTION = 's'

"""
source, filename = parse_cmd()
if source == KEYBOARD:
    unsorted_data = load_from_input()
else:
    unsorted_data = load_from_file(filename)
"""


@click.command()
@click.option('--filename', default=None,
              help='Имя файла с несортированными данными')
@click.option('--algorithm', default=BUBBLE,
              help='Алгоритм сортировки.')
def sorter(filename, algorithm, sorted_data=None):
    """ Простая утилита для сортировки чисел"""
    print(filename, algorithm)
    if filename is None:
        unsorted_data = loader.load_from_input()
    else:
        unsorted_data = loader.load_from_file(filename)
    print(unsorted_data)

    allowed_algorithms = [BUBBLE, INSERT, SELECTION]
    if algorithm not in [BUBBLE, INSERT, SELECTION]:
        print('Неправильно введено имя алгоритма')
        print('Правильные варианты:', allowed_algorithms)
        exit(1)

    if algorithm == BUBBLE:
        sorted_data = sorting.bubble_sort(unsorted_data)
    elif algorithm == INSERT:
        sorted_data = sorting.insert_sort(unsorted_data)
    elif algorithm == SELECTION:
        sorted_data = sorting.selection_sort(unsorted_data)

    print('Несортированный массив:  ', *unsorted_data)
    print('Сортированный массив:  ', *sorted_data)


if __name__ == '__main__':
    sorter()

# Абс. путь - путь до файла, который указывает расположение файла с любого каталога файловой системы.
# Относительный путь - путь до файла, который указывает расположение файла относительно текущего каталога.

import os

def factorial(number: int):
    if number == 1:
        return number
    return number * factorial(number-1)

current_path = os.path.abspath(__file__)
parent_path = os.path.join(current_path, '..')
parent_parent_path = os.path.join(parent_path, '..')

def get_all_paths(path, filename=None):
    for i_file in os.listdir(path):
        new_path = os.path.join(path, i_file)
        if os.path.isdir(new_path) and i_file != 'venv':
            new_file = open(i_file, 'a', encoding='utf-8')
            new_file.close()
            print('Директория -- > ', new_path)
            get_all_paths(new_path)
        else:
            if filename:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(i_file)
            print('\t -', new_path)

get_all_paths(parent_parent_path)
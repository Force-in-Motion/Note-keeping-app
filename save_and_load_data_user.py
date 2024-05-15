import os
import csv


def check_app():
    path = os.environ.get('LOCALAPPDATA') + r'\Notes User'

    if not os.path.isdir(path):
        os.mkdir(path)
    return path


path = check_app()

def check_file() -> bool:
    """
    Проверяет наличие файла txt по указанному пути, в данном случае в папке
    :return: True или False
    """
    file = path + r'\notes.txt'
    if os.path.isfile(file):
        return True
    else:
        return False


def check_len_file() -> bool:
    """
    Проверяет наличие данных в файле txt
    :return: True или False
    """
    matrix = load_data()
    if len(matrix) != 0:
        return True
    else:
        return False


def read_data_in_file():
    """
    Считывает файл txt с данными и записывает все данные файла в переменную
    :return: Возвращает все данные файла
    """
    file = open(path + r'\notes.txt', 'r', encoding='utf-8')
    data_notes_from_file = file.read().split('\n')
    file.close()
    return data_notes_from_file


def rewrite_data_in_file(write_data: str):
    """
    Перезаписывает имеющийся файл txt, если файл отсутствует, то создает его
    :param write_data: Пренимает данные для записи
    :return:
    """
    file = open(path + r'\notes.txt', 'w', encoding='utf-8')
    file.write(f'\n{write_data}')
    file.close()


def add_data_in_file(write_data: str):
    """
    Добавляет данные в файл txt
    :param write_data: Пренимает данные для записи
    :return:
    """
    file = open(path + r'\notes.txt', 'a', encoding='utf-8')
    file.write(f'\n{write_data}')
    file.close()

def write_data_in_file(write_data: str):
    """
    Дозаписывает полученные данные в файл txt если он существует, либо создает файл txt если его нет и записывает туда данные, каждый раз полученные данные пишутся на новой строке
    :param write_data: Пренимает данные в виде строки
    :return:
    """
    try:
        add_data_in_file(write_data)

    except:
        rewrite_data_in_file(write_data)


def write_data_in_csv(write_data: list[list]):
    """
    Записывает полученные данные в файл в csv формате
    :param write_data:
    :return:
    """
    file = open(path + r'\notes.csv', 'w', newline='')
    writer = csv.writer(file)
    writer.writerows(write_data)
    file.close()



def load_data() -> list[list]:
    """
    Вызывает внутри себя функцию, которая считывает данные из файла и обрабатывает, затем зоздает матрицу заметок, каждый вложенный список матрицы = 1 заметка со всеми ее элементами
    :return: Возвращает матрицу заметок
    """
    data_notes_from_file = read_data_in_file()

    matrix_note = []

    for i in range(0, len(data_notes_from_file), 1):
        if data_notes_from_file[i] != '':
            matrix_note.append(data_notes_from_file[i].split('<{@}>'))

    return matrix_note



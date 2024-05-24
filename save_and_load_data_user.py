import os
import csv



def create_folder():
    if not os.path.isdir(path):
        os.mkdir(path)


def check_file():
    """
    Проверяет наличие файла txt по указанному пути, в данном случае в папке
    :return: True или False
    """
    file = path + r'\notes.txt'
    if os.path.isfile(file):
        return True
    else:
        return False


def check_len_file(matrix_notes):
    """
    Проверяет наличие данных в файле txt
    :return: True или False
    """
    if len(matrix_notes) != 0:
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


def write_data_in_csv(write_data: list[list]):
    """
    Записывает полученные данные в файл в csv формате
    :param write_data:
    :return:
    """
    file = open(path_csv + r'\notes.csv', 'w', newline='')
    writer = csv.writer(file)
    writer.writerows(write_data)
    file.close()


def transforms_matrix_in_str():
    """
    Обходит все списки матрицы и разделяет их элементы служебным символом, затем разделяет списки матрицы "\n"
    :param matrix_notes: Пренимает матрицу элементов
    :return: Возвращает строку, готовыю к записи в файл
    """
    for i in range(0, len(matrix_notes), 1):
        matrix_notes[i] = '<{@}>'.join(matrix_notes[i])
    write_data = '\n'.join(matrix_notes)

    return write_data


def load_data():
    """
    Вызывает внутри себя создает папку, выполняет проверки на существование файла в папке и на то, что он не пустой, затем зоздает матрицу заметок, каждый вложенный список матрицы = 1 заметка со всеми ее элементами
    :return: None
    """
    create_folder()

    if not check_file(): return

    data_notes_from_file = read_data_in_file()

    if not check_len_file(data_notes_from_file): return

    for i in range(0, len(data_notes_from_file), 1):
        if data_notes_from_file[i] != '':
            matrix_notes.append(data_notes_from_file[i].split('<{@}>'))


def save_data():
    """
    Сохнаняет данные в тхт файл
    :return:
    """
    write_data = transforms_matrix_in_str()

    file = open(path + r'\notes.txt', 'w', encoding='utf-8')

    file.write(f'\n{write_data}')

    file.close()


path = os.environ.get('LOCALAPPDATA') + r'\Notes User'
path_csv = os.path.expanduser('~') + r'\Desktop'
matrix_notes = []

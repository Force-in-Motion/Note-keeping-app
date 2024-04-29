

def read_data_in_file():
    """
    Считывает файл с данными и записывает все данные файла в переменную
    :return: Возвращает все данные файла
    """
    file = open('notes.txt', 'r', encoding='utf-8')
    data_notes_from_file = file.read().split('\n')
    file.close()
    return data_notes_from_file


def write_data_in_file(write_data: str):
    """
    Дозаписывает полученные данные в файл если он существует, либо создает файл если его нет и записывает туда данные, каждый раз полученные данные пишутся на новой строке
    :param write_data: Пренимает данные в виде строки
    :return:
    """
    try:
        file = open('notes.txt', 'a', encoding='utf-8')
        file.write(f'\n{write_data}')
        file.close()

    except:
        file = open('notes.txt', 'w', encoding='utf-8')
        file.write(f'\n{write_data}')
        file.close()


def new_data_write_in_file(write_data: str):
    """
    Перезаписывает все заметки в файле после удаления искомой заметки
    :param write_data: Пренимает данные в виде строки и разбивает их по "\n"
    :return:
    """
    file = open('notes.txt', 'w', encoding='utf-8')
    file.write(f'\n{write_data}')
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


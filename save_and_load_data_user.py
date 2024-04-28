

def read_data_in_file():
    """
    Считывает файл с данными и записывает все данные файла в переменную
    :return: Возвращает все данные файла
    """
    file = open('notes.txt', 'r')
    data_file = file.read()
    file.close()
    return data_file



def write_data_in_file(write_data):
    file = open('notes.txt', 'w')
    file.write(write_data)
    file.close()
    return True



def load():
    pass
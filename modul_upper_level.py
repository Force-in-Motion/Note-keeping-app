import modul_lower_level
import GUI
import save_and_load_data_user




def create_note():
    data_set_notes = create_matrix_data()
    lst_data_note = create_lst_data_note(data_set_notes)
    save_and_load_data_user.write_data_in_file(lst_data_note)
    return True



def create_matrix_data():
    """
    Создает матрицу вложенных списков, каждый список содержит все данные заметки
    :param lst: Пренимает список, содержащий все данные заметки, введеные пользователем
    :return: Матрицу заметок
    """
    data_set_notes = []
    while True:
        data_set_notes.append([])
        name_note = GUI.input_data('Введите название заметки >> ')
        if not modul_lower_level.checks_input_for_empty_str(name_note):
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue
        else:
            data_set_notes[-1].append(name_note)

        importance = GUI.input_data('Укажите важность заметки >> ')
        if not modul_lower_level.checks_input_for_empty_str(importance):
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue
        else:
            data_set_notes[-1].append(importance)

        text_note = GUI.input_data('Введите текст заметки >> ')
        if not modul_lower_level.checks_input_for_empty_str(text_note):
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue
        else:
            data_set_notes[-1].append(text_note)

        return data_set_notes




def create_lst_data_note(data_set_notes: list[list]) -> str:
    """
    Преобразует все данные матрицы заметок, в один список строк с указанным разделителем, затем разбивает по '\n' общий список строк, чтобы в каждой строке была одна заметка
    :param data_set_notes: возвращает все данные каждой заметки в виде строк разбитые по '\n'
    :return:
    """
    lst_data_note = []
    for i in data_set_notes:
        lst_data_note.append('<{@}>'.join(i))
    write_data = '\n'.join(lst_data_note)
    return write_data



def search_note_by_name():
    pass

def search_set_notes():
    pass

def read_and_output_notes():
    pass


def delete_note():
    pass


def edits_note():
    pass


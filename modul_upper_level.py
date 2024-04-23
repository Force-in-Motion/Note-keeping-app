import modul_lower_level
import GUI


def create_note():
    """
    Создает матрицу вложенных списков, каждый список содержит все данные заметки
    :param lst: Пренимает список, содержащий все данные заметки, введеные пользователем
    :return: Матрицу заметок
    """
    data_set_notes = []
    while True:
        data_set_notes.append([])
        while True:
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


            text_note = GUI.input_data('Введите текст заметки')
            if not modul_lower_level.checks_input_for_empty_str(text_note):
                GUI.output_data(GUI.output_data_message['empty_note'])
                continue
            else:
                data_set_notes[-1].append(text_note)


            return data_set_notes


def search_note_by_name():
    pass


def read_and_output_notes():
    pass


def delete_note():
    pass


def edits_note():
    pass


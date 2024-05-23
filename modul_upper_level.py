import GUI
import modul_lower_level as ml
import save_and_load_data_user as sld
from save_and_load_data_user import matrix_notes

def create_note():
    """
    Создает заметку пользователя и записывает ее в файл или выкидывает исключение
    :return: True или False
    """
    try:
        lst_data_note = ml.create_lst_data_note()

        if lst_data_note == 'back':
            GUI.output_data(GUI.output_data_message['back_menu'])
            return

        matrix_notes.append(lst_data_note)

        GUI.output_data(GUI.output_data_message['save'])

    except:

        GUI.output_data(GUI.output_data_message['err_save'])
        return


def search_all_notes():
    """
    Выводит в консоль все заметки по запросу пользователя если они существуют или выкидывает исключение
    :return:
    """

    if not matrix_notes:
        GUI.output_data(GUI.output_data_message['err_file'])
        return

    GUI.print_all_notes(matrix_notes)

    GUI.output_data(GUI.output_data_message['open_note'])

    open_note = ml.search_note_in_matrix_data()

    if open_note == 'back':
        GUI.output_data(GUI.output_data_message['back_menu'])
        return
    else:
        GUI.print_open_note(open_note)



def search_notes_by_input_data():
    """
    Выполняет поиск искомой заметки если она существует или выкидывает исключение
    :return: Возвращает искомую заметку
    """
    if not matrix_notes:
        GUI.output_data(GUI.output_data_message['err_file'])
        return

    matrix_search_notes = ml.check_input_data_and_return_new_matrix_notes()

    if matrix_search_notes == 'back':
        GUI.output_data(GUI.output_data_message['back_menu'])
        return
    else:
        GUI.print_elems_matrix_notes(matrix_search_notes)


def sorted_notes():
    """
    Сортирует заметки по названию, дате создания или по важности или выкидывает исключение
    :return:
    """
    if not matrix_notes:
        GUI.output_data(GUI.output_data_message['err_file'])
        return

    GUI.output_data(GUI.output_data_message['sort_menu'])

    set_notes = ml.sorted_notes_by_input_data()
    if set_notes == 'back':
        GUI.output_data(GUI.output_data_message['back_menu'])
        return



def delete_note():
    """
    Выполняет удаление искомой заметки если она существует или выкидывает исключение
    :return: True или False
    """
    try:
        if not matrix_notes:
            GUI.output_data(GUI.output_data_message['err_file'])
            return

        del_note = ml.search_note_in_matrix_data()

        if del_note == 'back':
            GUI.output_data(GUI.output_data_message['back_menu'])
            return

        ml.dell_note_in_matrix_data(del_note, matrix_notes)

        GUI.output_data(GUI.output_data_message['del'])

    except:

        GUI.output_data(GUI.output_data_message['err_del'])
        return


def edits_note():
    """
    Редактирует заметку пользователя если она существует или выкидывает исключение
    :return:
    """
    try:
        if not matrix_notes:
            GUI.output_data(GUI.output_data_message['err_file'])
            return

        search_note = ml.search_note_in_matrix_data()

        GUI.output_data(GUI.output_data_message['edit_menu'])

        if search_note == 'back':
            GUI.output_data(GUI.output_data_message['back_menu'])
            return

        matrix_with_edited_lst = ml.create_edited_matrix_note(search_note, matrix_notes)

        if matrix_with_edited_lst == 'back':
            GUI.output_data(GUI.output_data_message['back_menu'])
            return

        GUI.output_data(GUI.output_data_message['edited'])

    except:
        GUI.output_data(GUI.output_data_message['err_edit'])
        return


def unloads_csv_file():
    """
    Выгружает имеющиеся заметки в csv файл если они имеются, либо выдает ошибку если заметки отсутствуют
    :return:
    """
    try:
        if not matrix_notes:
            GUI.output_data(GUI.output_data_message['err_file'])
            return

        sld.write_data_in_csv(matrix_notes)

        GUI.output_data(GUI.output_data_message['csv'])

    except:
        GUI.output_data(GUI.output_data_message['err_csv'])
        return

import modul_lower_level
import GUI
import save_and_load_data_user




def create_note():
    """
    Создает заметку пользователя и записывает ее в файл
    :return: True или False
    """
    try:
        lst_data_note = modul_lower_level.create_lst_data_note()

        write_data = modul_lower_level.create_write_data(lst_data_note)

        save_and_load_data_user.write_data_in_file(write_data)

        GUI.output_data(GUI.output_data_message['save'])

    except:

        GUI.output_data(GUI.output_data_message['err_save'])





def search_all_notes():
    try:
        matrix_note = save_and_load_data_user.load_data()
        GUI.print_all_notes(matrix_note)
    except:
        GUI.output_data(GUI.output_data_message['err_file'])



def search_note_by_name():
    """
    Выполняет поиск искомой заметки
    :return: Возвращает искомую заметку
    """
    try:
        matrix_note = save_and_load_data_user.load_data()

        search_note = modul_lower_level.search_note_in_matrix_data(matrix_note)

        return search_note
    except:
        GUI.output_data(GUI.output_data_message['err_search_output'])


def delete_note():
    """
    Выполняет удаление искомой заметки
    :return: True или False
    """
    try:
        matrix_note = save_and_load_data_user.load_data()

        del_note = modul_lower_level.search_note_in_matrix_data(matrix_note)

        matrix_with_del_lst = modul_lower_level.dell_note_in_matrix_data(del_note, matrix_note)

        write_data = modul_lower_level.transforms_matrix_in_str(matrix_with_del_lst)

        save_and_load_data_user.rewrite_data_in_file(write_data)

        GUI.output_data(GUI.output_data_message['del'])

    except:

        GUI.output_data(GUI.output_data_message['err_del'])




def edits_note():
    try:
        if not save_and_load_data_user.check_len_file():
            GUI.output_data(GUI.output_data_message['err_file'])
            return
        GUI.output_data(GUI.output_data_message['edit_menu'])

        matrix_note = save_and_load_data_user.load_data()

        search_note = modul_lower_level.search_note_in_matrix_data(matrix_note)

        matrix_with_edited_lst = modul_lower_level.create_edited_matrix_note(search_note, matrix_note)

        write_data = modul_lower_level.transforms_matrix_in_str(matrix_with_edited_lst)

        save_and_load_data_user.rewrite_data_in_file(write_data)

        GUI.output_data(GUI.output_data_message['edited'])

    except:

        GUI.output_data(GUI.output_data_message['err_edit'])


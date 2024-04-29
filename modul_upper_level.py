import modul_lower_level
import GUI
import save_and_load_data_user




def create_note():
    """
    Создает заметку пользователя и записывает ее в файл
    :return: True
    """
    try:
        lst_data_note = modul_lower_level.create_lst_data_note()

        write_data = modul_lower_level.create_write_data(lst_data_note)

        save_and_load_data_user.write_data_in_file(write_data)

        GUI.output_data(GUI.output_data_message['save'])
        return True

    except Exception as e:

        GUI.output_data(GUI.output_data_message['err_save'])
        return False


def search_note_by_name():
        matrix_note = save_and_load_data_user.load_data()

        search_note = modul_lower_level.search_note_in_matrix_data(matrix_note)

        return search_note


def delete_note():
    try:
        matrix_note = save_and_load_data_user.load_data()

        del_note = modul_lower_level.search_note_in_matrix_data(matrix_note)

        matrix_with_del_lst = modul_lower_level.dell_note_in_matrix_data(del_note, matrix_note)

        write_data = modul_lower_level.transforms_matrix_in_str(matrix_with_del_lst)

        save_and_load_data_user.new_data_write_in_file(write_data)

        return True
    except Exception as e:

        GUI.output_data(GUI.output_data_message['err_del'])
        return False



def edits_note(edits_note, matrix_note):
    pass




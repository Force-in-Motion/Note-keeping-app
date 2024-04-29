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


def search_note_by_name(): # Реализовать остановку программы 'stop'
        matrix_note = save_and_load_data_user.load_data()

        search_note = modul_lower_level.search_data(matrix_note)

        return search_note


def delete_note():
    try:
        matrix_note = save_and_load_data_user.load_data()
        print(matrix_note)
        del_note = modul_lower_level.search_data(matrix_note)
        print(del_note)
        del del_note

        return True
    except Exception as e:
        GUI.output_data(GUI.output_data_message['err_del'])


def edits_note(edits_note, matrix_note):
    pass




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
    while True:
        search_note = GUI.input_data(GUI.output_data_message['srch_note'])

        if search_note == 'stop':
            return
        if modul_lower_level.checks_input_for_empty_str(search_note):
            flag = True
            for i in range(0, len(matrix_note), 1):
                for j in range(0, len(matrix_note[i]), 1):
                    if search_note in matrix_note[i][j]:
                        search_note = matrix_note[i]
                        flag = True
                        return search_note
            if not flag:
                GUI.output_data(GUI.output_data_message['err_search'])
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])







def read_and_output_notes():
    pass


def delete_note(del_note, matrix_note):
    pass


def edits_note(edits_note, matrix_note):
    pass




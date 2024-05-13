import modul_lower_level
import GUI
import save_and_load_data_user

def create_note():
    """
    Создает заметку пользователя и записывает ее в файл или выкидывает исключение
    :return: True или False
    """
    try:
        lst_data_note = modul_lower_level.create_lst_data_note()
        if lst_data_note == 'back':
            GUI.output_data(GUI.output_data_message['back_menu'])
            return

        write_data = modul_lower_level.create_write_data(lst_data_note)

        save_and_load_data_user.write_data_in_file(write_data)

        GUI.output_data(GUI.output_data_message['save'])

    except:

        GUI.output_data(GUI.output_data_message['err_save'])


def search_all_notes():
    """
    Выводит в консоль все заметки по запросу пользователя если они существуют или выкидывает исключение
    :return:
    """
    try:
        if not save_and_load_data_user.check_len_file():
            GUI.output_data(GUI.output_data_message['err_file'])
            return
        matrix_note = save_and_load_data_user.load_data()

        GUI.print_all_notes(matrix_note)
    except:
        GUI.output_data(GUI.output_data_message['err_file'])


def search_note_by_name():
    """
    Выполняет поиск искомой заметки если она существует или выкидывает исключение
    :return: Возвращает искомую заметку
    """
    if not save_and_load_data_user.check_file():
        GUI.output_data(GUI.output_data_message['err_file'])
        return
    if not save_and_load_data_user.check_len_file():
        GUI.output_data(GUI.output_data_message['err_file'])
        return
    matrix_note = save_and_load_data_user.load_data()

    search_note = modul_lower_level.search_note_in_matrix_data(matrix_note)
    if search_note == 'back':
        GUI.output_data(GUI.output_data_message['back_menu'])
        return
    else:
        GUI.print_search_note(search_note)


def sorted_notes():
    """
    Сортирует заметки по названию, дате создания или по важности
    :return:
    """
    try:
        if not save_and_load_data_user.check_file():
            GUI.output_data(GUI.output_data_message['err_file'])
            return

        if not save_and_load_data_user.check_len_file():
            GUI.output_data(GUI.output_data_message['err_file'])
            return
        matrix_note = save_and_load_data_user.load_data()

        GUI.output_data(GUI.output_data_message['sort_menu'])

        set_notes = modul_lower_level.sorted_notes_by_input_data(matrix_note)
        if set_notes == 'back':
            GUI.output_data(GUI.output_data_message['back_menu'])
            return

    except:
        GUI.output_data(GUI.output_data_message['err_sort'])



def delete_note():
    """
    Выполняет удаление искомой заметки если она существует или выкидывает исключение
    :return: True или False
    """
    try:
        if not save_and_load_data_user.check_file():
            GUI.output_data(GUI.output_data_message['err_file'])
            return
        if not save_and_load_data_user.check_len_file():
            GUI.output_data(GUI.output_data_message['err_file'])
            return
        matrix_note = save_and_load_data_user.load_data()

        del_note = modul_lower_level.search_note_in_matrix_data(matrix_note)

        matrix_with_del_lst = modul_lower_level.dell_note_in_matrix_data(del_note, matrix_note)

        write_data = modul_lower_level.transforms_matrix_in_str(matrix_with_del_lst)

        save_and_load_data_user.rewrite_data_in_file(write_data)

        GUI.output_data(GUI.output_data_message['del'])

    except:

        GUI.output_data(GUI.output_data_message['err_del'])


def edits_note():
    """
    Редактирует заметку пользователя если она существует или выкидывает исключение
    :return:
    """
    try:
        if not save_and_load_data_user.check_file():
            GUI.output_data(GUI.output_data_message['err_file'])
            return

        if not save_and_load_data_user.check_len_file():
            GUI.output_data(GUI.output_data_message['err_file'])
            return

        GUI.output_data(GUI.output_data_message['edit_menu'])

        matrix_note = save_and_load_data_user.load_data()

        search_note = modul_lower_level.search_note_in_matrix_data(matrix_note)

        if search_note == 'back':
            GUI.output_data(GUI.output_data_message['back_menu'])
            return

        matrix_with_edited_lst = modul_lower_level.create_edited_matrix_note(search_note, matrix_note)

        if matrix_with_edited_lst == 'back':
            GUI.output_data(GUI.output_data_message['back_menu'])
            return

        write_data = modul_lower_level.transforms_matrix_in_str(matrix_with_edited_lst)

        save_and_load_data_user.rewrite_data_in_file(write_data)

        GUI.output_data(GUI.output_data_message['edited'])

    except:

        GUI.output_data(GUI.output_data_message['err_edit'])


def unloads_csv_file():
    """
    Выгружает имеющиеся заметки в csv файл если они имеются, либо выдает ошибку если заметки отсутствуют
    :return:
    """
    try:
        if not save_and_load_data_user.check_file():
            GUI.output_data(GUI.output_data_message['err_file'])
            return

        if not save_and_load_data_user.check_len_file():
            GUI.output_data(GUI.output_data_message['err_file'])
            return

        matrix_note = save_and_load_data_user.load_data()

        save_and_load_data_user.write_data_in_csv(matrix_note)

        GUI.output_data(GUI.output_data_message['csv'])

    except:
        GUI.output_data(GUI.output_data_message['err_csv'])

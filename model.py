import GUI
import modul_lower_level
import modul_upper_level
import save_and_load_data_user


def distributes_input_data_user(input_data: str):
    """
    Получает запрос пользователя и исходя из полученной команды распределяет в определенную функцию для исполнения запроса
    :param input_data: Пренимает запрос в виде строки
    :return:
    """
    while True:
        if modul_lower_level.check_command(input_data):
            if input_data == 'create':
                modul_upper_level.create_note()
                return

            if input_data == 'all notes':
                modul_upper_level.search_all_notes()
                return

            if input_data == 'search':
                modul_upper_level.search_note_by_name()
                return
            if input_data == 'sort':
                modul_upper_level.sorted_notes()
                return

            if input_data == 'delete':
                modul_upper_level.delete_note()
                return

            if input_data == 'edit':
                modul_upper_level.edits_note()
                return

            if input_data == 'csv':
                modul_upper_level.unloads_csv_file()
                return

            if input_data == 'info':
                GUI.print_output_menu()
                return
        else:
            GUI.output_data(GUI.output_data_message['err_input'])
            return
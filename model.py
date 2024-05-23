import GUI
import modul_lower_level as ml
import modul_upper_level as mu



def distributes_input_data_user(input_data: str):
    """
    Получает запрос пользователя и исходя из полученной команды распределяет в определенную функцию для исполнения запроса
    :param input_data: Пренимает запрос в виде строки
    :return:
    """
    while True:
        if ml.check_command(input_data):
            if input_data == 'add':
                mu.create_note()
                return

            if input_data == 'all':
                mu.search_all_notes()
                return

            if input_data == 'search':
                mu.search_notes_by_input_data()
                return

            if input_data == 'sort':
                mu.sorted_notes()
                return

            if input_data == 'del':
                mu.delete_note()
                return

            if input_data == 'edit':
                mu.edits_note()
                return

            if input_data == 'csv':
                mu.unloads_csv_file()
                return

            if input_data == 'info':
                GUI.output_data(GUI.output_data_message['all_menu'])
                return
        else:
            GUI.output_data(GUI.output_data_message['err_input'])
            return
import save_data_user
import modul_upper_level
import GUI


# def run_program():
#     GUI.print_output_menu()
#     GUI.input_data('Введите наименование заметки >> ')
#     # starts_main_loop()






def starts_main_loop():
    """
    Запускает главный жизненный цикл программы
    :return:
    """
    while True:
        input_data = GUI.input_data(GUI.input_data_message['name_note'])
        if input_data == 'stop':
            return
        if not modul_upper_level.create_note(input_data):
            GUI.output_data(GUI.output_data_message['empty_note'])


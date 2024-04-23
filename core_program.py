
import modul_upper_level
import GUI
import save_data_user

def run_program(data_set_notes):
    GUI.print_output_menu()

    starts_main_loop(data_set_notes)


def starts_main_loop():
    """
    Запускает главный жизненный цикл программы
    :return:
    """
    while True:
        input_data = GUI.input_data('Введите команду >> ')
        if input_data != '':
            if input_data == 'stop':
                return

            if input_data == 'create':
                data_set_notes = save_data_user.create_matrix_data()
                if not data_set_notes:
                    GUI.output_data(GUI.output_data_message['err_save'])
            if input_data == 'all notes':
                print(data_set_notes)
            else:
                GUI.output_data(GUI.output_data_message['err_input'])
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])
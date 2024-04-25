
import modul_upper_level
import GUI
import save_and_load_data_user
import model

def run_program():
    GUI.print_output_menu()
    starts_main_loop()


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
            else:
                model.distributes_input_data_user(input_data)
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])
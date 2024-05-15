
import GUI
import model


def run_program():
    """
    Выводит Приветствие и информационный блок, содержащий список команд
    :return:
    """
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    GUI.output_data(GUI.output_data_message['greetings'])
    GUI.output_data(GUI.output_data_message['all_menu'])
    starts_main_loop()


def starts_main_loop():
    """
    Запускает главный жизненный цикл программы
    :return:
    """
    while True:
        input_data = GUI.input_data('\033[36mВведите команду >> ')
        if input_data == 'stop' or input_data == 'back':
            GUI.output_data(GUI.output_data_message['off'])
            return
        if input_data != '':
            model.distributes_input_data_user(input_data)
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])

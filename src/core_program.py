import ctypes
import GUI
import model
import save_and_load_data_user as sld


def run_program():
    """
    Загружает данные из файла, выводит приветственное сообщение, запускает ядро программы, сохраняет данные в файл после завершения работы программы
    :return:
    """
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    sld.load_data()

    GUI.output_data(GUI.output_data_message['greetings'])

    starts_main_loop()

    sld.save_data()

    GUI.output_data('off')


def starts_main_loop():
    """
    Запускает главный жизненный цикл программы, пренимает ввод пользователя и обрабатывает его, при необходимости выбрасывает исключения
    :return:
    """
    GUI.output_data(GUI.output_data_message['all_menu'])
    while True:
        input_data = GUI.input_data('\033[36mВведите команду >> ')
        if input_data == 'stop':
            return

        if input_data == 'back':
            GUI.output_data(GUI.output_data_message['err_menu'])
            continue

        if input_data == '':
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue

        else:
            model.distributes_input_data_user(input_data)

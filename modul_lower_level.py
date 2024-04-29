import GUI
import save_and_load_data_user


def checks_input_for_empty_str(input_data) -> bool:
    """
    Выполняет проверку на пустую строку полученных данных, возвращает Тру если строка не пустая, в противном случае вернет Фолс
    :param input_data: Пренимает введенные пользователем данные
    :return: True или False
    """
    if input_data != '':

        return True
    else:
        return False


def check_commands(input_data: str) -> bool:
    """
    Сравнивает вводимые данные с предложенными командами и возвращает True если такая команда существует или False если такой команды нет
    :param input_data: Пренимает вводимые данные
    :return: True или False
    """
    if input_data == 'create' or input_data == 'search' or input_data == 'all notes' or input_data == 'delete' or input_data == 'edit' or input_data == 'info':
        return True
    else:
        return False


def check_and_create_name_note(lst_data_note: list) -> bool or str:
    """
    Запрашивает название заметки и осуществляет проверки, если проверки пройдены то добавляет название заметки в список
    :param lst_data_note: Пренимает список
    :return: Возвращет True если название заметки успешно добавлено в список или строку 'stop' если пользователь ввел эту команду
    """
    name_note = ''
    while name_note == '':
        name_note = GUI.input_data('\033[36mВведите название заметки >>\033[0m ')
        if name_note == 'stop':
            return 'stop'
        if checks_input_for_empty_str(name_note):
            lst_data_note.append(f'\033[36mНазвание заметки:\033[0m {name_note}')
            return True
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue


def check_and_create_importance_note(lst_data_note: list) -> bool or str:
    """
    Запрашивает важность заметки и осуществляет проверки, если проверки пройдены то добавляет важность заметки в список
    :param lst_data_note: Пренимает список
    :return: Возвращет True если важность заметки успешно добавлена в список или строку 'stop' если пользователь ввел эту команду
    """
    importance = ''
    while importance != 'important' or importance == 'not important':
        importance = GUI.input_data('\033[36mУкажите важность заметки >>\033[0m ')
        if checks_input_for_empty_str(importance):
            if importance == 'stop':
                return 'stop'

            if importance == 'important' or importance == 'not important':
                lst_data_note.append(f'\033[36mВажность заметки:\033[0m {importance}')
                return True
            else:
                GUI.output_data(GUI.output_data_message['err_input'])
                continue
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue


def check_and_create_text_note(lst_data_note: list) -> bool or str:
    """
    Запрашивает текст заметки и осуществляет проверки, если проверки пройдены то добавляет текст заметки в список
    :param lst_data_note: Пренимает список
    :return: Возвращет True если текст заметки успешно добавлен в список или строку 'stop' если пользователь ввел эту команду
    """
    text_note = ''
    while text_note == '':
        text_note = GUI.input_data('\033[36mВведите текст заметки >>\033[0m ')
        if text_note == 'stop':
            return 'stop'
        if checks_input_for_empty_str(text_note):
            lst_data_note.append(f'\033[36mТекст заметки:\033[0m {text_note}')
            return True
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue


def create_lst_data_note() -> list or bool:
    """
    Создает список элементов заметки в виде строк
    :return: Возвращает список элементов заметки
    """
    lst_data_note = []

    name_note = check_and_create_name_note(lst_data_note)
    if name_note == 'stop':
        return
    importance = check_and_create_importance_note(lst_data_note)
    if importance == 'stop':
        return
    text_note = check_and_create_text_note(lst_data_note)
    if text_note == 'stop':
        return
    else:
        return lst_data_note



def create_write_data(lst_data_note):
    """
    Добавляет между элементами списка служебный символ, по которому в дальнейшем будут делиться элементы заметки
    :param lst_data_note:
    :return:
    """
    write_data = '<{@}>'.join(lst_data_note)
    return write_data




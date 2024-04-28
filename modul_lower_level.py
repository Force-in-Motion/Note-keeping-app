import GUI



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
    if input_data == 'create' or input_data == 'search' or input_data == 'all notes' or input_data == 'delete' or input_data == 'edit':
        return True
    else:
        return False

def check_and_create_name_note(lst_data_note):
    name_note = ''
    while name_note == '':
        name_note = GUI.input_data('Введите название заметки >> ')
        if name_note == 'stop':
            return 'stop'
        if checks_input_for_empty_str(name_note):
            lst_data_note.append(name_note)
            return True
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue


def check_and_create_importance_note(lst_data_note):
    importance = ''
    while importance != 'important' or importance == 'not important':
        importance = GUI.input_data('Укажите важность заметки >> ')
        if checks_input_for_empty_str(importance):
            if importance == 'stop':
                return 'stop'

            if importance == 'important' or importance == 'not important':
                lst_data_note.append(importance)
                return True
            else:
                GUI.output_data(GUI.output_data_message['err_input'])
                continue
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue


def check_and_create_text_note(lst_data_note):
    text_note = ''
    while text_note == '':
        text_note = GUI.input_data('Введите текст заметки >> ')
        if text_note == 'stop':
            return 'stop'
        if checks_input_for_empty_str(text_note):
            lst_data_note.append(text_note)
            return True
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue




def create_lst_data_note() -> list:
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



# def create_matrix_note(write_data):
#     data_file = write_data.split('\n')
#
#     matrix_note = []
#
#     for i in range(0, len(data_file), 1):
#         matrix_note.append(data_file[i].split('<{@}>'))
#     return matrix_note
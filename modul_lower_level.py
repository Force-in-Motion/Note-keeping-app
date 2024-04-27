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



def create_lst_data_note() -> list:
    """
    Создает список элементов заметки в виде строк
    :return: Возвращает список элементов заметки
    """
    lst_data_note = []
    while True:
        name_note = GUI.input_data('Введите название заметки >> ')
        if name_note == 'stop':
            return
        if checks_input_for_empty_str(name_note):
            lst_data_note.append(name_note)
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue

        importance = GUI.input_data('Укажите важность заметки >> ')
        if importance == 'stop':
            return
        if checks_input_for_empty_str(importance):
            lst_data_note.append(importance)
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue

        text_note = GUI.input_data('Введите текст заметки >> ')
        if importance == 'stop':
            return
        if checks_input_for_empty_str(text_note):
            lst_data_note.append(text_note)
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue

        return lst_data_note


def adds_symbol_between_elems_note(lst_data_note):
    """
    Добавляет между элементами списка служебный символ, по которому в дальнейшем будут делиться элементы заметки
    :param lst_data_note:
    :return:
    """
    lst_data_separated_by_symbol = []
    for i in lst_data_note:
        lst_data_note.append('<{@}>'.join(i))

    return lst_data_separated_by_symbol


def create_write_data(lst_data_separated_by_symbol) -> str:
    """
    Добавляет в конце каждого списка \n чтобы потом это дело удобно считывать в матрицу
    :param lst_data_separated_by_symbol: Пренимает список элементов заметки, деленных служебным символом
    :return:
    """
    write_data = '\n'.join(lst_data_separated_by_symbol)
    return write_data


# def create_matrix_note(write_data):
#     data_file = write_data.split('\n')
#
#     matrix_note = []
#
#     for i in range(0, len(data_file), 1):
#         matrix_note.append(data_file[i].split('<{@}>'))
#     return matrix_note
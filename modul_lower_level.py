

def checks_input_for_empty_str(input_data) -> str:
    """
    Выполняет проверку на пустую строку полученных данных, возвращает Тру если строка не пустая, в противном случае вернет Фолс
    :param input_data: Пренимает введенные пользователем данные
    :return: True или False
    """
    if input_data != '':

        return True
    else:
        return False

def check_input_for_menu(input_data):
    if input_data == 'create' or input_data == 'search' or input_data == 'all notes' or input_data == 'delete' or input_data == 'edit':
        return True
    else:
        return False


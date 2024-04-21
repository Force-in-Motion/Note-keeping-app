
def save_input_data(input_data: str) -> list:
    lst = []
    lst.append(input_data)
    return lst



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

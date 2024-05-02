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

def check_importance_note():
    new_data = ''
    while new_data == 'important' or new_data == 'not important':
        new_data = GUI.input_data(GUI.input_data('\033[36mУкажите важность заметки >>\033[0m '))
        if checks_input_for_empty_str(new_data):
            if new_data == 'important' or new_data == 'not important':
                return new_data
            else:
                GUI.output_data(GUI.output_data_message['err_input'])
                continue
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue


def check_and_create_name_note(lst_data_note: list) -> bool or str:
    """
    Запрашивает название заметки и осуществляет проверки, если проверки пройдены то добавляет название заметки в список
    :param lst_data_note: Пренимает список
    :return: Возвращет True если название заметки успешно добавлено в список или строку 'stop' если пользователь ввел эту команду
    """
    name_note = ''
    while name_note == '':
        name_note = GUI.input_data('\033[36mВведите название заметки >>\033[0m ')
        if name_note == 'back':
            return 'back'
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
            if importance == 'back':
                return 'back'

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
        if text_note == 'back':
            return 'back'
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
    if name_note == 'back':
        return
    importance = check_and_create_importance_note(lst_data_note)
    if importance == 'back':
        return
    text_note = check_and_create_text_note(lst_data_note)
    if text_note == 'back':
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


def search_note_in_matrix_data(matrix_note: list[list]) -> list: # Реализовать остановку программы 'back'
    """
    Внутри себя запрашивает у пользователя название заметки, проводит проверки и если они возвращают True то перебирает матрицу и находят нужный список, содержащий элементы искомой заметки
    :param matrix_note: Пренимает матрицу заметок
    :return: Возвращает список, содержащий элементы искомой заметки
    """
    while True:
        input_data = GUI.input_data(GUI.output_data_message['srch_note'])

        # if input_data == 'back':
        #     return

        if checks_input_for_empty_str(input_data):
            flag = False
            for i in range(0, len(matrix_note), 1):
                for j in range(0, len(matrix_note[i]), 1):
                    if input_data in matrix_note[i][j]:
                        input_data = matrix_note[i]
                        flag = True
                        return input_data
            if not flag:
                GUI.output_data(GUI.output_data_message['err_search'])
        else:
            GUI.output_data(GUI.output_data_message['empty_note'])


def dell_note_in_matrix_data(del_note, matrix_note: str and list[list]) -> list[list]:
    """
    Обходит полученную матрицу и сравнивает каждый вложенный список с полученным списком, который требуется удалить и если они равны то удаляет его
    :param del_note: Пренимает в виде списка заметку, которую требуется удалить
    :param matrix_note: Матрица списков, содержащих элементы сохраненных заметок
    :return: Возвращает матрицу с удаленным списком
    """
    for i in range(0, len(matrix_note), 1):
        if matrix_note[i] == del_note:
            del matrix_note[i]

            return matrix_note


def transforms_matrix_in_str(matrix_with_del_lst):
    """
    Обходит все списки матрицы и разделяет их элементы служебным символом, затем разделяет списки матрицы "\n"
    :param matrix_with_del_lst: Пренимает матрицу элементов с удаленным списком
    :return: Возвращает строку, готовыю к записи в файл
    """
    for i in range(0, len(matrix_with_del_lst), 1):
        matrix_with_del_lst[i] = '<{@}>'.join(matrix_with_del_lst[i])
    write_data = '\n'.join(matrix_with_del_lst)

    return write_data


def requests_and_processes_edit_data_note(search_note):

    while True:
        input_data = GUI.input_data(GUI.output_data_message['editor'])

        if input_data == 'back':
            return

        if checks_input_for_empty_str(input_data):
            edit_note = edit_data_lst_note(search_note, input_data)
            return edit_note

        else:
            GUI.output_data(GUI.output_data_message['empty_note'])


def edit_data_lst_note(search_note, input_data):
    for i in range(0, len(search_note), 1):
        if input_data == 'name':
            new_data = GUI.input_data(GUI.output_data_message['new_data'])
            if checks_input_for_empty_str(new_data):
                search_note[0] = f'\033[36mНазвание заметки:\033[0m {new_data}'
                return search_note

        if input_data == 'importance':
            new_data = check_importance_note()
            search_note[1] = f'\033[36mВажность заметки:\033[0m {new_data}'
            return search_note

        if input_data == 'text':
            new_data = GUI.input_data(GUI.output_data_message['new_data'])
            if checks_input_for_empty_str(new_data):
                search_note[2] = f'\033[36mТекст заметки:\033[0m {new_data}'
                return search_note





# def requests_and_processes_new_importance_note():
#     pass

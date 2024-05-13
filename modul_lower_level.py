import datetime
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


def check_input_data_in_matrix_note(input_data, matrix: str and list[list]) -> str or bool:
    """
    Выполняет поиск совпадений полученной строки и элементов вложенных списков матрицы, если находит, то присваивает полученной строке список, содержащий совпадение
    :param input_data: Пренимает строку
    :param matrix: Пренимает матрицу
    :return:
    """
    for row in matrix:
        for elem in row:
            if input_data == elem:
                note = row
                return note


def check_command(input_data: str) -> bool:
    """
    Сравнивает вводимые данные с предложенными командами и возвращает True если такая команда существует или False если такой команды нет
    :param input_data: Пренимает вводимые данные
    :return: True или False
    """
    if input_data == 'create' or input_data == 'search' or input_data == 'all notes' or input_data == 'delete' or input_data == 'edit' or input_data == 'info' or input_data == 'sort' or input_data == 'csv':
        return True
    else:
        return False


def check_name_note(input_data: str) -> bool:
    """
    Проверяет на совпадение пренимаемой строки и элементов матрицы
    :param input_data: Пренимает строку для проверки совпадения с элементами матрицы
    :return: True
    """
    matrix = save_and_load_data_user.load_data()
    for row in matrix:
        for elem in row:
            if input_data == elem:
                return True
            else:
                continue


def requests_and_check_name_note() -> bool or str:
    """
    Запрашивает название заметки и осуществляет проверки, если проверки пройдены то возвращает название заметки или строку 'back' если ее ввел пользователь
    :return: Возвращет название заметки если все проверки успешно пройдены или строку 'back' если пользователь ввел эту команду
    """
    while True:
        name_note = GUI.input_data('\033[36mВведите название заметки >>\033[0m ')
        if name_note == 'back':
            return 'back'

        if not checks_input_for_empty_str(name_note):
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue

        if save_and_load_data_user.check_file():
            if check_name_note(f'\033[36mНазвание заметки:\033[0m {name_note}'):
                GUI.output_data(GUI.output_data_message['err_name_note'])
                continue

            else:
                return name_note
        else:
            return name_note


def requests_and_check_importance_note() -> bool or str:
    """
    Запрашивает важность заметки и осуществляет проверки, если проверки пройдены то возвращает выбранную пользователем важность заметки или строку 'back' если ее ввел пользователь
    :return: Возвращет важность или строку 'back' если пользователь ввел эту команду
    """
    importance = ''
    while importance != 'important' or importance == 'not important':
        importance = GUI.input_data('\033[36mУкажите важность заметки >>\033[0m ')
        if importance == 'back':
            return 'back'

        if not checks_input_for_empty_str(importance):
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue

        if importance == 'important' or importance == 'not important':
            return importance

        else:
            GUI.output_data(GUI.output_data_message['err_input'])
            continue


def requests_and_check_text_note() -> bool or str:
    """
    Запрашивает текст заметки и осуществляет проверки, если проверки пройдены то возвращает текст заметки или строку 'back' если ее ввел пользователь
    :return: Возвращет текст заметки если проверки успешно пройдены или строку 'back' если пользователь ввел эту команду
    """
    text_note = ''
    while text_note == '':
        text_note = GUI.input_data('\033[36mВведите текст заметки >>\033[0m ')
        if not checks_input_for_empty_str(text_note):
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue
        if text_note == 'back':
            return 'back'
        else:
            return text_note


def create_lst_data_note() -> list or bool:
    """
    Создает список элементов заметки в виде строк
    :return: Возвращает список элементов заметки
    """
    date_create_note = datetime.date.today()
    lst_data_note = []

    name_note = requests_and_check_name_note()
    if name_note == 'back':
        return 'back'
    else:
        lst_data_note.append(f'\033[36mНазвание заметки:\033[0m {name_note}')

    importance = requests_and_check_importance_note()
    if importance == 'back':
        return 'back'
    else:
        lst_data_note.append(f'\033[36mВажность заметки:\033[0m {importance}')

    text_note = requests_and_check_text_note()
    if text_note == 'back':
        return 'back'
    else:
        lst_data_note.append(f'\033[36mТекст заметки:\033[0m {text_note}')
        lst_data_note.append(f'\033[36mДата создания заметки:\033[0m {date_create_note}')

    return lst_data_note

def sorted_notes_by_input_data(matrix_note: list[list]) -> list[list] or str:
    """
    Сортирует матрицу по заданным пользователем параметрам
    :param matrix_note: Пренимает матрицу заметок
    :return: Возвращает сортированную матрицу заметок
    """
    while True:
        input_data = GUI.input_data(GUI.output_data_message['srt'])

        if input_data == 'back':
            return 'back'

        if input_data == 'not important' or input_data == 'important':
            GUI.print_sorted_notes(matrix_note, f'\033[36mВажность заметки:\033[0m {input_data}')
            return
        if input_data == 'sort date' or input_data == 'sort name':
            GUI.print_all_notes(sorted(matrix_note))
        else:
            GUI.output_data(GUI.output_data_message['err_input'])
            continue


def create_write_data(lst: list):
    """
    Добавляет между элементами списка служебный символ, по которому в дальнейшем будут делиться элементы заметки
    :param lst_data_note:
    :return:
    """
    write_data = '<{@}>'.join(lst)
    return write_data


def search_note_in_matrix_data(matrix_note: list[list]) -> list or bool: # Реализовать остановку программы 'back'
    """
    Внутри себя запрашивает у пользователя название заметки, проводит проверки и находит нужный список, содержащий элементы искомой заметки или строку 'back' если ее ввел пользователь
    :param matrix_note: Пренимает матрицу заметок
    :return: Возвращает список, содержащий элементы искомой заметки или строку 'back' если ее ввел пользователь
    """
    while True:
        input_data = GUI.input_data(GUI.output_data_message['srch_note'])
        if input_data == 'back':
            return 'back'

        if not checks_input_for_empty_str(input_data):
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue

        search_note = check_input_data_in_matrix_note(f'\033[36mНазвание заметки:\033[0m {input_data}', matrix_note)

        if not search_note:
            GUI.output_data(GUI.output_data_message['err_search'])
            continue

        else:
            return search_note


def dell_note_in_matrix_data(del_note, matrix: str and list[list]) -> list[list]:
    """
    Обходит полученную матрицу и сравнивает каждый вложенный список с полученным списком, который требуется удалить и если они равны то удаляет его
    :param del_note: Пренимает в виде списка заметку, которую требуется удалить
    :param matrix_note: Матрица списков, содержащих элементы сохраненных заметок
    :return: Возвращает матрицу с удаленным списком
    """
    for i in range(0, len(matrix), 1):
        if matrix[i] == del_note:
            del matrix[i]

            return matrix


def transforms_matrix_in_str(matrix):
    """
    Обходит все списки матрицы и разделяет их элементы служебным символом, затем разделяет списки матрицы "\n"
    :param matrix_with_del_lst: Пренимает матрицу элементов с удаленным списком
    :return: Возвращает строку, готовыю к записи в файл
    """
    for i in range(0, len(matrix), 1):
        matrix[i] = '<{@}>'.join(matrix[i])
    write_data = '\n'.join(matrix)

    return write_data


def create_edited_matrix_note(search_note, matrix_note: str and list[list]) -> list[list] or bool:
    """
    Редактирует матрицу заметок согласно полученным данным
    :param search_note: Пренимает список, содержащий редактированную заметку
    :param matrix_note: Пренимает матрицу исходных заметок
    :return: Возвращает матрицу редактированных заметок или строку 'back' если ее ввел пользователь
    """
    while True:
        input_data = GUI.input_data(GUI.output_data_message['editor'])

        if input_data == 'back':
            return 'back'

        if not checks_input_for_empty_str(input_data):
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue

        if input_data == 'name' or input_data == 'importance' or input_data == 'text':
            edit_note = edit_data_lst_note(search_note, input_data)
            if edit_note == 'back':
                return 'back'
            matrix_with_edited_lst = dell_note_in_matrix_data(search_note, matrix_note)
            matrix_with_edited_lst.append(edit_note)
            return matrix_with_edited_lst
        else:
            GUI.output_data(GUI.output_data_message['err_input'])





def edit_data_lst_note(search_note, input_data: list and str) -> list or str:
    """
    Заменяет элементы списка на новые в зависимости от полученных данных
    :param search_note: Пренимает список, содержащий исходные элементы заметки
    :param input_data: Пренимает строку, которая поясняет какой именно элемент списка будет меняться на новый
    :return: Возвращает измененный список или строку 'back' если ее ввел пользователь
    """
    for i in range(0, len(search_note), 1):
        if input_data == 'name':
            new_name = requests_and_check_name_note()
            if new_name == 'back':
                return 'back'
            else:
                search_note[0] = f'\033[36mНазвание заметки:\033[0m {new_name}'
                return search_note

        if input_data == 'importance':
            new_importance = requests_and_check_importance_note()
            if new_importance == 'back':
                return 'back'
            else:
                search_note[1] = f'\033[36mВажность заметки:\033[0m {new_importance}'
                return search_note

        if input_data == 'text':
            new_text = requests_and_check_text_note()
            if new_text == 'back':
                return 'back'
            else:
                search_note[2] = f'\033[36mТекст заметки:\033[0m {new_text}'
                return search_note


import datetime
import GUI
from save_and_load_data_user import matrix_notes


def checks_input_for_empty_str(input_data) -> bool:
    """
    Выполняет проверку на пустую строку полученные данных, возвращает Тру если строка не пустая, в противном случае вернет Фолс
    :param input_data: Пренимает введенные пользователем данные
    :return: True или False
    """
    if input_data != '':
        return True
    else:
        return False


def check_input_data_in_matrix_note(input_data: str) -> str or bool:
    """
    Выполняет поиск совпадений полученной строки и элементов вложенных списков матрицы, если находит, то присваивает полученной строке список, содержащий совпадение
    :param input_data: Пренимает строку
    :return:
    """
    for row in matrix_notes:
        for elem in row:
            if input_data == elem:
                note = row
                return note


def create_matrix_search_notes(input_data: str) -> list[list]:
    """
    Создает матрицу заметок, в которых содержатся данные, введенные пользователем
    :param input_data: Пренимает данные, по которым происходит фильтрование и затем добавление заметок в новую матрицу
    :return: Возвращает новую матрицу
    """
    matrix_search_notes = []

    for i in range(0, len(matrix_notes), 1):
        for j in range(0, len(matrix_notes[i]), 1):

            if input_data in matrix_notes[i][j]:
                matrix_search_notes.append(matrix_notes[i])
            else:
                continue

    return matrix_search_notes


def check_name_note(input_data: str) -> bool:
    """
    Проверяет на совпадение пренимаемой строки и элементов матрицы
    :param input_data: Пренимает строку для проверки совпадения с элементами матрицы
    :return: bool
    """
    for row in matrix_notes:
        for elem in row:
            if input_data == elem:
                return True
            else:
                continue


def requests_and_check_name_note() -> str:
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

        if check_name_note(f'\033[36mНазвание заметки:\033[0m {name_note}'):
            GUI.output_data(GUI.output_data_message['err_name_note'])
            continue

        else:
            return name_note


def requests_and_check_importance_note() -> str:
    """
    Запрашивает важность заметки и осуществляет проверки, если проверки пройдены то возвращает выбранную пользователем важность заметки или строку 'back' если ее ввел пользователь
    :return: Возвращет важность или строку 'back' если пользователь ввел эту команду
    """
    while True:
        GUI.output_data(GUI.output_data_message['importance_menu'])

        importance = GUI.input_data('\033[36mУкажите важность заметки >>\033[0m ')
        if importance == 'back':
            return 'back'

        if not checks_input_for_empty_str(importance):
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue

        if importance == '+' or importance == '-':
            return importance

        else:
            GUI.output_data(GUI.output_data_message['err_input'])
            continue


def requests_and_check_text_note() -> str:
    """
    Запрашивает текст заметки и осуществляет проверки, если проверки пройдены то возвращает текст заметки или строку 'back' если ее ввел пользователь
    :return: Возвращет текст заметки если проверки успешно пройдены или строку 'back' если пользователь ввел эту команду
    """
    while True:
        text_note = GUI.input_data('\033[36mВведите текст заметки >>\033[0m ')

        if not checks_input_for_empty_str(text_note):
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue

        if text_note == 'back':
            return 'back'
        else:
            return text_note


def create_lst_data_note() -> list or str:
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
    elif importance == '+':
        lst_data_note.append(f'\033[36mВажность заметки:\033[0m important')

    elif importance == '-':
        lst_data_note.append(f'\033[36mВажность заметки:\033[0m not important')

    text_note = requests_and_check_text_note()
    if text_note == 'back':
        return 'back'
    else:
        lst_data_note.append(f'\033[36mТекст заметки:\033[0m {text_note}')
        lst_data_note.append(f'\033[36mДата создания заметки:\033[0m {date_create_note}')

    return lst_data_note


def sorted_notes_by_input_data() -> list[list] or str:
    """
    Сортирует матрицу по заданным пользователем параметрам
    :return: Возвращает сортированную матрицу заметок
    """
    while True:
        input_data = GUI.input_data(GUI.output_data_message['sort_menu'])

        if input_data == 'back':
            return 'back'

        if input_data == 'not important' or input_data == 'important':
            GUI.print_sorted_notes_for_importance(f'\033[36mВажность заметки:\033[0m {input_data}')
            return

        if input_data == 'sort date' or input_data == 'sort name':
            GUI.print_all_notes(sorted(matrix_notes))
            return

        else:
            GUI.output_data(GUI.output_data_message['err_input'])
            continue


def search_note_in_matrix_data() -> list or str:
    """
    Внутри себя запрашивает у пользователя название заметки, проводит проверки и находит нужный список, содержащий элементы искомой заметки или строку 'back' если ее ввел пользователь
    :return: Возвращает список, содержащий элементы искомой заметки или строку 'back' если ее ввел пользователь
    """
    while True:
        input_data = GUI.input_data(GUI.output_data_message['srch_note'])
        if input_data == 'back':
            return 'back'

        if not checks_input_for_empty_str(input_data):
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue

        search_note = check_input_data_in_matrix_note(f'\033[36mНазвание заметки:\033[0m {input_data}')

        if not search_note:
            GUI.output_data(GUI.output_data_message['err_search'])
            continue

        else:
            return search_note


def open_note_in_matrix_data() -> list or str:
    """
    Внутри себя запрашивает у пользователя название заметки, проводит проверки и находит нужный список, содержащий элементы искомой заметки или строку 'back' если ее ввел пользователь
    :return: Возвращает список, содержащий элементы искомой заметки или строку 'back' если ее ввел пользователь
    """
    while True:
        input_data = GUI.input_data(GUI.output_data_message['menu_open_note'])
        if input_data == 'back':
            return 'back'

        if not checks_input_for_empty_str(input_data):
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue

        open_note = check_input_data_in_matrix_note(f'\033[36mНазвание заметки:\033[0m {input_data}')

        if not open_note:
            GUI.output_data(GUI.output_data_message['err_search'])
            continue

        else:
            return open_note


def check_input_data_and_return_new_matrix_notes() -> list or str:
    """
    Внутри себя запрашивает у пользователя данные, которые проходят проверки и если они пройдены, то возвращает готовыю матрицу заметок в которых были найдены совпадения с введенными данными
    :return: Возвращает список, содержащий элементы искомой заметки или строку 'back' если ее ввел пользователь
    """
    while True:
        input_data = GUI.input_data(GUI.output_data_message['srch_date_in_notes'])
        if input_data == 'back':
            return 'back'

        if not checks_input_for_empty_str(input_data):
            GUI.output_data(GUI.output_data_message['empty_note'])
            continue

        matrix_search_notes = create_matrix_search_notes(input_data)

        if not matrix_search_notes:
            GUI.output_data(GUI.output_data_message['err_data'])
            continue

        else:
            return matrix_search_notes


def dell_note_in_matrix_data(del_note) -> list[list]:
    """
    Обходит полученную матрицу и сравнивает каждый вложенный список с полученным списком, который требуется удалить и если они равны то удаляет его
    :param del_note: Пренимает в виде списка заметку, которую требуется удалить
    :return: Возвращает матрицу с удаленным списком
    """
    for i in range(0, len(matrix_notes), 1):
        if matrix_notes[i] == del_note:
            del matrix_notes[i]

            return matrix_notes


def create_edited_matrix_note(search_note) -> list[list] or str:
    """
    Редактирует матрицу заметок согласно полученным данным
    :param search_note: Пренимает список, содержащий редактированную заметку
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

            matrix_with_edited_lst = dell_note_in_matrix_data(search_note)

            matrix_with_edited_lst.append(edit_note)

            return matrix_with_edited_lst
        else:
            GUI.output_data(GUI.output_data_message['err_input'])
            continue


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

            if new_importance == '+':
                search_note[1] = f'\033[36mВажность заметки:\033[0m important'
                return search_note

            if new_importance == '-':
                search_note[1] = f'\033[36mВажность заметки:\033[0m not important'
                return search_note

        if input_data == 'text':
            new_text = requests_and_check_text_note()
            if new_text == 'back':
                return 'back'
            else:
                search_note[2] = f'\033[36mТекст заметки:\033[0m {new_text}'
                return search_note


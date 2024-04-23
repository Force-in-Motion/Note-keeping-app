
output_data_message = {'greetings': """Приветствую Вас! 
        Все данные загружены 
        Программа успешно запущена!""",
               'menu': """Возможности программы :
        Для того чтобы создать новую заметку введите "create"
        Для того чтобы определить важность заметки введите "important" если это важная заметка или "not important" если заметка не важна
        Для того чтобы  найти заметку по Названию введите "search"
        Для того чтобы вывести все ваши заметки введите "all notes"
        Для того чтобы удалить заметку введите "delete"
        Для того чтобы редактировать заметку введите "edit"
        Для того чтобы выйти из программы введте "stop"
        """,
               'save': 'Ваша заметка успешно сохранена!',
               'off': 'Приложение завершило свою работу',
               'empty_note': 'Пустая строка не может быть принята, введите данные',
               'err_input': 'Я пока не могу это обработать, введите команду из предложенных',
               'err': 'Ошибка сохранения'
               }



def color_text_output():
    """
    Меняет цвет текста
    :return: None
    """
    print('\033[33mINFO: \033[0m', end='\t')

def color_text_input():
    """
    Меняет цвет текста
    :return: None
    """
    print('\033[34mUSER: \033[0m', end='\t')

def print_output_menu() -> str:
    """
    Выводит строку приветствия и описания возможностей программы'
    :return: None
    """
    color_text_output()
    print(output_data_message['greetings'])
    print()
    color_text_output()
    print(output_data_message['menu'])
    print()



def input_data(message) -> str:
    """
    Запрашивает у пользователя данные
    :return: Возвращает данные
    """
    color_text_output()
    print(message)
    color_text_input()
    return input()

def output_data(message) -> str:
    """
    Выводит пользователю сообщение
    :param message: Пренимает параметр в виде строки
    :return: None
    """
    color_text_output()
    print(message)
    print()
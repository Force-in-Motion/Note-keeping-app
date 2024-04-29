
output_data_message = {'greetings': """\033[36mПриветствую Вас! 
        Все данные загружены 
        Программа успешно запущена!""",
               'menu': """\033[36mВозможности программы :
        Для того чтобы создать новую заметку введите \033[32m"create:"\033[36m
        Для того чтобы определить важность заметки введите \033[32m"important"\033[36m если это важная заметка или \033[32m"not important"\033[36m если заметка не важна
        Для того чтобы  найти заметку по названию введите \033[32m"search"\033[36m
        Для того чтобы вывести все ваши заметки введите \033[32m"all notes"\033[36m
        Для того чтобы удалить заметку введите \033[32m"delete"\033[36m
        Для того чтобы редактировать заметку введите \033[32m"edit"\033[36m
        Для того чтобы выйти из программы введте \033[32m"stop"\033[36m
        Для того чтобы вывести список доступных команд введите \033[32m"info"
        """,
               'save': '\033[36mВаша заметка успешно сохранена!\033[0m',
               'del_note': '\033[36mВведите название заметки, которую следует удалить\033[0m',
               'ed_note': '\033[36mВведите название заметки, которую следует редактировать\033[0m',
               'srch_note': '\033[36mВведите название заметки, которую следует найти\033[0m',
               'desired_note': '\033[36mВаша заметка имеет следующее содержание :\033[0m',
               'disp_all_notes': '\033[36mСписок ваших заметок :\033[0m',
               'del': '\033[36mВаша заметка успешно удалена\033[0m',
               'off': '\033[36mПриложение завершило свою работу\033[0m',
               'empty_note': '\033[36mПустая строка не может быть принята, введите данные\033[0m',
               'err_input': '\033[36mЯ пока не могу это обработать, введите команду из предложенных\033[0m',
               'err_search': '\033[36mЗаметка с таким названием отсутствует, введите другое или создайте новую\033[0m',
               'err_save': '\033[36mПри сохранении возникла ошибка\033[0m',
               'err_data': '\033[36mЧто то пошло не так \033[1m\033[33m:(\033[0m',
               'err_del': 'При удалении возникла ошибка',
               }



def color_text_output():
    """
    Меняет цвет текста
    :return: None
    """
    print('\033[1m\033[33mINFO: \033[0m', end='\t')

def color_text_input():
    """
    Меняет цвет текста
    :return: None
    """
    print('\033[1m\033[35mUSER: \033[0m', end='\t')

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


def print_all_notes(matrix_note: list[list]) -> None:
    """
    Выводит в консоль все заметки пользователя
    :param matrix_note: Пренимает матрицу заметок
    :return: None
    """
    output_data(output_data_message['disp_all_notes'])

    for row in matrix_note:
        for elem in row:
            print(f'\t\t{elem}')
        print()


def print_search_note(input_data: list[list]) -> None:
    """
    Выводит в консоль искомую заметку пользователя
    :param matrix_note: Пренимает список, содержащий все эелементы заметки пользователя
    :return: None
    """
    output_data(output_data_message['desired_note'])

    for elem in input_data:
        print(f'\t\t{elem}')
    print()

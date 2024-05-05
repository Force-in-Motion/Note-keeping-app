import save_and_load_data_user

output_data_message = {'greetings': """\033[36mПриветствую Вас! 
        Все данные загружены 
        Программа успешно запущена!""",
                'all_menu': """\033[36mВозможности программы :
        Для того чтобы создать новую заметку введите \033[32m"create:"\033[36m
        Для того чтобы определить важность заметки введите \033[32m"important"\033[36m если это важная заметка или \033[32m"not important"\033[36m если заметка не важна
        Для того чтобы  найти заметку по названию введите \033[32m"search"\033[36m
        Для того чтобы вывести все ваши заметки введите \033[32m"all notes"\033[36m
        Для того чтобы удалить заметку введите \033[32m"delete"\033[36m
        Для того чтобы редактировать заметку введите \033[32m"edit"\033[36m
        Для того чтобы выйти из программы введите в главном меню \033[32m"stop"\033[36m
        Для того чтобы выйти в главное меню введите \033[32m"back"\033[36m
        Для того чтобы вывести список доступных команд введите \033[32m"info"
        """,
               'edit_menu': """\033[36mДля того чтобы редактировать название введите  \033[32m"name"\033[36m
        Для того чтобы редактировать важность введите \033[32m"importance"\033[36m
        Для того чтобы редактировать текст введите \033[32m"text"\033[36m
        """,
               'save': '\033[36mВаша заметка успешно сохранена!\033[0m',
               'editor': '\033[36mВведите элемент заметки, который требуется редактировать >>\033[0m',
               'edited': '\033[36mЗаметка успешно редактирована\033[0m',
               'new_data': '\033[36mВведите новые данные\033[0m',
               'srch_note': '\033[36mВведите название заметки, которую следует найти\033[0m',
               'desired_note': '\033[36mВаша заметка имеет следующее содержание :\033[0m',
               'disp_all_notes': '\033[36mСписок ваших заметок :\033[0m',
               'del': '\033[36mВаша заметка успешно удалена!\033[0m',
               'off': '\033[36mПриложение завершило свою работу!\033[0m',
               'empty_note': '\033[36mПустая строка не может быть принята, введите данные!\033[0m',
               'err_input': '\033[36mЯ пока не могу это обработать, введите команду из предложенных!\033[0m',
               'err_search': '\033[36mЗаметка с таким названием отсутствует, введите другое или создайте новую!\033[0m',
               'err_search_output': '\033[36mПри поиске заметки возникла ошибка, вы возвращены в главное меню\033[0m',
               'err_save': '\033[36mПри создании заметки возникла ошибка, вы возвращены в главное меню\033[0m',
               'err_data': '\033[36mВведенные данные отсутствуют, повторите ввод\033[0m',
               'err_del': '\033[36mПри удалении возникла ошибка, вы возвращены в главное меню\033[0m',
               'err_edit': '\033[36mПри редактировании возникла ошибка, вы возвращены в главное меню\033[0m',
               'err_file': '\033[36mФайл с заметками отсутствует, чтобы вызвать заметки с начала их создайте!\033[0m',
               'err_name_note': '\033[36mЗаметка с таким названием уже существует, введите другое название!\033[0m',
               'err_file': '\033[36mВ вашем файле отсутствуют заметки, для начала создайте их!\033[0m',
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
    print(output_data_message['all_menu'])
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



def print_search_note(input_data: list[list]) -> None or bool:
    """
    Выводит в консоль искомую заметку пользователя
    :param matrix_note: Пренимает список, содержащий все эелементы заметки пользователя
    :return: None
    """
    if not save_and_load_data_user.check_len_file():
        output_data(output_data_message['err_file'])
        return
    output_data(output_data_message['desired_note'])

    for elem in input_data:
        print(f'\t\t{elem}')
    print()

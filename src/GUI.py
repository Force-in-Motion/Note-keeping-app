from save_and_load_data_user import matrix_notes

output_data_message = {'greetings': """\033[36mПриветствую Вас! 
        Все данные загружены 
        Программа успешно запущена!""",
                'all_menu': """\033[36mВозможности программы :
        Для того чтобы создать новую заметку введите \033[32m"add:"\033[36m
        Для того чтобы найти заметки, содержащие введенные данные, введите \033[32m"search"\033[36m
        Для того чтобы вывести все ваши заметки введите \033[32m"all"\033[36m
        Для того чтобы сортировать все ваши заметки введите \033[32m"sort"\033[36m
        Для того чтобы удалить заметку введите \033[32m"del"\033[36m
        Для того чтобы редактировать заметку введите \033[32m"edit"\033[36m
        Для того чтобы выгрузить заметки в "csv" файл введите \033[32m"csv"\033[36m
        Для того чтобы выйти из программы в главном меню введите \033[32m"stop"\033[36m
        Для того чтобы выйти в главное меню введите \033[32m"back"\033[36m
        Для того чтобы вывести список доступных команд в главном меню введите \033[32m"info"
        """,
               'edit_menu': """\033[36mДля того чтобы редактировать название введите  \033[32m"name"\033[36m
        Для того чтобы редактировать важность введите \033[32m"importance"\033[36m
        Для того чтобы редактировать текст введите \033[32m"text"\033[36m
        """,
                'sort_menu': """\033[36mДля того чтобы сортировать ваши заметки по названию введите \033[32m"sort name"\033[36m
        Для того чтобы сортировать ваши заметки по типу важности введите \033[32m"important" или not important"\033[36m
        Для того чтобы сортировать ваши заметки по дате создания введите \033[32m"sort date"\033[36m
        """,
                'importance_menu': """\033[36mОпределите важность заметки:
        Для того чтобы указать что заметка повышенной важности ( important ) введите \033[32m"+"\033[36m
        Для того чтобы указать что заметка обычная ( not important ) введите \033[32m"-"\033[36m
        """,
                'srch_data_menu': """"\033Напоминаю:
        Текст и название может содержать любые символы
        Важность заметки- important или not important""",

               'save': '\033[36mВаша заметка успешно добавлена!\033[0m',
               'editor': '\033[36mВведите элемент заметки, который требуется редактировать >>\033[0m',
               'edited': '\033[36mЗаметка успешно редактирована\033[0m',
               'srch_note': '\033[36mВведите название заметки, которую следует найти\033[0m',
               'open_note': '\033[36mВведите \033[0m',
               'srch_date_in_notes': '\033[36mВведите данные, по которым следует найти заметки >> \033[0m',
               'desired_note': '\033[36mВаша заметка имеет следующее содержание :\033[0m\n',
               'disp_all_notes': '\033[36mСписок ваших заметок :\033[0m\n',
               'del': '\033[36mВаша заметка успешно удалена!\033[0m',
               'csv': '\033[36mФайл csv успешно создан на рабочем столе!\033[0m',
               'off': '\033[36mВсе данные сохранены.\n\tПриложение завершило свою работу!\033[0m',
               'empty_note': '\033[36mПустая строка не может быть принята, введите данные!\033[0m',
               'back_menu': '\033[36mВы возвращены в главное меню\033[0m',
               'menu_open_note': '\033[36mДля того чтобы открыть нужную заметку введите ее название\n\tИли введите \033[32m"back"\033[36m для возврата в главное меню\033[0m',
               'err_menu': '\033[36mВы и так в главном меню\033[0m',
               'err_input': '\033[36mЯ пока не могу это обработать, введите команду из предложенных!\033[0m',
               'err_search': '\033[36mЗаметка с таким названием отсутствует, введите другое или создайте новую!\033[0m',
               'err_search_output': '\033[36mПри поиске заметки возникла ошибка, вы возвращены в главное меню\033[0m',
               'err_save': '\033[36mПри создании заметки возникла ошибка, вы возвращены в главное меню\033[0m',
               'err_data': '\033[36mВведенные данные отсутствуют, повторите ввод\033[0m',
               'err_del': '\033[36mПри удалении возникла ошибка, вы возвращены в главное меню\033[0m',
               'err_edit': '\033[36mПри редактировании возникла ошибка, вы возвращены в главное меню\033[0m',
               'err_file': '\033[36mФайл с заметками отсутствует, чтобы вызвать заметки с начала их создайте!\033[0m',
               'err_name_note': '\033[36mЗаметка с таким названием уже существует, введите другое название!\033[0m',
               'err_sort': '\033[36mВ процессе сортировки возникла ошибка, вы возвращены в главное меню\033[0m',
               'err_csv': '\033[36mВ процессе создания csv файла возникла ошибка, вы возвращены в главное меню\033[0m',
               'err_srt_importance': '\033[36mЗаметки с указанной важностью отсутствуют\033[0m',
               }


def color_text_output():
    """
    Меняет цвет текста
    :return: None
    """
    print('\n\033[1m\033[33mINFO: \033[0m', end='\t')


def color_text_input():
    """
    Меняет цвет текста
    :return: None
    """
    print('\n\033[1m\033[35mUSER: \033[0m', end='\t')


def input_data(message: str) -> str:
    """
    Запрашивает у пользователя данные
    :return: Возвращает данные
    """
    color_text_output()
    print(message)
    color_text_input()
    return input()


def output_data(message: str):
    """
    Выводит пользователю сообщение
    :param message: Пренимает параметр в виде строки
    :return: None
    """
    if message == 'off':
        color_text_output()
        input(output_data_message[message])
        return

    color_text_output()
    print(message)


def print_all_notes(matrix_notes) -> None:
    """
    Выводит в консоль все названия заметок пользователя
    :return: None
    """
    output_data(output_data_message['disp_all_notes'])

    for i in range(0, len(matrix_notes), 1):
        for j in range(0, len(matrix_notes[i]), 1):
            pass
        print(f'\t{matrix_notes[i][0]}')


def print_open_note(note) -> None or bool:
    """
    Выводит в консоль искомую заметку пользователя
    :return: None
    """
    output_data(output_data_message['desired_note'])

    for elem in note:
        print(f'\t{elem}')


def print_elems_matrix_notes(matrix_notes) -> None:
    """
    Выводит на консоль элементы полученной матрицы
    :param matrix_notes: Пренимает матрицу
    :return: None
    """
    for row in matrix_notes:
        for elem in row:
            print(f'\t{elem}')
        print()


def print_sorted_notes_for_importance(input_data: str) -> None:
    """
    Выводит на консоль названия заметок пользователя исходя из заданных условий
    :param input_data: Пренимает строку для сравнения с имеющимися в матрице заметок
    :return: None
    """
    flag = False
    for i in range(0, len(matrix_notes), 1):
        for j in range(0, len(matrix_notes[i]), 1):
            if input_data in matrix_notes[i][j]:
                flag = True
                print(f'\t{matrix_notes[i][0]}')
    print()
    if not flag:
        output_data(output_data_message['err_srt_importance'])

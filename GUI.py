output_data_message = {'greetings': """Приветствую Вас! 
        Все данные загружены 
        Программа успешно запущена!""",
               'menu': """Возможности программы :
        Создание заметки и присвоение ей названия
        Запись содержания и определение ее важности
        Поиск заметки по названию
        Вывод всех заметок повышеной степени важности
        Редактирование заметок
        Удаление заметок""",
               'save': 'Ваша заметка успешно сохранена!',
               'off': 'Приложение завершило свою работу',
               'empty_note': 'Вы ввели пустую строку! Название заметки',
               'err': 'Ошибка сохранения'
               }



input_data_message = {'name_note': 'Введите название заметки >> ',
                      'importance': 'Укажите важность заметки >> ',
                      'important': 'Важная заметка',
                      'not_important': 'Обычная заметка'
                      }




def color_text():
    """
    Меняет цвет текста
    :return: None
    """
    print('\033[33mINFO: \033[0m', end='\t')



def print_output_menu() -> str:
    """
    Выводит строку приветствия и описания возможностей программы'
    :return: None
    """
    color_text()
    print(output_data_message['greetings'])
    print()
    color_text()
    print(output_data_message['menu'])
    print()



def input_data(message) -> str:
    """
    Запрашивает у пользователя данные
    :return: Возвращает данные
    """
    print(message)
    return input()

def output_data(message) -> str:
    """
    Выводит пользователю сообщение
    :param message: Пренимает параметр в виде строки
    :return: None
    """
    print(message)
import modul_lower_level
import save_data_user


def create_note(input_data):
    if modul_lower_level.checks_input_for_empty_str(input_data):
        lst = modul_lower_level.save_input_data(input_data)
        save_data_user.create_note_matrix(lst)
        return True
    else:
        return False


def search_note_by_name():
    pass


def read_and_output_notes():
    pass


def delete_note():
    pass


def edits_note():
    pass


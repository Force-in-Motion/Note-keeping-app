import modul_lower_level
import GUI
import save_and_load_data_user




def create_note():
    lst_data_note = modul_lower_level.create_lst_data_note()
    lst_data_separated_by_symbol = modul_lower_level.adds_symbol_between_elems_note(lst_data_note)
    print(lst_data_separated_by_symbol)
    write_data = modul_lower_level.create_write_data(lst_data_separated_by_symbol)
    save_and_load_data_user.write_data_in_file(write_data)
    print(save_and_load_data_user.write_data_in_file(write_data))
    return True


def search_note_by_name(search_note, matrix_note):
    pass

def search_set_notes(matrix_note):
    pass

def read_and_output_notes():
    pass


def delete_note(del_note, matrix_note):
    pass


def edits_note(edits_note, matrix_note):
    pass




import modul_lower_level
import GUI
import save_and_load_data_user




def create_note():
    lst_data_note = modul_lower_level.create_lst_data_note()

    write_data = modul_lower_level.create_write_data(lst_data_note)

    save_and_load_data_user.write_data_in_file(write_data)

    return True


def search_note_by_name():
    pass



def read_and_output_notes():
    pass


def delete_note(del_note, matrix_note):
    pass


def edits_note(edits_note, matrix_note):
    pass




import GUI
import core_program
import modul_upper_level


def distributes_input_data_user(input_data):
    if input_data == 'create':
        create_note = modul_upper_level.create_note()
        if not create_note:
            GUI.output_data(GUI.output_data_message['err_save'])
    if input_data == 'search':
        search_note = modul_upper_level.search_note_by_name()
        GUI.output_data(search_note)
        if not search_note:
            GUI.output_data(GUI.output_data_message['err_search'])
    if input_data == 'delete':
        delete_note = modul_upper_level.delete_note()
        GUI.output_data(GUI.output_data_message['del'])
        if not delete_note:
            GUI.output_data(GUI.output_data_message['err_del'])
    if input_data == 'edit':
        edits_note = modul_upper_level.edits_note()
        GUI.output_data(GUI.output_data_message['edited'])
        if not edits_note:
            GUI.output_data(GUI.output_data_message['err_ed'])
    if input_data == 'all notes':
        set_notes = modul_upper_level.search_set_notes()
        GUI.output_data(set_notes)
        if not set_notes:
            GUI.output_data(GUI.output_data_message['err_read'])
    else:
        GUI.output_data(GUI.output_data_message['err_input'])

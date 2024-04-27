import GUI
import modul_upper_level


def distributes_input_data_user(input_data):
    while True:
        if input_data == 'create':
            modul_upper_level.create_note()

        # if input_data == 'search':
        #     search_note = GUI.input_data(GUI.output_data_message['srch_note'])
        #     modul_upper_level.search_note_by_name(search_note)
        #     GUI.output_data(search_note)
        #
        # if input_data == 'delete':
        #     del_note = GUI.input_data(GUI.output_data_message['del_note'])
        #     modul_upper_level.delete_note(del_note)
        #     GUI.output_data(GUI.output_data_message['del'])
        #
        # if input_data == 'edit':
        #     edits_note = GUI.input_data(GUI.output_data_message['ed_note'])
        #     modul_upper_level.edits_note(edits_note)
        #     GUI.output_data(GUI.output_data_message['edited'])
        #
        # if input_data == 'all notes':
        #     set_notes = modul_upper_level.search_set_notes()
        #     GUI.output_data(set_notes)

        else:
            GUI.output_data(GUI.output_data_message['err_input'])
            continue
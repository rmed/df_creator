#!/usr/bin/python

def get_basic(window):
    # Get values from GUI fields
    name = window.builder.get_object("entry_name").get_text()
    execute = window.builder.get_object("entry_exec").get_text()
    icon = window.builder.get_object("entry_icon").get_text()

    # Get the value of the selected element of the type box
    type_index = window.builder.get_object("cbox_type").get_active()
    type_model = window.builderget_object("cbox_type").get_model()
    apptype = type_model[type_index][0]

    # Get the value of the selected element of the categories box
    category_index = window.builder.get_object("cbox_category").get_active()
    category_model = window.builder.get_object("cbox_category").get_model()
    category = category_model[category_index][0]

    # Uses terminal?
    useterm = "false"
    if window.builder.get_object("switch_terminal").get_active():
        useterm = "true"

    # Return basic contents for the file
    contents = [name, execute, icon, apptype, useterm, category]
    return contents

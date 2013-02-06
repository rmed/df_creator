#!/usr/bin/python

# Create the .desktop file
def save(window, filepath):
    # Get values from GUI fields
    name = window.builder.get_object("entry_name").get_text()
    command = window.builder.get_object("entry_command").get_text()
    icon = window.builder.get_object("entry_icon").get_text()
    apptype = window.builder.get_object("entry_type").get_text()

    # Get the value of the selected element of the box
    category_index = window.builder.get_object("cbox_category").get_active()
    category_model = window.builder.get_object("cbox_category").get_model()
    category = category_model[category_index][0]

    # Uses terminal?
    useterm = "false"
    if window.builder.get_object("switch_terminal").get_active():
        useterm = "true"

    # Define the contents of the file
    contents = ["[Desktop Entry]\n", "Name=" + name + "\n", "Exec=" + command + "\n", "Icon=" + icon + "\n", "Type=" + apptype + "\n", "Terminal=" + useterm + "\n", "Categories=" + category + ";"]

    # Write to file
    try:
        dfile = open(filepath, "w")
        try:
            dfile.writelines(contents)
        finally:
            dfile.close()
    except IOError:
        pass 


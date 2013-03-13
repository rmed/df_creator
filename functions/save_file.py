#!/usr/bin/python

import get_content

# Save the file
def savedf(window, savepath):
    # Get the values from the GUI
    values = get_content.GUIValues(window)

    towrite = []
    # Get contents depending on the specified type
    # Application (1)
    if values.typeindex == 0:
        towrite = save_type_app(values)
    # Link (2)
    elif values.typeindex == 1:
        towrite = save_type_link(values)
    # Directory (3)
    else:
        towrite = save_type_dir(values)

    # Save the file
    try:
        dfile = open(savepath, "w")
        try:
            dfile.writelines(towrite)
        finally:
            dfile.close()
    except IOError:
        pass 

# Type Application
def save_type_app(values):
    # Determine the final contents of the file
    final_content = ["[Desktop Entry]\n"]
    # Add name
    final_content.append("Name=" + values.name + "\n")
    # Has generic name?
    if values.genericname != '':
        final_content.append("GenericName=" + values.genericname + "\n")
    # Has comment?
    if values.comment != '':
        final_content.append("Comment=" + values.comment + "\n")
    # Has version?
    if values.version != '':
        final_content.append("Version=" + values.version + "\n")
    # Has tryexec?
    if values.tryexec != '':
        final_content.append("TryExec=" + values.tryexec + "\n")    
    # Add exec
    final_content.append("Exec=" + values.execute + "\n")
    # Has icon?
    if values.icon != '':
        final_content.append("Icon=" + values.icon + "\n")
    # Type?
    final_content.append("Type=Application\n")
    # Run from terminal?
    final_content.append("Terminal=" + values.useterm + "\n")
    # Add category
    final_content.append("Categories=" + values.category + "\n")
    # Must not display?
    if values.nodisplay != 'false':
        final_content.append("NoDisplay=true" + "\n")
    # Is hidden?
    if values.hidden != 'false':
        final_content.append("Hidden=true" + "\n")
    # Must not show in some environment?
    if values.notshowin != '':
        final_content.append("NotShowIn=" + values.notshowin + "\n")
    # Has path?
    if values.path != '':
        final_content.append("Path=" + values.path + "\n")
    # Has mime?
    if values.mime != '':
        final_content.append("MimeType=" + values.mime + "\n")
    # Has keywords?
    if values.keywords != '':
        final_content.append("Keywords=" + values.keywords + "\n")
    # Must notify startup?
    if values.notify != 'false':
        final_content.append("StartupNotify=true" + "\n")
    # Has startup wm class?
    if values.wmclass != '':
        final_content.append("StartupWMClass=" + values.wmclass + "\n")

    # Return final content
    return final_content

# Type Link
def save_type_link(values):
    # Determine the final contents of the file
    final_content = ["[Desktop Entry]\n"]
    # Add name
    final_content.append("Name=" + values.name + "\n")
    # Has generic name?
    if values.genericname != '':
        final_content.append("GenericName=" + values.genericname + "\n")
    # Has comment?
    if values.comment != '':
        final_content.append("Comment=" + values.comment + "\n")
    # Add URL
    final_content.append("URL=" + values.url + "\n")
    # Has version?
    if values.version != '':
        final_content.append("Version=" + values.version + "\n")
    # Has icon?
    if values.icon != '':
        final_content.append("Icon=" + values.icon + "\n")
    # Type?
    final_content.append("Type=Application\n")
    # Must not display?
    if values.nodisplay != 'false':
        final_content.append("NoDisplay=true" + "\n")
    # Is hidden?
    if values.hidden != 'false':
        final_content.append("Hidden=true" + "\n")
    # Must not show in some environment?
    if values.notshowin != '':
        final_content.append("NotShowIn=" + values.notshowin + "\n")

    # Return final content
    return final_content

# Type Directory
def save_type_dir(values):
    # Determine the final contents of the file
    final_content = ["[Desktop Entry]\n"]
    # Add name
    final_content.append("Name=" + values.name + "\n")
    # Has generic name?
    if values.genericname != '':
        final_content.append("GenericName=" + values.genericname + "\n")
    # Has comment?
    if values.comment != '':
        final_content.append("Comment=" + values.comment + "\n")
    # Has version?
    if values.version != '':
        final_content.append("Version=" + values.version + "\n")
    # Has icon?
    if values.icon != '':
        final_content.append("Icon=" + values.icon + "\n")
    # Type?
    final_content.append("Type=Application\n")
    # Run from terminal?
    final_content.append("Terminal=" + values.useterm + "\n")
    # Add category
    final_content.append("Categories=" + values.category + "\n")
    # Must not display?
    if values.nodisplay != 'false':
        final_content.append("NoDisplay=true" + "\n")
    # Is hidden?
    if values.hidden != 'false':
        final_content.append("Hidden=true" + "\n")
    # Must not show in some environment?
    if values.notshowin != '':
        final_content.append("NotShowIn=" + values.notshowin + "\n")

    # Return final content
    return final_content


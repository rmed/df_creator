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

def save_type_app(values):
    # Determine the final contents of the file
    final_content = ["[Desktop Entry]\n"]
    # Type?
    final_content.append("Type=Application\n")
    # Has version?
    if values.version != '':
        final_content.append("Version=" + values.version + "\n")
    # Add name
    final_content.append("Name=" + values.name + "\n")
    # Has generic name?
    if values.genericname != '':
        final_content.append("GenericName=" + values.genericname + "\n")
    # Must not display?
    final_content.append("NoDisplay=" + values.nodisplay + "\n")
    # Has comment?
    if values.comment != '':
        final_content.append("Comment=" + values.comment + "\n")
    # Has icon?
    if values.icon != '':
        final_content.append("Icon=" + values.icon + "\n")
    # Is hidden?
    final_content.append("Hidden=" + values.hidden + "\n")
    # Must not show in some environment?
    if values.notshowin != '':
        final_content.append("NotShowIn=" + values.notshowin + "\n")
    # Has tryexec?
    if values.tryexec != '':
        final_content.append("TryExec=" + values.tryexec + "\n")    
    # Add exec
    final_content.append("Exec=" + values.execute + "\n")
    # Has path?
    if values.path != '':
        final_content.append("Path=" + values.path + "\n")
    # Run from terminal?
    final_content.append("Terminal=" + values.useterm + "\n")
    # Has mime?
    if values.mime != '':
        final_content.append("MimeType=" + values.mime + "\n")
    # Add category
    final_content.append("Categories=" + values.category + "\n")
    # Has keywords?
    if values.keywords != '':
        final_content.append("Keywords=" + values.keywords + "\n")
    # Must notify startup?
    final_content.append("StartupNotify=" + values.notify + "\n")
    # Has startup wm class?
    if values.wmclass != '':
        final_content.append("StartupWMClass=" + values.wmclass + "\n")

    # Return final content
    return final_content

def save_type_link(values):
    # Determine the final contents of the file
    final_content = ["[Desktop Entry]\n"]
    # Type?
    final_content.append("Type=Link\n")    
    # Has version?
    if values.version != '':
        final_content.append("Version=" + values.version + "\n")
    # Add name
    final_content.append("Name=" + values.name + "\n")
    # Has generic name?
    if values.genericname != '':
        final_content.append("GenericName=" + values.genericname + "\n")
    # Must not display?
    final_content.append("NoDisplay=" + values.nodisplay + "\n")
    # Has comment?
    if values.comment != '':
        final_content.append("Comment=" + values.comment + "\n")
    # Has icon?
    if values.icon != '':
        final_content.append("Icon=" + values.icon + "\n")
    # Is hidden?
    final_content.append("Hidden=" + values.hidden + "\n")
    # Must not show in some environment?
    if values.notshowin != '':
        final_content.append("NotShowIn=" + values.notshowin + "\n")
    # Add URL
    final_content.append("URL=" + values.url + "\n")

    # Return final content
    return final_content

def save_type_dir(values):
    # Determine the final contents of the file
    final_content = ["[Desktop Entry]\n"]  
    # Type?
    final_content.append("Type=Directory\n") 
    # Has version?
    if values.version != '':
        final_content.append("Version=" + values.version + "\n")
    # Add name
    final_content.append("Name=" + values.name + "\n")
    # Has generic name?
    if values.genericname != '':
        final_content.append("GenericName=" + values.genericname + "\n")
    # Must not display?
    final_content.append("NoDisplay=" + values.nodisplay + "\n")
    # Has comment?
    if values.comment != '':
        final_content.append("Comment=" + values.comment + "\n")
    # Has icon?
    if values.icon != '':
        final_content.append("Icon=" + values.icon + "\n")
    # Is hidden?
    final_content.append("Hidden=" + values.hidden + "\n")
    # Must not show in some environment?
    if values.notshowin != '':
        final_content.append("NotShowIn=" + values.notshowin + "\n")

    # Return final content
    return final_content


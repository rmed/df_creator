#!/usr/bin/python

import get_content

# Create the .desktop file
def save(window, filepath):
    # Get basic contents
    basic_contents = get_content.get_basic(window)

    # Write to file
    try:
        dfile = open(filepath, "w")
        try:
            dfile.writelines(contents)
        finally:
            dfile.close()
    except IOError:
        pass 


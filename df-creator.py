#!/usr/bin/python

from gi.repository import Gtk
from functions import *

class MainGui:
    
    # Build the main window
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gui/df-creator.glade")
        self.builder.connect_signals(self)
        self.win = self.builder.get_object("main_window")
        self.win.show_all()
        # Hide URL box, as the default type is application
        self.builder.get_object("box_url").set_visible(False)
        

    # Destroy signal
    def on_delete_window(self, *args):
        Gtk.main_quit(*args)

    # Clean all the fields and start from scratch
    def on_new_activate(self, widget):
        entries = {
            "entry_name", "entry_exec", "entry_icon", "entry_url"
        }
        for entry in entries:
            self.builder.get_object(entry).set_text('')

        self.builder.get_object("switch_terminal").set_active(False)
        
    # Save file
    def on_save_activate(self, widget):
        # Create save dialog
        savedialog = Gtk.FileChooserDialog("Save file", self.win, Gtk.FileChooserAction.SAVE, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.OK))

        # Add filter
        dfilter = Gtk.FileFilter()
        dfilter.set_name(".desktop")
        dfilter.add_mime_type("application/x-desktop")
        savedialog.add_filter(dfilter)

        response = savedialog.run()
        # Call the save function
        if response == Gtk.ResponseType.OK:
            save_file.save(self, savedialog.get_filename())

        # Destroy dialog
        savedialog.destroy()

    # Hide objects depending on the type selected
    def on_type_changed(self, widget):
        # Create lists of the boxes present in the window
        type_application_boxes = {
            "box_tryexec", "box_exec", "box_path", "box_terminal", "box_mime", "box_category", "box_keywords", "box_notify", "box_wmclass"
        }

        type_directory_boxes = {
            "box_version", "box_name", "box_generic_name", "box_nodisplay", "box_comment", "box_icon", "box_hidden", "box_notshowin"
        }

        # Chosen type is Application (1)
        if widget.get_active() == 0:
            # Show all possible widgets for this type (1 & 3)
            for box in type_application_boxes:
                self.builder.get_object(box).set_visible(True)
            for box in type_directory_boxes:
                self.builder.get_object(box).set_visible(True)
            # Hide the URL box
            self.builder.get_object("box_url").set_visible(False)

        # Chosen type is URL (2)
        elif widget.get_active() == 1:
            # Show all possible widgets for this type (2)
            for box in type_directory_boxes:
                self.builder.get_object(box).set_visible(True)
            self.builder.get_object("box_url").set_visible(True)
            # Hide widgets of type 1
            for box in type_application_boxes:
                self.builder.get_object(box).set_visible(False)

        # Chosen type is Directory (3)
        elif widget.get_active() == 2:
            # Show all possible widgets for this type (3)
            for box in type_directory_boxes:
                self.builder.get_object(box).set_visible(True)
            # Hide widgets of types 1 & 3
            for box in type_application_boxes:
                self.builder.get_object(box).set_visible(False)
            self.builder.get_object("box_url").set_visible(False)
        
window = MainGui()
Gtk.main()


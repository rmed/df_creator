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

    # Destroy signal
    def on_delete_window(self, *args):
        Gtk.main_quit(*args)

    # Clean all the fields and start from scratch
    def on_new_activate(self, widget):
        entries = {
            "entry_name", "entry_command", "entry_icon", "entry_type"
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
            savefile.save(self, savedialog.get_filename())

        # Destroy dialog
        savedialog.destroy()
        
window = MainGui()
Gtk.main()


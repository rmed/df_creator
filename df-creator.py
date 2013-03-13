'''
Main program controller
'''

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

    # Search for element to execute
    def on_btn_exec_clicked(self, widget):

        # Create dialog for choosing element
        opendialog = Gtk.FileChooserDialog("Choose element", self.win, Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = opendialog.run()
        # Change exec
        if response == Gtk.ResponseType.OK:
            self.builder.get_object("entry_exec").set_text(opendialog.get_filename())

        # Destroy dialog
        opendialog.destroy()

    # Search for an icon
    def on_btn_icon_clicked(self, widget):

        # Create dialog for choosing icon
        opendialog = Gtk.FileChooserDialog("Choose icon", self.win, Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        # Add filters
        ifilter = Gtk.FileFilter()
        ifilter.set_name("Image files")
        ifilter.add_mime_type("image/*")
        opendialog.add_filter(ifilter)

        response = opendialog.run()
        # Change icon
        if response == Gtk.ResponseType.OK:
            self.builder.get_object("entry_icon").set_text(opendialog.get_filename())

        # Destroy dialog
        opendialog.destroy()

    # Search for element to execute
    def on_btn_tryexec_clicked(self, widget):

        # Create dialog for choosing element
        opendialog = Gtk.FileChooserDialog("Choose element", self.win, Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = opendialog.run()
        # Change exec
        if response == Gtk.ResponseType.OK:
            self.builder.get_object("entry_tryexec").set_text(opendialog.get_filename())

        # Destroy dialog
        opendialog.destroy()

    # Search for element to execute
    def on_btn_path_clicked(self, widget):

        # Create dialog for choosing directory
        opendialog = Gtk.FileChooserDialog("Choose directory", self.win, Gtk.FileChooserAction.SELECT_FOLDER, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = opendialog.run()
        # Change exec
        if response == Gtk.ResponseType.OK:
            self.builder.get_object("entry_path").set_text(opendialog.get_filename())

        # Destroy dialog
        opendialog.destroy()


    # About dialog
    def on_about_activate(self, widget):

        # Get the dialog from the glade file
        dialog = self.builder.get_object("about_dialog")
        response = dialog.run()

        # Get response
        if response == Gtk.ResponseType.CANCEL or response == Gtk.ResponseType.DELETE_EVENT:
            # Hide the dialog
            dialog.hide()

    # Clean all the fields and start from scratch
    def on_new_activate(self, widget):

        # Create dialog asking whether or not to continue
        newdialog = Gtk.MessageDialog(self.win, Gtk.DialogFlags.DESTROY_WITH_PARENT, Gtk.MessageType.INFO, Gtk.ButtonsType.YES_NO, "All unsaved progress will be lost, continue?")

        response = newdialog.run()
        # Reset all the content
        if response == Gtk.ResponseType.YES:
            entries = {
                "entry_name", "entry_exec", "entry_icon", "entry_url", "entry_version", "entry_generic_name", "entry_comment", "entry_notshowin", "entry_tryexec", "entry_path", "entry_mime", "entry_keywords", "entry_wmclass"
            }
            # Clear entries
            for entry in entries:
                self.builder.get_object(entry).set_text('')

            # Clear switches
            self.builder.get_object("switch_terminal").set_active(False)
            self.builder.get_object("switch_nodisplay").set_active(False)
            self.builder.get_object("switch_hidden").set_active(False)
            self.builder.get_object("switch_notify").set_active(False)
        
        # Destroy Dialog
        newdialog.destroy()
        
    # Save file
    def on_save_activate(self, widget):

        # Create save dialog
        savedialog = Gtk.FileChooserDialog("Save file", self.win, Gtk.FileChooserAction.SAVE, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.OK))

        # Ask for confirmation on overwrite
        savedialog.set_do_overwrite_confirmation(True) 

        # Define initial name for the file
        savedialog.set_current_name(self.builder.get_object("entry_name").get_text().lower())     

        # Add filter
        dfilter = Gtk.FileFilter()
        dfilter.set_name(".desktop")
        dfilter.add_pattern("*.desktop")
        dfilter.add_mime_type("application/x-desktop")
        savedialog.add_filter(dfilter)

        response = savedialog.run()
        # Call the save function
        if response == Gtk.ResponseType.OK:
            save_file.savedf(self, savedialog.get_filename())

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

        # Chosen type is Link (2)
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

# Create main window       
window = MainGui()
Gtk.main()


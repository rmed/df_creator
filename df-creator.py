from gi.repository import Gtk

class MainGui:
    
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("gui/df-creator.glade")
        self.builder.connect_signals(self)
        self.win = self.builder.get_object("main_window")
        self.win.show_all()

    def on_delete_window(self, *args):
        Gtk.main_quit(*args)

    def on_new_click(self, widget):
        entries = {
            "entry_name", "entry_command", "entry_icon", "entry_type"
        }
        for entry in entries:
            self.builder.get_object(entry).set_text('')

        self.builder.get_object("switch_terminal").set_active(False)
        
    def on_save_click(self, widget):
        savedialog = Gtk.FileChooserDialog("Save file", self.win, Gtk.FileChooserAction.SAVE, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.OK))

        dfilter = Gtk.FileFilter()
        dfilter.set_name(".desktop files")
        dfilter.add_mime_type("application/x-desktop")
        savedialog.add_filter(dfilter)

        response = savedialog.run()
        if response == Gtk.ResponseType.OK:
            #print savedialog.get_filename()
            self.save_desktop_file(savedialog.get_filename())

        savedialog.destroy()
        
    def save_desktop_file(self, filepath):
        # Get values from GUI fields
        name = self.builder.get_object("entry_name").get_text()
        command = self.builder.get_object("entry_command").get_text()
        icon = self.builder.get_object("entry_icon").get_text()
        apptype = self.builder.get_object("entry_type").get_text()

        category_index = self.builder.get_object("cbox_category").get_active()
        category_model = self.builder.get_object("cbox_category").get_model()
        category = category_model[category_index][0]


        useterm = "false"
        if self.builder.get_object("switch_terminal").get_active():
            useterm = "true"

        # Define the contents of the file
        contents = ["[Desktop Entry]\n", "Name=" + name + "\n", "Exec=" + command + "\n", "Icon=" + icon + "\n", "Type=" + apptype + "\n", "Terminal=" + useterm + "\n", "Categories=" + category + ";"]

        try:
            dfile = open(filepath, "w")
            try:
                dfile.writelines(contents)
            finally:
                dfile.close()
        except IOError:
            pass 
        
window = MainGui()
Gtk.main()


